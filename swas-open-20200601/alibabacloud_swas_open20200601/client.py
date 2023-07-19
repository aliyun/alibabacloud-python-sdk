# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_swas_open20200601 import models as swas__open20200601_models
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
        self._endpoint = self.get_endpoint('swas-open', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_public_connection_with_options(
        self,
        request: swas__open20200601_models.AllocatePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.AllocatePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocatePublicConnection',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.AllocatePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_public_connection_with_options_async(
        self,
        request: swas__open20200601_models.AllocatePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.AllocatePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocatePublicConnection',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.AllocatePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_public_connection(
        self,
        request: swas__open20200601_models.AllocatePublicConnectionRequest,
    ) -> swas__open20200601_models.AllocatePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_connection_with_options(request, runtime)

    async def allocate_public_connection_async(
        self,
        request: swas__open20200601_models.AllocatePublicConnectionRequest,
    ) -> swas__open20200601_models.AllocatePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_public_connection_with_options_async(request, runtime)

    def create_custom_image_with_options(
        self,
        request: swas__open20200601_models.CreateCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateCustomImageResponse:
        """
        A custom image is created based on a snapshot of a simple application server. You can use custom images to create multiple simple application servers that have the same configurations. You can also share custom images with ECS and use the shared images to create ECS instances or replace the OSs of existing ECS instances.
        For more information about custom images, see [Overview of custom images](~~199375~~).
        You must create a system disk snapshot of a simple application server before you create a custom image of the simple application server. For more information, see [CreateSnapshot](~~190452~~).
        >  If you need the data on the data disk of a simple application server when you create a custom image, create a snapshot for the data disk first.
        When you create a custom image, take note of the following items:
        *   The custom image and the corresponding simple application server reside in the same region.
        *   The maximum number of custom images that can be retained in an Alibaba Cloud account is triple of the number of simple application servers that you created. The value cannot be greater than 15.
        *   You can directly create a custom image only based on the system disk snapshot of a simple application server. If you want a custom image to contain the data on the data disk of the simple application server, you must select a data disk snapshot when you create the custom image.
        *   If a simple application server is released due to expiration or refunds, the custom images that are created based on the server are also released.
        *   If you reset a simple application sever, the disk data on the server is cleared. You must back up the data as needed.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: CreateCustomImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_snapshot_id):
            query['DataSnapshotId'] = request.data_snapshot_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomImage',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateCustomImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_image_with_options_async(
        self,
        request: swas__open20200601_models.CreateCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateCustomImageResponse:
        """
        A custom image is created based on a snapshot of a simple application server. You can use custom images to create multiple simple application servers that have the same configurations. You can also share custom images with ECS and use the shared images to create ECS instances or replace the OSs of existing ECS instances.
        For more information about custom images, see [Overview of custom images](~~199375~~).
        You must create a system disk snapshot of a simple application server before you create a custom image of the simple application server. For more information, see [CreateSnapshot](~~190452~~).
        >  If you need the data on the data disk of a simple application server when you create a custom image, create a snapshot for the data disk first.
        When you create a custom image, take note of the following items:
        *   The custom image and the corresponding simple application server reside in the same region.
        *   The maximum number of custom images that can be retained in an Alibaba Cloud account is triple of the number of simple application servers that you created. The value cannot be greater than 15.
        *   You can directly create a custom image only based on the system disk snapshot of a simple application server. If you want a custom image to contain the data on the data disk of the simple application server, you must select a data disk snapshot when you create the custom image.
        *   If a simple application server is released due to expiration or refunds, the custom images that are created based on the server are also released.
        *   If you reset a simple application sever, the disk data on the server is cleared. You must back up the data as needed.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: CreateCustomImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_snapshot_id):
            query['DataSnapshotId'] = request.data_snapshot_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomImage',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateCustomImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_image(
        self,
        request: swas__open20200601_models.CreateCustomImageRequest,
    ) -> swas__open20200601_models.CreateCustomImageResponse:
        """
        A custom image is created based on a snapshot of a simple application server. You can use custom images to create multiple simple application servers that have the same configurations. You can also share custom images with ECS and use the shared images to create ECS instances or replace the OSs of existing ECS instances.
        For more information about custom images, see [Overview of custom images](~~199375~~).
        You must create a system disk snapshot of a simple application server before you create a custom image of the simple application server. For more information, see [CreateSnapshot](~~190452~~).
        >  If you need the data on the data disk of a simple application server when you create a custom image, create a snapshot for the data disk first.
        When you create a custom image, take note of the following items:
        *   The custom image and the corresponding simple application server reside in the same region.
        *   The maximum number of custom images that can be retained in an Alibaba Cloud account is triple of the number of simple application servers that you created. The value cannot be greater than 15.
        *   You can directly create a custom image only based on the system disk snapshot of a simple application server. If you want a custom image to contain the data on the data disk of the simple application server, you must select a data disk snapshot when you create the custom image.
        *   If a simple application server is released due to expiration or refunds, the custom images that are created based on the server are also released.
        *   If you reset a simple application sever, the disk data on the server is cleared. You must back up the data as needed.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: CreateCustomImageRequest
        @return: CreateCustomImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_image_with_options(request, runtime)

    async def create_custom_image_async(
        self,
        request: swas__open20200601_models.CreateCustomImageRequest,
    ) -> swas__open20200601_models.CreateCustomImageResponse:
        """
        A custom image is created based on a snapshot of a simple application server. You can use custom images to create multiple simple application servers that have the same configurations. You can also share custom images with ECS and use the shared images to create ECS instances or replace the OSs of existing ECS instances.
        For more information about custom images, see [Overview of custom images](~~199375~~).
        You must create a system disk snapshot of a simple application server before you create a custom image of the simple application server. For more information, see [CreateSnapshot](~~190452~~).
        >  If you need the data on the data disk of a simple application server when you create a custom image, create a snapshot for the data disk first.
        When you create a custom image, take note of the following items:
        *   The custom image and the corresponding simple application server reside in the same region.
        *   The maximum number of custom images that can be retained in an Alibaba Cloud account is triple of the number of simple application servers that you created. The value cannot be greater than 15.
        *   You can directly create a custom image only based on the system disk snapshot of a simple application server. If you want a custom image to contain the data on the data disk of the simple application server, you must select a data disk snapshot when you create the custom image.
        *   If a simple application server is released due to expiration or refunds, the custom images that are created based on the server are also released.
        *   If you reset a simple application sever, the disk data on the server is cleared. You must back up the data as needed.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: CreateCustomImageRequest
        @return: CreateCustomImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_image_with_options_async(request, runtime)

    def create_firewall_rule_with_options(
        self,
        request: swas__open20200601_models.CreateFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateFirewallRuleResponse:
        """
        Firewalls serve to control network access to simple application servers and isolate security domains in the cloud. By default, Secure Shell (SSH) port 22, HTTP port 80, and HTTPS port 443 are enabled for simple application servers. Other ports are disabled. You can add firewall rules to enable more ports.
        
        @param request: CreateFirewallRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFirewallRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rule_protocol):
            query['RuleProtocol'] = request.rule_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateFirewallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_firewall_rule_with_options_async(
        self,
        request: swas__open20200601_models.CreateFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateFirewallRuleResponse:
        """
        Firewalls serve to control network access to simple application servers and isolate security domains in the cloud. By default, Secure Shell (SSH) port 22, HTTP port 80, and HTTPS port 443 are enabled for simple application servers. Other ports are disabled. You can add firewall rules to enable more ports.
        
        @param request: CreateFirewallRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFirewallRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rule_protocol):
            query['RuleProtocol'] = request.rule_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateFirewallRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_firewall_rule(
        self,
        request: swas__open20200601_models.CreateFirewallRuleRequest,
    ) -> swas__open20200601_models.CreateFirewallRuleResponse:
        """
        Firewalls serve to control network access to simple application servers and isolate security domains in the cloud. By default, Secure Shell (SSH) port 22, HTTP port 80, and HTTPS port 443 are enabled for simple application servers. Other ports are disabled. You can add firewall rules to enable more ports.
        
        @param request: CreateFirewallRuleRequest
        @return: CreateFirewallRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_firewall_rule_with_options(request, runtime)

    async def create_firewall_rule_async(
        self,
        request: swas__open20200601_models.CreateFirewallRuleRequest,
    ) -> swas__open20200601_models.CreateFirewallRuleResponse:
        """
        Firewalls serve to control network access to simple application servers and isolate security domains in the cloud. By default, Secure Shell (SSH) port 22, HTTP port 80, and HTTPS port 443 are enabled for simple application servers. Other ports are disabled. You can add firewall rules to enable more ports.
        
        @param request: CreateFirewallRuleRequest
        @return: CreateFirewallRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_firewall_rule_with_options_async(request, runtime)

    def create_firewall_rules_with_options(
        self,
        tmp_req: swas__open20200601_models.CreateFirewallRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateFirewallRulesResponse:
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.CreateFirewallRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.firewall_rules):
            request.firewall_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.firewall_rules, 'FirewallRules', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.firewall_rules_shrink):
            query['FirewallRules'] = request.firewall_rules_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFirewallRules',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateFirewallRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_firewall_rules_with_options_async(
        self,
        tmp_req: swas__open20200601_models.CreateFirewallRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateFirewallRulesResponse:
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.CreateFirewallRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.firewall_rules):
            request.firewall_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.firewall_rules, 'FirewallRules', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.firewall_rules_shrink):
            query['FirewallRules'] = request.firewall_rules_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFirewallRules',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateFirewallRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_firewall_rules(
        self,
        request: swas__open20200601_models.CreateFirewallRulesRequest,
    ) -> swas__open20200601_models.CreateFirewallRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_firewall_rules_with_options(request, runtime)

    async def create_firewall_rules_async(
        self,
        request: swas__open20200601_models.CreateFirewallRulesRequest,
    ) -> swas__open20200601_models.CreateFirewallRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_firewall_rules_with_options_async(request, runtime)

    def create_instance_key_pair_with_options(
        self,
        request: swas__open20200601_models.CreateInstanceKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateInstanceKeyPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceKeyPair',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateInstanceKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_key_pair_with_options_async(
        self,
        request: swas__open20200601_models.CreateInstanceKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateInstanceKeyPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceKeyPair',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateInstanceKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_key_pair(
        self,
        request: swas__open20200601_models.CreateInstanceKeyPairRequest,
    ) -> swas__open20200601_models.CreateInstanceKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_key_pair_with_options(request, runtime)

    async def create_instance_key_pair_async(
        self,
        request: swas__open20200601_models.CreateInstanceKeyPairRequest,
    ) -> swas__open20200601_models.CreateInstanceKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_key_pair_with_options_async(request, runtime)

    def create_instances_with_options(
        self,
        request: swas__open20200601_models.CreateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateInstancesResponse:
        """
        Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](~~58623~~).
        *   A maximum of 20 simple application servers can be created within an Alibaba Cloud account.
        *   When you call this operation to create simple application servers, make sure that the balance in your account is sufficient to pay for the servers. If the balance in your account is insufficient, the servers cannot be created.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: CreateInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instances_with_options_async(
        self,
        request: swas__open20200601_models.CreateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateInstancesResponse:
        """
        Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](~~58623~~).
        *   A maximum of 20 simple application servers can be created within an Alibaba Cloud account.
        *   When you call this operation to create simple application servers, make sure that the balance in your account is sufficient to pay for the servers. If the balance in your account is insufficient, the servers cannot be created.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: CreateInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instances(
        self,
        request: swas__open20200601_models.CreateInstancesRequest,
    ) -> swas__open20200601_models.CreateInstancesResponse:
        """
        Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](~~58623~~).
        *   A maximum of 20 simple application servers can be created within an Alibaba Cloud account.
        *   When you call this operation to create simple application servers, make sure that the balance in your account is sufficient to pay for the servers. If the balance in your account is insufficient, the servers cannot be created.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: CreateInstancesRequest
        @return: CreateInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instances_with_options(request, runtime)

    async def create_instances_async(
        self,
        request: swas__open20200601_models.CreateInstancesRequest,
    ) -> swas__open20200601_models.CreateInstancesResponse:
        """
        Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](~~58623~~).
        *   A maximum of 20 simple application servers can be created within an Alibaba Cloud account.
        *   When you call this operation to create simple application servers, make sure that the balance in your account is sufficient to pay for the servers. If the balance in your account is insufficient, the servers cannot be created.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: CreateInstancesRequest
        @return: CreateInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instances_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: swas__open20200601_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateSnapshotResponse:
        """
        A snapshot is a point-in-time backup of a disk. Snapshots can be used to back up data, recover data after accidental instance releases, recover data after network attacks, and create custom images.
        >  You are not charged for creating snapshots for simple application servers.
        ## Precautions
        - You can create up to three snapshots for disks of each simple application server.
        - The maximum number of snapshots that can be retained in an Alibaba Cloud account is triple of the number of simple application servers that are created. The value cannot be greater than 15.
        - If a simple application server is automatically released due to expiration, the snapshots created for the server are deleted.
        - If you create a snapshot for a simple application server before you reset the server, the snapshot is retained after you reset the server but the snapshot cannot be used to roll back the disks of the server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: CreateSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: swas__open20200601_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateSnapshotResponse:
        """
        A snapshot is a point-in-time backup of a disk. Snapshots can be used to back up data, recover data after accidental instance releases, recover data after network attacks, and create custom images.
        >  You are not charged for creating snapshots for simple application servers.
        ## Precautions
        - You can create up to three snapshots for disks of each simple application server.
        - The maximum number of snapshots that can be retained in an Alibaba Cloud account is triple of the number of simple application servers that are created. The value cannot be greater than 15.
        - If a simple application server is automatically released due to expiration, the snapshots created for the server are deleted.
        - If you create a snapshot for a simple application server before you reset the server, the snapshot is retained after you reset the server but the snapshot cannot be used to roll back the disks of the server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: CreateSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.CreateSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_snapshot(
        self,
        request: swas__open20200601_models.CreateSnapshotRequest,
    ) -> swas__open20200601_models.CreateSnapshotResponse:
        """
        A snapshot is a point-in-time backup of a disk. Snapshots can be used to back up data, recover data after accidental instance releases, recover data after network attacks, and create custom images.
        >  You are not charged for creating snapshots for simple application servers.
        ## Precautions
        - You can create up to three snapshots for disks of each simple application server.
        - The maximum number of snapshots that can be retained in an Alibaba Cloud account is triple of the number of simple application servers that are created. The value cannot be greater than 15.
        - If a simple application server is automatically released due to expiration, the snapshots created for the server are deleted.
        - If you create a snapshot for a simple application server before you reset the server, the snapshot is retained after you reset the server but the snapshot cannot be used to roll back the disks of the server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: CreateSnapshotRequest
        @return: CreateSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: swas__open20200601_models.CreateSnapshotRequest,
    ) -> swas__open20200601_models.CreateSnapshotResponse:
        """
        A snapshot is a point-in-time backup of a disk. Snapshots can be used to back up data, recover data after accidental instance releases, recover data after network attacks, and create custom images.
        >  You are not charged for creating snapshots for simple application servers.
        ## Precautions
        - You can create up to three snapshots for disks of each simple application server.
        - The maximum number of snapshots that can be retained in an Alibaba Cloud account is triple of the number of simple application servers that are created. The value cannot be greater than 15.
        - If a simple application server is automatically released due to expiration, the snapshots created for the server are deleted.
        - If you create a snapshot for a simple application server before you reset the server, the snapshot is retained after you reset the server but the snapshot cannot be used to roll back the disks of the server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: CreateSnapshotRequest
        @return: CreateSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def delete_custom_image_with_options(
        self,
        request: swas__open20200601_models.DeleteCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteCustomImageResponse:
        """
        You can delete a custom image that you no longer need. After the custom image is deleted, the simple application servers that were created from the custom image cannot be reset by using the custom image.
        >  If a custom image is shared, you must unshare the image before you can delete it. After a custom image is unshared, you cannot query the custom image by using the Elastic Compute Service (ECS) console or by calling ECS API operations. If you need to use the custom image in ECS, we recommend that you copy the image before you delete it. For more information, see [Copy custom images](~~199378~~).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: DeleteCustomImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomImage',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteCustomImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_image_with_options_async(
        self,
        request: swas__open20200601_models.DeleteCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteCustomImageResponse:
        """
        You can delete a custom image that you no longer need. After the custom image is deleted, the simple application servers that were created from the custom image cannot be reset by using the custom image.
        >  If a custom image is shared, you must unshare the image before you can delete it. After a custom image is unshared, you cannot query the custom image by using the Elastic Compute Service (ECS) console or by calling ECS API operations. If you need to use the custom image in ECS, we recommend that you copy the image before you delete it. For more information, see [Copy custom images](~~199378~~).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: DeleteCustomImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomImage',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteCustomImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_image(
        self,
        request: swas__open20200601_models.DeleteCustomImageRequest,
    ) -> swas__open20200601_models.DeleteCustomImageResponse:
        """
        You can delete a custom image that you no longer need. After the custom image is deleted, the simple application servers that were created from the custom image cannot be reset by using the custom image.
        >  If a custom image is shared, you must unshare the image before you can delete it. After a custom image is unshared, you cannot query the custom image by using the Elastic Compute Service (ECS) console or by calling ECS API operations. If you need to use the custom image in ECS, we recommend that you copy the image before you delete it. For more information, see [Copy custom images](~~199378~~).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: DeleteCustomImageRequest
        @return: DeleteCustomImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_image_with_options(request, runtime)

    async def delete_custom_image_async(
        self,
        request: swas__open20200601_models.DeleteCustomImageRequest,
    ) -> swas__open20200601_models.DeleteCustomImageResponse:
        """
        You can delete a custom image that you no longer need. After the custom image is deleted, the simple application servers that were created from the custom image cannot be reset by using the custom image.
        >  If a custom image is shared, you must unshare the image before you can delete it. After a custom image is unshared, you cannot query the custom image by using the Elastic Compute Service (ECS) console or by calling ECS API operations. If you need to use the custom image in ECS, we recommend that you copy the image before you delete it. For more information, see [Copy custom images](~~199378~~).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: DeleteCustomImageRequest
        @return: DeleteCustomImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_image_with_options_async(request, runtime)

    def delete_firewall_rule_with_options(
        self,
        request: swas__open20200601_models.DeleteFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteFirewallRuleResponse:
        """
        After a firewall rule is deleted, your business deployed on the simple application server may become inaccessible. Before you delete a firewall rule, make sure that the firewall rule is no longer needed by the simple application server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: DeleteFirewallRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFirewallRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteFirewallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_firewall_rule_with_options_async(
        self,
        request: swas__open20200601_models.DeleteFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteFirewallRuleResponse:
        """
        After a firewall rule is deleted, your business deployed on the simple application server may become inaccessible. Before you delete a firewall rule, make sure that the firewall rule is no longer needed by the simple application server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: DeleteFirewallRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFirewallRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteFirewallRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_firewall_rule(
        self,
        request: swas__open20200601_models.DeleteFirewallRuleRequest,
    ) -> swas__open20200601_models.DeleteFirewallRuleResponse:
        """
        After a firewall rule is deleted, your business deployed on the simple application server may become inaccessible. Before you delete a firewall rule, make sure that the firewall rule is no longer needed by the simple application server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: DeleteFirewallRuleRequest
        @return: DeleteFirewallRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_firewall_rule_with_options(request, runtime)

    async def delete_firewall_rule_async(
        self,
        request: swas__open20200601_models.DeleteFirewallRuleRequest,
    ) -> swas__open20200601_models.DeleteFirewallRuleResponse:
        """
        After a firewall rule is deleted, your business deployed on the simple application server may become inaccessible. Before you delete a firewall rule, make sure that the firewall rule is no longer needed by the simple application server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: DeleteFirewallRuleRequest
        @return: DeleteFirewallRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_firewall_rule_with_options_async(request, runtime)

    def delete_instance_key_pair_with_options(
        self,
        request: swas__open20200601_models.DeleteInstanceKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteInstanceKeyPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceKeyPair',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteInstanceKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_key_pair_with_options_async(
        self,
        request: swas__open20200601_models.DeleteInstanceKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteInstanceKeyPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceKeyPair',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteInstanceKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_key_pair(
        self,
        request: swas__open20200601_models.DeleteInstanceKeyPairRequest,
    ) -> swas__open20200601_models.DeleteInstanceKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_key_pair_with_options(request, runtime)

    async def delete_instance_key_pair_async(
        self,
        request: swas__open20200601_models.DeleteInstanceKeyPairRequest,
    ) -> swas__open20200601_models.DeleteInstanceKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_key_pair_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: swas__open20200601_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteSnapshotResponse:
        """
        You can delete a snapshot that is no longer needed.
        >  If a custom image was created from the snapshot, delete the custom image before you delete the snapshot.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: DeleteSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: swas__open20200601_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteSnapshotResponse:
        """
        You can delete a snapshot that is no longer needed.
        >  If a custom image was created from the snapshot, delete the custom image before you delete the snapshot.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: DeleteSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshot(
        self,
        request: swas__open20200601_models.DeleteSnapshotRequest,
    ) -> swas__open20200601_models.DeleteSnapshotResponse:
        """
        You can delete a snapshot that is no longer needed.
        >  If a custom image was created from the snapshot, delete the custom image before you delete the snapshot.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: DeleteSnapshotRequest
        @return: DeleteSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: swas__open20200601_models.DeleteSnapshotRequest,
    ) -> swas__open20200601_models.DeleteSnapshotResponse:
        """
        You can delete a snapshot that is no longer needed.
        >  If a custom image was created from the snapshot, delete the custom image before you delete the snapshot.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: DeleteSnapshotRequest
        @return: DeleteSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def delete_snapshots_with_options(
        self,
        request: swas__open20200601_models.DeleteSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteSnapshotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshots',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshots_with_options_async(
        self,
        request: swas__open20200601_models.DeleteSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteSnapshotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshots',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DeleteSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshots(
        self,
        request: swas__open20200601_models.DeleteSnapshotsRequest,
    ) -> swas__open20200601_models.DeleteSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshots_with_options(request, runtime)

    async def delete_snapshots_async(
        self,
        request: swas__open20200601_models.DeleteSnapshotsRequest,
    ) -> swas__open20200601_models.DeleteSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshots_with_options_async(request, runtime)

    def describe_cloud_assistant_status_with_options(
        self,
        tmp_req: swas__open20200601_models.DescribeCloudAssistantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCloudAssistantStatusResponse:
        """
        By default, the Cloud Assistant client is installed on your simple application server. If you have manually uninstalled the client, you must reinstall the client. Otherwise, you cannot run commands on the server.
        
        @param tmp_req: DescribeCloudAssistantStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudAssistantStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.DescribeCloudAssistantStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudAssistantStatus',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeCloudAssistantStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_assistant_status_with_options_async(
        self,
        tmp_req: swas__open20200601_models.DescribeCloudAssistantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCloudAssistantStatusResponse:
        """
        By default, the Cloud Assistant client is installed on your simple application server. If you have manually uninstalled the client, you must reinstall the client. Otherwise, you cannot run commands on the server.
        
        @param tmp_req: DescribeCloudAssistantStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudAssistantStatusResponse
        """
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.DescribeCloudAssistantStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudAssistantStatus',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeCloudAssistantStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_assistant_status(
        self,
        request: swas__open20200601_models.DescribeCloudAssistantStatusRequest,
    ) -> swas__open20200601_models.DescribeCloudAssistantStatusResponse:
        """
        By default, the Cloud Assistant client is installed on your simple application server. If you have manually uninstalled the client, you must reinstall the client. Otherwise, you cannot run commands on the server.
        
        @param request: DescribeCloudAssistantStatusRequest
        @return: DescribeCloudAssistantStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_assistant_status_with_options(request, runtime)

    async def describe_cloud_assistant_status_async(
        self,
        request: swas__open20200601_models.DescribeCloudAssistantStatusRequest,
    ) -> swas__open20200601_models.DescribeCloudAssistantStatusResponse:
        """
        By default, the Cloud Assistant client is installed on your simple application server. If you have manually uninstalled the client, you must reinstall the client. Otherwise, you cannot run commands on the server.
        
        @param request: DescribeCloudAssistantStatusRequest
        @return: DescribeCloudAssistantStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_assistant_status_with_options_async(request, runtime)

    def describe_cloud_monitor_agent_statuses_with_options(
        self,
        request: swas__open20200601_models.DescribeCloudMonitorAgentStatusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCloudMonitorAgentStatusesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudMonitorAgentStatuses',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeCloudMonitorAgentStatusesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_monitor_agent_statuses_with_options_async(
        self,
        request: swas__open20200601_models.DescribeCloudMonitorAgentStatusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCloudMonitorAgentStatusesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudMonitorAgentStatuses',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeCloudMonitorAgentStatusesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_monitor_agent_statuses(
        self,
        request: swas__open20200601_models.DescribeCloudMonitorAgentStatusesRequest,
    ) -> swas__open20200601_models.DescribeCloudMonitorAgentStatusesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_monitor_agent_statuses_with_options(request, runtime)

    async def describe_cloud_monitor_agent_statuses_async(
        self,
        request: swas__open20200601_models.DescribeCloudMonitorAgentStatusesRequest,
    ) -> swas__open20200601_models.DescribeCloudMonitorAgentStatusesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_monitor_agent_statuses_with_options_async(request, runtime)

    def describe_database_error_logs_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseErrorLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseErrorLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseErrorLogs',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseErrorLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_error_logs_with_options_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseErrorLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseErrorLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseErrorLogs',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseErrorLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_error_logs(
        self,
        request: swas__open20200601_models.DescribeDatabaseErrorLogsRequest,
    ) -> swas__open20200601_models.DescribeDatabaseErrorLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_database_error_logs_with_options(request, runtime)

    async def describe_database_error_logs_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseErrorLogsRequest,
    ) -> swas__open20200601_models.DescribeDatabaseErrorLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_error_logs_with_options_async(request, runtime)

    def describe_database_instance_metric_data_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseInstanceMetricData',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_instance_metric_data_with_options_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseInstanceMetricData',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_instance_metric_data(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceMetricDataRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_database_instance_metric_data_with_options(request, runtime)

    async def describe_database_instance_metric_data_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceMetricDataRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_instance_metric_data_with_options_async(request, runtime)

    def describe_database_instance_parameters_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseInstanceParameters',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseInstanceParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_instance_parameters_with_options_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseInstanceParameters',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseInstanceParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_instance_parameters(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceParametersRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_database_instance_parameters_with_options(request, runtime)

    async def describe_database_instance_parameters_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceParametersRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_instance_parameters_with_options_async(request, runtime)

    def describe_database_instances_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_ids):
            query['DatabaseInstanceIds'] = request.database_instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_instances_with_options_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_ids):
            query['DatabaseInstanceIds'] = request.database_instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_instances(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstancesRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_database_instances_with_options(request, runtime)

    async def describe_database_instances_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstancesRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_instances_with_options_async(request, runtime)

    def describe_database_slow_log_records_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseSlowLogRecords',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_database_slow_log_records_with_options_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabaseSlowLogRecords',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_database_slow_log_records(
        self,
        request: swas__open20200601_models.DescribeDatabaseSlowLogRecordsRequest,
    ) -> swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_database_slow_log_records_with_options(request, runtime)

    async def describe_database_slow_log_records_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseSlowLogRecordsRequest,
    ) -> swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_slow_log_records_with_options_async(request, runtime)

    def describe_instance_key_pair_with_options(
        self,
        request: swas__open20200601_models.DescribeInstanceKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInstanceKeyPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceKeyPair',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInstanceKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_key_pair_with_options_async(
        self,
        request: swas__open20200601_models.DescribeInstanceKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInstanceKeyPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceKeyPair',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInstanceKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_key_pair(
        self,
        request: swas__open20200601_models.DescribeInstanceKeyPairRequest,
    ) -> swas__open20200601_models.DescribeInstanceKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_key_pair_with_options(request, runtime)

    async def describe_instance_key_pair_async(
        self,
        request: swas__open20200601_models.DescribeInstanceKeyPairRequest,
    ) -> swas__open20200601_models.DescribeInstanceKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_key_pair_with_options_async(request, runtime)

    def describe_instance_passwords_setting_with_options(
        self,
        request: swas__open20200601_models.DescribeInstancePasswordsSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInstancePasswordsSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstancePasswordsSetting',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInstancePasswordsSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_passwords_setting_with_options_async(
        self,
        request: swas__open20200601_models.DescribeInstancePasswordsSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInstancePasswordsSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstancePasswordsSetting',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInstancePasswordsSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_passwords_setting(
        self,
        request: swas__open20200601_models.DescribeInstancePasswordsSettingRequest,
    ) -> swas__open20200601_models.DescribeInstancePasswordsSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_passwords_setting_with_options(request, runtime)

    async def describe_instance_passwords_setting_async(
        self,
        request: swas__open20200601_models.DescribeInstancePasswordsSettingRequest,
    ) -> swas__open20200601_models.DescribeInstancePasswordsSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_passwords_setting_with_options_async(request, runtime)

    def describe_instance_vnc_url_with_options(
        self,
        request: swas__open20200601_models.DescribeInstanceVncUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInstanceVncUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceVncUrl',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInstanceVncUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_vnc_url_with_options_async(
        self,
        request: swas__open20200601_models.DescribeInstanceVncUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInstanceVncUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceVncUrl',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInstanceVncUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_vnc_url(
        self,
        request: swas__open20200601_models.DescribeInstanceVncUrlRequest,
    ) -> swas__open20200601_models.DescribeInstanceVncUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_vnc_url_with_options(request, runtime)

    async def describe_instance_vnc_url_async(
        self,
        request: swas__open20200601_models.DescribeInstanceVncUrlRequest,
    ) -> swas__open20200601_models.DescribeInstanceVncUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_vnc_url_with_options_async(request, runtime)

    def describe_invocation_result_with_options(
        self,
        request: swas__open20200601_models.DescribeInvocationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInvocationResultResponse:
        """
        After you run a command, the command may not succeed or return the expected results. You can call this operation to query the actual execution results.
        *   You can query the execution information that is generated within the last two weeks. Up to 100,000 lines of execution information can be retained.
        
        @param request: DescribeInvocationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInvocationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocationResult',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInvocationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invocation_result_with_options_async(
        self,
        request: swas__open20200601_models.DescribeInvocationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInvocationResultResponse:
        """
        After you run a command, the command may not succeed or return the expected results. You can call this operation to query the actual execution results.
        *   You can query the execution information that is generated within the last two weeks. Up to 100,000 lines of execution information can be retained.
        
        @param request: DescribeInvocationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInvocationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocationResult',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInvocationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invocation_result(
        self,
        request: swas__open20200601_models.DescribeInvocationResultRequest,
    ) -> swas__open20200601_models.DescribeInvocationResultResponse:
        """
        After you run a command, the command may not succeed or return the expected results. You can call this operation to query the actual execution results.
        *   You can query the execution information that is generated within the last two weeks. Up to 100,000 lines of execution information can be retained.
        
        @param request: DescribeInvocationResultRequest
        @return: DescribeInvocationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_invocation_result_with_options(request, runtime)

    async def describe_invocation_result_async(
        self,
        request: swas__open20200601_models.DescribeInvocationResultRequest,
    ) -> swas__open20200601_models.DescribeInvocationResultResponse:
        """
        After you run a command, the command may not succeed or return the expected results. You can call this operation to query the actual execution results.
        *   You can query the execution information that is generated within the last two weeks. Up to 100,000 lines of execution information can be retained.
        
        @param request: DescribeInvocationResultRequest
        @return: DescribeInvocationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocation_result_with_options_async(request, runtime)

    def describe_invocations_with_options(
        self,
        request: swas__open20200601_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInvocationsResponse:
        """
        After you run a command, the command may not succeed or deliver the expected results. You can call this operation to query the actual execution results.
        *   You can query the execution information that is generated within the last two weeks. Up to 100,000 lines of execution information can be retained.
        
        @param request: DescribeInvocationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInvocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_status):
            query['InvokeStatus'] = request.invoke_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocations',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invocations_with_options_async(
        self,
        request: swas__open20200601_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInvocationsResponse:
        """
        After you run a command, the command may not succeed or deliver the expected results. You can call this operation to query the actual execution results.
        *   You can query the execution information that is generated within the last two weeks. Up to 100,000 lines of execution information can be retained.
        
        @param request: DescribeInvocationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInvocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invoke_status):
            query['InvokeStatus'] = request.invoke_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocations',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeInvocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invocations(
        self,
        request: swas__open20200601_models.DescribeInvocationsRequest,
    ) -> swas__open20200601_models.DescribeInvocationsResponse:
        """
        After you run a command, the command may not succeed or deliver the expected results. You can call this operation to query the actual execution results.
        *   You can query the execution information that is generated within the last two weeks. Up to 100,000 lines of execution information can be retained.
        
        @param request: DescribeInvocationsRequest
        @return: DescribeInvocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    async def describe_invocations_async(
        self,
        request: swas__open20200601_models.DescribeInvocationsRequest,
    ) -> swas__open20200601_models.DescribeInvocationsResponse:
        """
        After you run a command, the command may not succeed or deliver the expected results. You can call this operation to query the actual execution results.
        *   You can query the execution information that is generated within the last two weeks. Up to 100,000 lines of execution information can be retained.
        
        @param request: DescribeInvocationsRequest
        @return: DescribeInvocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocations_with_options_async(request, runtime)

    def describe_monitor_data_with_options(
        self,
        request: swas__open20200601_models.DescribeMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeMonitorDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorData',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_data_with_options_async(
        self,
        request: swas__open20200601_models.DescribeMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeMonitorDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMonitorData',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_data(
        self,
        request: swas__open20200601_models.DescribeMonitorDataRequest,
    ) -> swas__open20200601_models.DescribeMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_data_with_options(request, runtime)

    async def describe_monitor_data_async(
        self,
        request: swas__open20200601_models.DescribeMonitorDataRequest,
    ) -> swas__open20200601_models.DescribeMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_data_with_options_async(request, runtime)

    def describe_security_agent_status_with_options(
        self,
        request: swas__open20200601_models.DescribeSecurityAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeSecurityAgentStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityAgentStatus',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeSecurityAgentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_agent_status_with_options_async(
        self,
        request: swas__open20200601_models.DescribeSecurityAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeSecurityAgentStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityAgentStatus',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DescribeSecurityAgentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_agent_status(
        self,
        request: swas__open20200601_models.DescribeSecurityAgentStatusRequest,
    ) -> swas__open20200601_models.DescribeSecurityAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_agent_status_with_options(request, runtime)

    async def describe_security_agent_status_async(
        self,
        request: swas__open20200601_models.DescribeSecurityAgentStatusRequest,
    ) -> swas__open20200601_models.DescribeSecurityAgentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_agent_status_with_options_async(request, runtime)

    def disable_firewall_rule_with_options(
        self,
        request: swas__open20200601_models.DisableFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DisableFirewallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DisableFirewallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_firewall_rule_with_options_async(
        self,
        request: swas__open20200601_models.DisableFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DisableFirewallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.DisableFirewallRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_firewall_rule(
        self,
        request: swas__open20200601_models.DisableFirewallRuleRequest,
    ) -> swas__open20200601_models.DisableFirewallRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_firewall_rule_with_options(request, runtime)

    async def disable_firewall_rule_async(
        self,
        request: swas__open20200601_models.DisableFirewallRuleRequest,
    ) -> swas__open20200601_models.DisableFirewallRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_firewall_rule_with_options_async(request, runtime)

    def enable_firewall_rule_with_options(
        self,
        request: swas__open20200601_models.EnableFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.EnableFirewallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.EnableFirewallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_firewall_rule_with_options_async(
        self,
        request: swas__open20200601_models.EnableFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.EnableFirewallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.EnableFirewallRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_firewall_rule(
        self,
        request: swas__open20200601_models.EnableFirewallRuleRequest,
    ) -> swas__open20200601_models.EnableFirewallRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_firewall_rule_with_options(request, runtime)

    async def enable_firewall_rule_async(
        self,
        request: swas__open20200601_models.EnableFirewallRuleRequest,
    ) -> swas__open20200601_models.EnableFirewallRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_firewall_rule_with_options_async(request, runtime)

    def install_cloud_assistant_with_options(
        self,
        tmp_req: swas__open20200601_models.InstallCloudAssistantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.InstallCloudAssistantResponse:
        """
        To run commands, you must install the Cloud Assistant client on your simple application server. You can call the [DescribeCloudAssistantStatus](~~439512~~) operation to query whether the Cloud Assistant client is installed on your simple application server. If you have not installed the Cloud Assistant client, you can call the InstallCloudAssistant operation to install the client. Then, you can call the [RebootInstance](~~190443~~) operation to restart the server to allow the installation to take effect.
        
        @param tmp_req: InstallCloudAssistantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallCloudAssistantResponse
        """
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.InstallCloudAssistantShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallCloudAssistant',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.InstallCloudAssistantResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_cloud_assistant_with_options_async(
        self,
        tmp_req: swas__open20200601_models.InstallCloudAssistantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.InstallCloudAssistantResponse:
        """
        To run commands, you must install the Cloud Assistant client on your simple application server. You can call the [DescribeCloudAssistantStatus](~~439512~~) operation to query whether the Cloud Assistant client is installed on your simple application server. If you have not installed the Cloud Assistant client, you can call the InstallCloudAssistant operation to install the client. Then, you can call the [RebootInstance](~~190443~~) operation to restart the server to allow the installation to take effect.
        
        @param tmp_req: InstallCloudAssistantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallCloudAssistantResponse
        """
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.InstallCloudAssistantShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallCloudAssistant',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.InstallCloudAssistantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_cloud_assistant(
        self,
        request: swas__open20200601_models.InstallCloudAssistantRequest,
    ) -> swas__open20200601_models.InstallCloudAssistantResponse:
        """
        To run commands, you must install the Cloud Assistant client on your simple application server. You can call the [DescribeCloudAssistantStatus](~~439512~~) operation to query whether the Cloud Assistant client is installed on your simple application server. If you have not installed the Cloud Assistant client, you can call the InstallCloudAssistant operation to install the client. Then, you can call the [RebootInstance](~~190443~~) operation to restart the server to allow the installation to take effect.
        
        @param request: InstallCloudAssistantRequest
        @return: InstallCloudAssistantResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_cloud_assistant_with_options(request, runtime)

    async def install_cloud_assistant_async(
        self,
        request: swas__open20200601_models.InstallCloudAssistantRequest,
    ) -> swas__open20200601_models.InstallCloudAssistantResponse:
        """
        To run commands, you must install the Cloud Assistant client on your simple application server. You can call the [DescribeCloudAssistantStatus](~~439512~~) operation to query whether the Cloud Assistant client is installed on your simple application server. If you have not installed the Cloud Assistant client, you can call the InstallCloudAssistant operation to install the client. Then, you can call the [RebootInstance](~~190443~~) operation to restart the server to allow the installation to take effect.
        
        @param request: InstallCloudAssistantRequest
        @return: InstallCloudAssistantResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.install_cloud_assistant_with_options_async(request, runtime)

    def install_cloud_monitor_agent_with_options(
        self,
        request: swas__open20200601_models.InstallCloudMonitorAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.InstallCloudMonitorAgentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallCloudMonitorAgent',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.InstallCloudMonitorAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_cloud_monitor_agent_with_options_async(
        self,
        request: swas__open20200601_models.InstallCloudMonitorAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.InstallCloudMonitorAgentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallCloudMonitorAgent',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.InstallCloudMonitorAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_cloud_monitor_agent(
        self,
        request: swas__open20200601_models.InstallCloudMonitorAgentRequest,
    ) -> swas__open20200601_models.InstallCloudMonitorAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_cloud_monitor_agent_with_options(request, runtime)

    async def install_cloud_monitor_agent_async(
        self,
        request: swas__open20200601_models.InstallCloudMonitorAgentRequest,
    ) -> swas__open20200601_models.InstallCloudMonitorAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_cloud_monitor_agent_with_options_async(request, runtime)

    def list_custom_images_with_options(
        self,
        request: swas__open20200601_models.ListCustomImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListCustomImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_snapshot_id):
            query['DataSnapshotId'] = request.data_snapshot_id
        if not UtilClient.is_unset(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not UtilClient.is_unset(request.image_names):
            query['ImageNames'] = request.image_names
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomImages',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListCustomImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_images_with_options_async(
        self,
        request: swas__open20200601_models.ListCustomImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListCustomImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_snapshot_id):
            query['DataSnapshotId'] = request.data_snapshot_id
        if not UtilClient.is_unset(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not UtilClient.is_unset(request.image_names):
            query['ImageNames'] = request.image_names
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomImages',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListCustomImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_images(
        self,
        request: swas__open20200601_models.ListCustomImagesRequest,
    ) -> swas__open20200601_models.ListCustomImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_custom_images_with_options(request, runtime)

    async def list_custom_images_async(
        self,
        request: swas__open20200601_models.ListCustomImagesRequest,
    ) -> swas__open20200601_models.ListCustomImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_images_with_options_async(request, runtime)

    def list_disks_with_options(
        self,
        request: swas__open20200601_models.ListDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListDisksResponse:
        """
        ## Usage notes
        You can specify multiple request parameters such as `InstanceId` and `DiskIds`. Specified parameters have logical AND relations. Only the specified parameters are included in the filter conditions.
        
        @param request: ListDisksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDisksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDisks',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListDisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_disks_with_options_async(
        self,
        request: swas__open20200601_models.ListDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListDisksResponse:
        """
        ## Usage notes
        You can specify multiple request parameters such as `InstanceId` and `DiskIds`. Specified parameters have logical AND relations. Only the specified parameters are included in the filter conditions.
        
        @param request: ListDisksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDisksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDisks',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListDisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_disks(
        self,
        request: swas__open20200601_models.ListDisksRequest,
    ) -> swas__open20200601_models.ListDisksResponse:
        """
        ## Usage notes
        You can specify multiple request parameters such as `InstanceId` and `DiskIds`. Specified parameters have logical AND relations. Only the specified parameters are included in the filter conditions.
        
        @param request: ListDisksRequest
        @return: ListDisksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_disks_with_options(request, runtime)

    async def list_disks_async(
        self,
        request: swas__open20200601_models.ListDisksRequest,
    ) -> swas__open20200601_models.ListDisksResponse:
        """
        ## Usage notes
        You can specify multiple request parameters such as `InstanceId` and `DiskIds`. Specified parameters have logical AND relations. Only the specified parameters are included in the filter conditions.
        
        @param request: ListDisksRequest
        @return: ListDisksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_disks_with_options_async(request, runtime)

    def list_firewall_rules_with_options(
        self,
        request: swas__open20200601_models.ListFirewallRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListFirewallRulesResponse:
        """
        You can call the ListFirewallRules operation to query the firewall rule details of a specified simple application server, including the port range, firewall rule ID, and transport layer protocol.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListFirewallRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFirewallRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFirewallRules',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListFirewallRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_firewall_rules_with_options_async(
        self,
        request: swas__open20200601_models.ListFirewallRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListFirewallRulesResponse:
        """
        You can call the ListFirewallRules operation to query the firewall rule details of a specified simple application server, including the port range, firewall rule ID, and transport layer protocol.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListFirewallRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFirewallRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFirewallRules',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListFirewallRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_firewall_rules(
        self,
        request: swas__open20200601_models.ListFirewallRulesRequest,
    ) -> swas__open20200601_models.ListFirewallRulesResponse:
        """
        You can call the ListFirewallRules operation to query the firewall rule details of a specified simple application server, including the port range, firewall rule ID, and transport layer protocol.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListFirewallRulesRequest
        @return: ListFirewallRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_firewall_rules_with_options(request, runtime)

    async def list_firewall_rules_async(
        self,
        request: swas__open20200601_models.ListFirewallRulesRequest,
    ) -> swas__open20200601_models.ListFirewallRulesResponse:
        """
        You can call the ListFirewallRules operation to query the firewall rule details of a specified simple application server, including the port range, firewall rule ID, and transport layer protocol.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListFirewallRulesRequest
        @return: ListFirewallRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_firewall_rules_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        request: swas__open20200601_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListImagesResponse:
        """
        You can query details about one or more images in a specified region, including the IDs, names, and types of the images.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of your calls per second exceeds the limit, throttling is triggered. This may affect your business. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: swas__open20200601_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListImagesResponse:
        """
        You can query details about one or more images in a specified region, including the IDs, names, and types of the images.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of your calls per second exceeds the limit, throttling is triggered. This may affect your business. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: swas__open20200601_models.ListImagesRequest,
    ) -> swas__open20200601_models.ListImagesResponse:
        """
        You can query details about one or more images in a specified region, including the IDs, names, and types of the images.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of your calls per second exceeds the limit, throttling is triggered. This may affect your business. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListImagesRequest
        @return: ListImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: swas__open20200601_models.ListImagesRequest,
    ) -> swas__open20200601_models.ListImagesResponse:
        """
        You can query details about one or more images in a specified region, including the IDs, names, and types of the images.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of your calls per second exceeds the limit, throttling is triggered. This may affect your business. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListImagesRequest
        @return: ListImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def list_instance_plans_modification_with_options(
        self,
        request: swas__open20200601_models.ListInstancePlansModificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancePlansModificationResponse:
        """
        If the plans of your simple application server do not meet your business requirements, you can call the ListInstancePlansModification operation to obtain a list of plans that can be upgraded for your simple application server. Then, you can call the [UpgradeInstance](~~190445~~) operation to upgrade the plans.
        >  We recommend that you create snapshots for the disks of your simple application server to back up data before you upgrade the plans. For more information, see [CreateSnapshot](~~190452~~).
        For the precautions about plan upgrade, see [Upgrade configurations](~~61433~~).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListInstancePlansModificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancePlansModificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancePlansModification',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancePlansModificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_plans_modification_with_options_async(
        self,
        request: swas__open20200601_models.ListInstancePlansModificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancePlansModificationResponse:
        """
        If the plans of your simple application server do not meet your business requirements, you can call the ListInstancePlansModification operation to obtain a list of plans that can be upgraded for your simple application server. Then, you can call the [UpgradeInstance](~~190445~~) operation to upgrade the plans.
        >  We recommend that you create snapshots for the disks of your simple application server to back up data before you upgrade the plans. For more information, see [CreateSnapshot](~~190452~~).
        For the precautions about plan upgrade, see [Upgrade configurations](~~61433~~).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListInstancePlansModificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancePlansModificationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancePlansModification',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancePlansModificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_plans_modification(
        self,
        request: swas__open20200601_models.ListInstancePlansModificationRequest,
    ) -> swas__open20200601_models.ListInstancePlansModificationResponse:
        """
        If the plans of your simple application server do not meet your business requirements, you can call the ListInstancePlansModification operation to obtain a list of plans that can be upgraded for your simple application server. Then, you can call the [UpgradeInstance](~~190445~~) operation to upgrade the plans.
        >  We recommend that you create snapshots for the disks of your simple application server to back up data before you upgrade the plans. For more information, see [CreateSnapshot](~~190452~~).
        For the precautions about plan upgrade, see [Upgrade configurations](~~61433~~).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListInstancePlansModificationRequest
        @return: ListInstancePlansModificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_plans_modification_with_options(request, runtime)

    async def list_instance_plans_modification_async(
        self,
        request: swas__open20200601_models.ListInstancePlansModificationRequest,
    ) -> swas__open20200601_models.ListInstancePlansModificationResponse:
        """
        If the plans of your simple application server do not meet your business requirements, you can call the ListInstancePlansModification operation to obtain a list of plans that can be upgraded for your simple application server. Then, you can call the [UpgradeInstance](~~190445~~) operation to upgrade the plans.
        >  We recommend that you create snapshots for the disks of your simple application server to back up data before you upgrade the plans. For more information, see [CreateSnapshot](~~190452~~).
        For the precautions about plan upgrade, see [Upgrade configurations](~~61433~~).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListInstancePlansModificationRequest
        @return: ListInstancePlansModificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_plans_modification_with_options_async(request, runtime)

    def list_instance_status_with_options(
        self,
        request: swas__open20200601_models.ListInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceStatus',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_status_with_options_async(
        self,
        request: swas__open20200601_models.ListInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceStatus',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_status(
        self,
        request: swas__open20200601_models.ListInstanceStatusRequest,
    ) -> swas__open20200601_models.ListInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_status_with_options(request, runtime)

    async def list_instance_status_async(
        self,
        request: swas__open20200601_models.ListInstanceStatusRequest,
    ) -> swas__open20200601_models.ListInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_status_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: swas__open20200601_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancesResponse:
        """
        You can call this operation to query the details of one or more simple application servers in a specified region, including the names, public IP addresses, internal IP addresses, creation time, and expiration time of the servers.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.public_ip_addresses):
            query['PublicIpAddresses'] = request.public_ip_addresses
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: swas__open20200601_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancesResponse:
        """
        You can call this operation to query the details of one or more simple application servers in a specified region, including the names, public IP addresses, internal IP addresses, creation time, and expiration time of the servers.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.public_ip_addresses):
            query['PublicIpAddresses'] = request.public_ip_addresses
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: swas__open20200601_models.ListInstancesRequest,
    ) -> swas__open20200601_models.ListInstancesResponse:
        """
        You can call this operation to query the details of one or more simple application servers in a specified region, including the names, public IP addresses, internal IP addresses, creation time, and expiration time of the servers.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: swas__open20200601_models.ListInstancesRequest,
    ) -> swas__open20200601_models.ListInstancesResponse:
        """
        You can call this operation to query the details of one or more simple application servers in a specified region, including the names, public IP addresses, internal IP addresses, creation time, and expiration time of the servers.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_instances_traffic_packages_with_options(
        self,
        request: swas__open20200601_models.ListInstancesTrafficPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancesTrafficPackagesResponse:
        """
        You can query the details of data transfer plans for one or more simple application servers, including the data transfer quota, used data transfer quota, unused data transfer quota, and excess data transfers in the current month.
        Simple Application Server provides data transfer quotas in plans. The prices for data transfers within quotas are included in the plans. You are charged for data transfers that exceed the quotas. Take note of the following items:
        *   You are charged only for outbound data transfers from simple application servers over the Internet. You are not charged for inbound data transfers to simple application servers over the Internet.
        *   Outbound data transfers from simple application servers to other Alibaba Cloud services over the Internet consume the data transfer quotas that are included in plans. If the quotas are exceeded, you are charged for the excess data transfers.
        *   You are not charged for data transfers between simple application servers within the same virtual private cloud (VPC).
        For more information, see [Quotas and billing of data transfers](~~86281~~).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListInstancesTrafficPackagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesTrafficPackagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesTrafficPackages',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesTrafficPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_traffic_packages_with_options_async(
        self,
        request: swas__open20200601_models.ListInstancesTrafficPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancesTrafficPackagesResponse:
        """
        You can query the details of data transfer plans for one or more simple application servers, including the data transfer quota, used data transfer quota, unused data transfer quota, and excess data transfers in the current month.
        Simple Application Server provides data transfer quotas in plans. The prices for data transfers within quotas are included in the plans. You are charged for data transfers that exceed the quotas. Take note of the following items:
        *   You are charged only for outbound data transfers from simple application servers over the Internet. You are not charged for inbound data transfers to simple application servers over the Internet.
        *   Outbound data transfers from simple application servers to other Alibaba Cloud services over the Internet consume the data transfer quotas that are included in plans. If the quotas are exceeded, you are charged for the excess data transfers.
        *   You are not charged for data transfers between simple application servers within the same virtual private cloud (VPC).
        For more information, see [Quotas and billing of data transfers](~~86281~~).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListInstancesTrafficPackagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesTrafficPackagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesTrafficPackages',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListInstancesTrafficPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_traffic_packages(
        self,
        request: swas__open20200601_models.ListInstancesTrafficPackagesRequest,
    ) -> swas__open20200601_models.ListInstancesTrafficPackagesResponse:
        """
        You can query the details of data transfer plans for one or more simple application servers, including the data transfer quota, used data transfer quota, unused data transfer quota, and excess data transfers in the current month.
        Simple Application Server provides data transfer quotas in plans. The prices for data transfers within quotas are included in the plans. You are charged for data transfers that exceed the quotas. Take note of the following items:
        *   You are charged only for outbound data transfers from simple application servers over the Internet. You are not charged for inbound data transfers to simple application servers over the Internet.
        *   Outbound data transfers from simple application servers to other Alibaba Cloud services over the Internet consume the data transfer quotas that are included in plans. If the quotas are exceeded, you are charged for the excess data transfers.
        *   You are not charged for data transfers between simple application servers within the same virtual private cloud (VPC).
        For more information, see [Quotas and billing of data transfers](~~86281~~).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListInstancesTrafficPackagesRequest
        @return: ListInstancesTrafficPackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_traffic_packages_with_options(request, runtime)

    async def list_instances_traffic_packages_async(
        self,
        request: swas__open20200601_models.ListInstancesTrafficPackagesRequest,
    ) -> swas__open20200601_models.ListInstancesTrafficPackagesResponse:
        """
        You can query the details of data transfer plans for one or more simple application servers, including the data transfer quota, used data transfer quota, unused data transfer quota, and excess data transfers in the current month.
        Simple Application Server provides data transfer quotas in plans. The prices for data transfers within quotas are included in the plans. You are charged for data transfers that exceed the quotas. Take note of the following items:
        *   You are charged only for outbound data transfers from simple application servers over the Internet. You are not charged for inbound data transfers to simple application servers over the Internet.
        *   Outbound data transfers from simple application servers to other Alibaba Cloud services over the Internet consume the data transfer quotas that are included in plans. If the quotas are exceeded, you are charged for the excess data transfers.
        *   You are not charged for data transfers between simple application servers within the same virtual private cloud (VPC).
        For more information, see [Quotas and billing of data transfers](~~86281~~).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListInstancesTrafficPackagesRequest
        @return: ListInstancesTrafficPackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_traffic_packages_with_options_async(request, runtime)

    def list_plans_with_options(
        self,
        request: swas__open20200601_models.ListPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListPlansResponse:
        """
        You can query the details of all plans provided by Simple Application Server in a specified region, including the IDs, prices, disk sizes, and disk categories of the plans.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlans',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plans_with_options_async(
        self,
        request: swas__open20200601_models.ListPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListPlansResponse:
        """
        You can query the details of all plans provided by Simple Application Server in a specified region, including the IDs, prices, disk sizes, and disk categories of the plans.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlans',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plans(
        self,
        request: swas__open20200601_models.ListPlansRequest,
    ) -> swas__open20200601_models.ListPlansResponse:
        """
        You can query the details of all plans provided by Simple Application Server in a specified region, including the IDs, prices, disk sizes, and disk categories of the plans.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListPlansRequest
        @return: ListPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_plans_with_options(request, runtime)

    async def list_plans_async(
        self,
        request: swas__open20200601_models.ListPlansRequest,
    ) -> swas__open20200601_models.ListPlansResponse:
        """
        You can query the details of all plans provided by Simple Application Server in a specified region, including the IDs, prices, disk sizes, and disk categories of the plans.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListPlansRequest
        @return: ListPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_plans_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListRegionsResponse:
        """
        The query results include all the Alibaba Cloud regions where Simple Application Server is available on the International site (alibabacloud.com) and the China site (aliyun.com).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListRegionsResponse:
        """
        The query results include all the Alibaba Cloud regions where Simple Application Server is available on the International site (alibabacloud.com) and the China site (aliyun.com).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> swas__open20200601_models.ListRegionsResponse:
        """
        The query results include all the Alibaba Cloud regions where Simple Application Server is available on the International site (alibabacloud.com) and the China site (aliyun.com).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> swas__open20200601_models.ListRegionsResponse:
        """
        The query results include all the Alibaba Cloud regions where Simple Application Server is available on the International site (alibabacloud.com) and the China site (aliyun.com).
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_snapshots_with_options(
        self,
        request: swas__open20200601_models.ListSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListSnapshotsResponse:
        """
        ## Description
        You can configure multiple request parameters such as `InstanceId`, `DiskId`, and `SnapshotIds` to query snapshots. Configured parameters have logical AND relations. Only the configured parameters are included in the filter conditions.
        ### QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](~~347607~~).
        
        @param request: ListSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSnapshotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.source_disk_type):
            query['SourceDiskType'] = request.source_disk_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshots',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_snapshots_with_options_async(
        self,
        request: swas__open20200601_models.ListSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListSnapshotsResponse:
        """
        ## Description
        You can configure multiple request parameters such as `InstanceId`, `DiskId`, and `SnapshotIds` to query snapshots. Configured parameters have logical AND relations. Only the configured parameters are included in the filter conditions.
        ### QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](~~347607~~).
        
        @param request: ListSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSnapshotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.source_disk_type):
            query['SourceDiskType'] = request.source_disk_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshots',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_snapshots(
        self,
        request: swas__open20200601_models.ListSnapshotsRequest,
    ) -> swas__open20200601_models.ListSnapshotsResponse:
        """
        ## Description
        You can configure multiple request parameters such as `InstanceId`, `DiskId`, and `SnapshotIds` to query snapshots. Configured parameters have logical AND relations. Only the configured parameters are included in the filter conditions.
        ### QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](~~347607~~).
        
        @param request: ListSnapshotsRequest
        @return: ListSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_snapshots_with_options(request, runtime)

    async def list_snapshots_async(
        self,
        request: swas__open20200601_models.ListSnapshotsRequest,
    ) -> swas__open20200601_models.ListSnapshotsResponse:
        """
        ## Description
        You can configure multiple request parameters such as `InstanceId`, `DiskId`, and `SnapshotIds` to query snapshots. Configured parameters have logical AND relations. Only the configured parameters are included in the filter conditions.
        ### QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](~~347607~~).
        
        @param request: ListSnapshotsRequest
        @return: ListSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_snapshots_with_options_async(request, runtime)

    def login_instance_with_options(
        self,
        request: swas__open20200601_models.LoginInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.LoginInstanceResponse:
        """
        After you create a simple application server, you can log on to the simple application server to build environments and applications on the server.
        
        @param request: LoginInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LoginInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LoginInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.LoginInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def login_instance_with_options_async(
        self,
        request: swas__open20200601_models.LoginInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.LoginInstanceResponse:
        """
        After you create a simple application server, you can log on to the simple application server to build environments and applications on the server.
        
        @param request: LoginInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LoginInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LoginInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.LoginInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def login_instance(
        self,
        request: swas__open20200601_models.LoginInstanceRequest,
    ) -> swas__open20200601_models.LoginInstanceResponse:
        """
        After you create a simple application server, you can log on to the simple application server to build environments and applications on the server.
        
        @param request: LoginInstanceRequest
        @return: LoginInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.login_instance_with_options(request, runtime)

    async def login_instance_async(
        self,
        request: swas__open20200601_models.LoginInstanceRequest,
    ) -> swas__open20200601_models.LoginInstanceResponse:
        """
        After you create a simple application server, you can log on to the simple application server to build environments and applications on the server.
        
        @param request: LoginInstanceRequest
        @return: LoginInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.login_instance_with_options_async(request, runtime)

    def modify_database_instance_description_with_options(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_description):
            query['DatabaseInstanceDescription'] = request.database_instance_description
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseInstanceDescription',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_instance_description_with_options_async(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_description):
            query['DatabaseInstanceDescription'] = request.database_instance_description
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseInstanceDescription',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database_instance_description(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceDescriptionRequest,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_database_instance_description_with_options(request, runtime)

    async def modify_database_instance_description_async(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceDescriptionRequest,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_instance_description_with_options_async(request, runtime)

    def modify_database_instance_parameter_with_options(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceParameterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.force_restart):
            query['ForceRestart'] = request.force_restart
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseInstanceParameter',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyDatabaseInstanceParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_instance_parameter_with_options_async(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceParameterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.force_restart):
            query['ForceRestart'] = request.force_restart
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseInstanceParameter',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyDatabaseInstanceParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database_instance_parameter(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceParameterRequest,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_database_instance_parameter_with_options(request, runtime)

    async def modify_database_instance_parameter_async(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceParameterRequest,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_instance_parameter_with_options_async(request, runtime)

    def modify_firewall_rule_with_options(
        self,
        request: swas__open20200601_models.ModifyFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyFirewallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_protocol):
            query['RuleProtocol'] = request.rule_protocol
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyFirewallRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_firewall_rule_with_options_async(
        self,
        request: swas__open20200601_models.ModifyFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyFirewallRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_protocol):
            query['RuleProtocol'] = request.rule_protocol
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFirewallRule',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyFirewallRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_firewall_rule(
        self,
        request: swas__open20200601_models.ModifyFirewallRuleRequest,
    ) -> swas__open20200601_models.ModifyFirewallRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_firewall_rule_with_options(request, runtime)

    async def modify_firewall_rule_async(
        self,
        request: swas__open20200601_models.ModifyFirewallRuleRequest,
    ) -> swas__open20200601_models.ModifyFirewallRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_firewall_rule_with_options_async(request, runtime)

    def modify_image_share_status_with_options(
        self,
        request: swas__open20200601_models.ModifyImageShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyImageShareStatusResponse:
        """
        You can share a custom image to ECS. When the configurations of your simple application server cannot meet your business requirements, or you want to use ECS instances to deploy your business, you can share your custom image to ECS to transfer your business from Simple Application Server to ECS.
        >  The region in which the shared image resides in ECS is the same as the region in which the custom image resides in Simple Application Server.
        You can unshare a custom image based on your business requirements or when you want to delete the custom image.
        Take note of the following items:
        *   After you unshare a custom image, you cannot query or use the custom image in the ECS console or by calling ECS API operations.
        *   After you unshare a custom image, the system disks of the ECS instances that were created from the shared image cannot be re-initialized.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ModifyImageShareStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyImageShareStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageShareStatus',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyImageShareStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_image_share_status_with_options_async(
        self,
        request: swas__open20200601_models.ModifyImageShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyImageShareStatusResponse:
        """
        You can share a custom image to ECS. When the configurations of your simple application server cannot meet your business requirements, or you want to use ECS instances to deploy your business, you can share your custom image to ECS to transfer your business from Simple Application Server to ECS.
        >  The region in which the shared image resides in ECS is the same as the region in which the custom image resides in Simple Application Server.
        You can unshare a custom image based on your business requirements or when you want to delete the custom image.
        Take note of the following items:
        *   After you unshare a custom image, you cannot query or use the custom image in the ECS console or by calling ECS API operations.
        *   After you unshare a custom image, the system disks of the ECS instances that were created from the shared image cannot be re-initialized.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ModifyImageShareStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyImageShareStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageShareStatus',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyImageShareStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_image_share_status(
        self,
        request: swas__open20200601_models.ModifyImageShareStatusRequest,
    ) -> swas__open20200601_models.ModifyImageShareStatusResponse:
        """
        You can share a custom image to ECS. When the configurations of your simple application server cannot meet your business requirements, or you want to use ECS instances to deploy your business, you can share your custom image to ECS to transfer your business from Simple Application Server to ECS.
        >  The region in which the shared image resides in ECS is the same as the region in which the custom image resides in Simple Application Server.
        You can unshare a custom image based on your business requirements or when you want to delete the custom image.
        Take note of the following items:
        *   After you unshare a custom image, you cannot query or use the custom image in the ECS console or by calling ECS API operations.
        *   After you unshare a custom image, the system disks of the ECS instances that were created from the shared image cannot be re-initialized.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ModifyImageShareStatusRequest
        @return: ModifyImageShareStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_status_with_options(request, runtime)

    async def modify_image_share_status_async(
        self,
        request: swas__open20200601_models.ModifyImageShareStatusRequest,
    ) -> swas__open20200601_models.ModifyImageShareStatusResponse:
        """
        You can share a custom image to ECS. When the configurations of your simple application server cannot meet your business requirements, or you want to use ECS instances to deploy your business, you can share your custom image to ECS to transfer your business from Simple Application Server to ECS.
        >  The region in which the shared image resides in ECS is the same as the region in which the custom image resides in Simple Application Server.
        You can unshare a custom image based on your business requirements or when you want to delete the custom image.
        Take note of the following items:
        *   After you unshare a custom image, you cannot query or use the custom image in the ECS console or by calling ECS API operations.
        *   After you unshare a custom image, the system disks of the ECS instances that were created from the shared image cannot be re-initialized.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ModifyImageShareStatusRequest
        @return: ModifyImageShareStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_share_status_with_options_async(request, runtime)

    def modify_instance_vnc_password_with_options(
        self,
        request: swas__open20200601_models.ModifyInstanceVncPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyInstanceVncPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vnc_password):
            query['VncPassword'] = request.vnc_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVncPassword',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyInstanceVncPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_vnc_password_with_options_async(
        self,
        request: swas__open20200601_models.ModifyInstanceVncPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyInstanceVncPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vnc_password):
            query['VncPassword'] = request.vnc_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVncPassword',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ModifyInstanceVncPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_vnc_password(
        self,
        request: swas__open20200601_models.ModifyInstanceVncPasswordRequest,
    ) -> swas__open20200601_models.ModifyInstanceVncPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vnc_password_with_options(request, runtime)

    async def modify_instance_vnc_password_async(
        self,
        request: swas__open20200601_models.ModifyInstanceVncPasswordRequest,
    ) -> swas__open20200601_models.ModifyInstanceVncPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vnc_password_with_options_async(request, runtime)

    def reboot_instance_with_options(
        self,
        request: swas__open20200601_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RebootInstanceResponse:
        """
        You can restart simple application server instances that are only in the Running (Running) state.
        *   After you restart a simple application server, it enters the Starting (Starting) state.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: RebootInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RebootInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_instance_with_options_async(
        self,
        request: swas__open20200601_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RebootInstanceResponse:
        """
        You can restart simple application server instances that are only in the Running (Running) state.
        *   After you restart a simple application server, it enters the Starting (Starting) state.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: RebootInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RebootInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_instance(
        self,
        request: swas__open20200601_models.RebootInstanceRequest,
    ) -> swas__open20200601_models.RebootInstanceResponse:
        """
        You can restart simple application server instances that are only in the Running (Running) state.
        *   After you restart a simple application server, it enters the Starting (Starting) state.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: RebootInstanceRequest
        @return: RebootInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reboot_instance_with_options(request, runtime)

    async def reboot_instance_async(
        self,
        request: swas__open20200601_models.RebootInstanceRequest,
    ) -> swas__open20200601_models.RebootInstanceResponse:
        """
        You can restart simple application server instances that are only in the Running (Running) state.
        *   After you restart a simple application server, it enters the Starting (Starting) state.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: RebootInstanceRequest
        @return: RebootInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reboot_instance_with_options_async(request, runtime)

    def reboot_instances_with_options(
        self,
        request: swas__open20200601_models.RebootInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RebootInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_reboot):
            query['ForceReboot'] = request.force_reboot
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RebootInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_instances_with_options_async(
        self,
        request: swas__open20200601_models.RebootInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RebootInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_reboot):
            query['ForceReboot'] = request.force_reboot
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RebootInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_instances(
        self,
        request: swas__open20200601_models.RebootInstancesRequest,
    ) -> swas__open20200601_models.RebootInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_instances_with_options(request, runtime)

    async def reboot_instances_async(
        self,
        request: swas__open20200601_models.RebootInstancesRequest,
    ) -> swas__open20200601_models.RebootInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_instances_with_options_async(request, runtime)

    def release_public_connection_with_options(
        self,
        request: swas__open20200601_models.ReleasePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ReleasePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePublicConnection',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ReleasePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_public_connection_with_options_async(
        self,
        request: swas__open20200601_models.ReleasePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ReleasePublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePublicConnection',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ReleasePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_public_connection(
        self,
        request: swas__open20200601_models.ReleasePublicConnectionRequest,
    ) -> swas__open20200601_models.ReleasePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_public_connection_with_options(request, runtime)

    async def release_public_connection_async(
        self,
        request: swas__open20200601_models.ReleasePublicConnectionRequest,
    ) -> swas__open20200601_models.ReleasePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_public_connection_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: swas__open20200601_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RenewInstanceResponse:
        """
        Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](~~58623~~).
        *   When you call this operation to renew a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be renewed.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: RenewInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: swas__open20200601_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RenewInstanceResponse:
        """
        Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](~~58623~~).
        *   When you call this operation to renew a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be renewed.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: RenewInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: swas__open20200601_models.RenewInstanceRequest,
    ) -> swas__open20200601_models.RenewInstanceResponse:
        """
        Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](~~58623~~).
        *   When you call this operation to renew a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be renewed.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: RenewInstanceRequest
        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: swas__open20200601_models.RenewInstanceRequest,
    ) -> swas__open20200601_models.RenewInstanceResponse:
        """
        Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](~~58623~~).
        *   When you call this operation to renew a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be renewed.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: RenewInstanceRequest
        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def reset_database_account_password_with_options(
        self,
        request: swas__open20200601_models.ResetDatabaseAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetDatabaseAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDatabaseAccountPassword',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetDatabaseAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_database_account_password_with_options_async(
        self,
        request: swas__open20200601_models.ResetDatabaseAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetDatabaseAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDatabaseAccountPassword',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetDatabaseAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_database_account_password(
        self,
        request: swas__open20200601_models.ResetDatabaseAccountPasswordRequest,
    ) -> swas__open20200601_models.ResetDatabaseAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_database_account_password_with_options(request, runtime)

    async def reset_database_account_password_async(
        self,
        request: swas__open20200601_models.ResetDatabaseAccountPasswordRequest,
    ) -> swas__open20200601_models.ResetDatabaseAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_database_account_password_with_options_async(request, runtime)

    def reset_disk_with_options(
        self,
        request: swas__open20200601_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetDiskResponse:
        """
        You can call this operation to roll back a disk only when the associated simple application server is in the Stopped state.
        *   After a disk is rolled back, all data changes that are made from when the snapshot was created to when the disk is rolled back are lost. Back up disk data based on your needs before you roll back the disk.
        ## Precautions
        If you reset a simple application server, the disk data on the server is deleted. Snapshots created before the resetting are retained but cannot be used to roll back the disks of the server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ResetDiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetDiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDisk',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_disk_with_options_async(
        self,
        request: swas__open20200601_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetDiskResponse:
        """
        You can call this operation to roll back a disk only when the associated simple application server is in the Stopped state.
        *   After a disk is rolled back, all data changes that are made from when the snapshot was created to when the disk is rolled back are lost. Back up disk data based on your needs before you roll back the disk.
        ## Precautions
        If you reset a simple application server, the disk data on the server is deleted. Snapshots created before the resetting are retained but cannot be used to roll back the disks of the server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ResetDiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetDiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDisk',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_disk(
        self,
        request: swas__open20200601_models.ResetDiskRequest,
    ) -> swas__open20200601_models.ResetDiskResponse:
        """
        You can call this operation to roll back a disk only when the associated simple application server is in the Stopped state.
        *   After a disk is rolled back, all data changes that are made from when the snapshot was created to when the disk is rolled back are lost. Back up disk data based on your needs before you roll back the disk.
        ## Precautions
        If you reset a simple application server, the disk data on the server is deleted. Snapshots created before the resetting are retained but cannot be used to roll back the disks of the server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ResetDiskRequest
        @return: ResetDiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_disk_with_options(request, runtime)

    async def reset_disk_async(
        self,
        request: swas__open20200601_models.ResetDiskRequest,
    ) -> swas__open20200601_models.ResetDiskResponse:
        """
        You can call this operation to roll back a disk only when the associated simple application server is in the Stopped state.
        *   After a disk is rolled back, all data changes that are made from when the snapshot was created to when the disk is rolled back are lost. Back up disk data based on your needs before you roll back the disk.
        ## Precautions
        If you reset a simple application server, the disk data on the server is deleted. Snapshots created before the resetting are retained but cannot be used to roll back the disks of the server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ResetDiskRequest
        @return: ResetDiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_disk_with_options_async(request, runtime)

    def reset_system_with_options(
        self,
        request: swas__open20200601_models.ResetSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetSystemResponse:
        """
        You can reset a simple application server to re-install its applications or operating system and re-initialize the server. You can reset a simple application server by resetting the operating system or replacing the image.
        You can use one of the following methods to reset a simple application server:
        *   Reset the operating system. You can re-install the operating system without the need to replace the image.
        *   Replace the image. You can replace the existing image on the simple application server by using another Alibaba Cloud image or a custom image. This effectively replaces the operating system.
        ## Precautions
        - If you reset a simple application sever, the disk data on the server is cleared. You must back up the data as needed.
        - After you reset a simple application server, the monitoring operations that are performed on the server may fail. You can use one of the following methods to install the CloudMonitor agent on the server:    - Connect to the server: For more information, see [Manually install plug-ins for Alibaba Cloud hosts](/help/en/cloudmonitor/latest/install-and-uninstall-the-cloudmonitor-agent-for-cpp).
        - Use Command Assistant: For more information, see [Use Command Assistant](/help/en/simple-application-server/latest/cloud-assistant). You can obtain the commands that are used to install CloudMonitor from the "Common commands" section in the [Use Command Assistant](/help/en/simple-application-server/latest/cloud-assistant) topic.
        ## Limits
        - If a simple application server is reset, snapshots that are created before the server is reset are retained, but the snapshots cannot be used to roll back the disks of the server.
        - If a simple application server was created based on a custom image that contains data of a data disk, the server cannot be reset.
        - If you reset a simple application server by replacing the existing image with a custom image,   - The custom image must reside in the same region as the current server.
        - The custom image cannot be created from the current server. If you want to recover the data on the server, you can use a snapshot that is created from the server to roll back the disks.
        - If your simple application server resides in a region outside the Chinese mainland, you cannot switch the operating system of the server between Windows Server and Linux. You cannot use a Windows Server custom image to reset a Linux simple application server. Similarly, you cannot use a Linux custom image to reset a Windows Server simple application server. You can switch the operating system of simple application servers only between Windows Server operating systems or between Linux distributions.
        - The following limits apply to the disks on the simple application server:     - If the custom image contains a system disk and data disks, but the simple application server is not attached with a data disk but attached only with a system disk, you cannot use the custom image to reset the simple application server.
        - If the system disk size of the custom image is greater than the system disk size of the simple application server, you cannot directly use the custom image to reset the simple application server.
        - When the system disk size of the simple application server is greater than or equal to the system disk size of the custom image, you can use the custom image to reset the simple application server. To increase the system disk size of the server, you can upgrade the simple application server. For more information, see Upgrade configurations.
        - If the data disk size of the custom image is greater than the data disk size of the simple application server, you cannot use the custom image to reset the simple application server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ResetSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSystem',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_system_with_options_async(
        self,
        request: swas__open20200601_models.ResetSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetSystemResponse:
        """
        You can reset a simple application server to re-install its applications or operating system and re-initialize the server. You can reset a simple application server by resetting the operating system or replacing the image.
        You can use one of the following methods to reset a simple application server:
        *   Reset the operating system. You can re-install the operating system without the need to replace the image.
        *   Replace the image. You can replace the existing image on the simple application server by using another Alibaba Cloud image or a custom image. This effectively replaces the operating system.
        ## Precautions
        - If you reset a simple application sever, the disk data on the server is cleared. You must back up the data as needed.
        - After you reset a simple application server, the monitoring operations that are performed on the server may fail. You can use one of the following methods to install the CloudMonitor agent on the server:    - Connect to the server: For more information, see [Manually install plug-ins for Alibaba Cloud hosts](/help/en/cloudmonitor/latest/install-and-uninstall-the-cloudmonitor-agent-for-cpp).
        - Use Command Assistant: For more information, see [Use Command Assistant](/help/en/simple-application-server/latest/cloud-assistant). You can obtain the commands that are used to install CloudMonitor from the "Common commands" section in the [Use Command Assistant](/help/en/simple-application-server/latest/cloud-assistant) topic.
        ## Limits
        - If a simple application server is reset, snapshots that are created before the server is reset are retained, but the snapshots cannot be used to roll back the disks of the server.
        - If a simple application server was created based on a custom image that contains data of a data disk, the server cannot be reset.
        - If you reset a simple application server by replacing the existing image with a custom image,   - The custom image must reside in the same region as the current server.
        - The custom image cannot be created from the current server. If you want to recover the data on the server, you can use a snapshot that is created from the server to roll back the disks.
        - If your simple application server resides in a region outside the Chinese mainland, you cannot switch the operating system of the server between Windows Server and Linux. You cannot use a Windows Server custom image to reset a Linux simple application server. Similarly, you cannot use a Linux custom image to reset a Windows Server simple application server. You can switch the operating system of simple application servers only between Windows Server operating systems or between Linux distributions.
        - The following limits apply to the disks on the simple application server:     - If the custom image contains a system disk and data disks, but the simple application server is not attached with a data disk but attached only with a system disk, you cannot use the custom image to reset the simple application server.
        - If the system disk size of the custom image is greater than the system disk size of the simple application server, you cannot directly use the custom image to reset the simple application server.
        - When the system disk size of the simple application server is greater than or equal to the system disk size of the custom image, you can use the custom image to reset the simple application server. To increase the system disk size of the server, you can upgrade the simple application server. For more information, see Upgrade configurations.
        - If the data disk size of the custom image is greater than the data disk size of the simple application server, you cannot use the custom image to reset the simple application server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ResetSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSystem',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ResetSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_system(
        self,
        request: swas__open20200601_models.ResetSystemRequest,
    ) -> swas__open20200601_models.ResetSystemResponse:
        """
        You can reset a simple application server to re-install its applications or operating system and re-initialize the server. You can reset a simple application server by resetting the operating system or replacing the image.
        You can use one of the following methods to reset a simple application server:
        *   Reset the operating system. You can re-install the operating system without the need to replace the image.
        *   Replace the image. You can replace the existing image on the simple application server by using another Alibaba Cloud image or a custom image. This effectively replaces the operating system.
        ## Precautions
        - If you reset a simple application sever, the disk data on the server is cleared. You must back up the data as needed.
        - After you reset a simple application server, the monitoring operations that are performed on the server may fail. You can use one of the following methods to install the CloudMonitor agent on the server:    - Connect to the server: For more information, see [Manually install plug-ins for Alibaba Cloud hosts](/help/en/cloudmonitor/latest/install-and-uninstall-the-cloudmonitor-agent-for-cpp).
        - Use Command Assistant: For more information, see [Use Command Assistant](/help/en/simple-application-server/latest/cloud-assistant). You can obtain the commands that are used to install CloudMonitor from the "Common commands" section in the [Use Command Assistant](/help/en/simple-application-server/latest/cloud-assistant) topic.
        ## Limits
        - If a simple application server is reset, snapshots that are created before the server is reset are retained, but the snapshots cannot be used to roll back the disks of the server.
        - If a simple application server was created based on a custom image that contains data of a data disk, the server cannot be reset.
        - If you reset a simple application server by replacing the existing image with a custom image,   - The custom image must reside in the same region as the current server.
        - The custom image cannot be created from the current server. If you want to recover the data on the server, you can use a snapshot that is created from the server to roll back the disks.
        - If your simple application server resides in a region outside the Chinese mainland, you cannot switch the operating system of the server between Windows Server and Linux. You cannot use a Windows Server custom image to reset a Linux simple application server. Similarly, you cannot use a Linux custom image to reset a Windows Server simple application server. You can switch the operating system of simple application servers only between Windows Server operating systems or between Linux distributions.
        - The following limits apply to the disks on the simple application server:     - If the custom image contains a system disk and data disks, but the simple application server is not attached with a data disk but attached only with a system disk, you cannot use the custom image to reset the simple application server.
        - If the system disk size of the custom image is greater than the system disk size of the simple application server, you cannot directly use the custom image to reset the simple application server.
        - When the system disk size of the simple application server is greater than or equal to the system disk size of the custom image, you can use the custom image to reset the simple application server. To increase the system disk size of the server, you can upgrade the simple application server. For more information, see Upgrade configurations.
        - If the data disk size of the custom image is greater than the data disk size of the simple application server, you cannot use the custom image to reset the simple application server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ResetSystemRequest
        @return: ResetSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_system_with_options(request, runtime)

    async def reset_system_async(
        self,
        request: swas__open20200601_models.ResetSystemRequest,
    ) -> swas__open20200601_models.ResetSystemResponse:
        """
        You can reset a simple application server to re-install its applications or operating system and re-initialize the server. You can reset a simple application server by resetting the operating system or replacing the image.
        You can use one of the following methods to reset a simple application server:
        *   Reset the operating system. You can re-install the operating system without the need to replace the image.
        *   Replace the image. You can replace the existing image on the simple application server by using another Alibaba Cloud image or a custom image. This effectively replaces the operating system.
        ## Precautions
        - If you reset a simple application sever, the disk data on the server is cleared. You must back up the data as needed.
        - After you reset a simple application server, the monitoring operations that are performed on the server may fail. You can use one of the following methods to install the CloudMonitor agent on the server:    - Connect to the server: For more information, see [Manually install plug-ins for Alibaba Cloud hosts](/help/en/cloudmonitor/latest/install-and-uninstall-the-cloudmonitor-agent-for-cpp).
        - Use Command Assistant: For more information, see [Use Command Assistant](/help/en/simple-application-server/latest/cloud-assistant). You can obtain the commands that are used to install CloudMonitor from the "Common commands" section in the [Use Command Assistant](/help/en/simple-application-server/latest/cloud-assistant) topic.
        ## Limits
        - If a simple application server is reset, snapshots that are created before the server is reset are retained, but the snapshots cannot be used to roll back the disks of the server.
        - If a simple application server was created based on a custom image that contains data of a data disk, the server cannot be reset.
        - If you reset a simple application server by replacing the existing image with a custom image,   - The custom image must reside in the same region as the current server.
        - The custom image cannot be created from the current server. If you want to recover the data on the server, you can use a snapshot that is created from the server to roll back the disks.
        - If your simple application server resides in a region outside the Chinese mainland, you cannot switch the operating system of the server between Windows Server and Linux. You cannot use a Windows Server custom image to reset a Linux simple application server. Similarly, you cannot use a Linux custom image to reset a Windows Server simple application server. You can switch the operating system of simple application servers only between Windows Server operating systems or between Linux distributions.
        - The following limits apply to the disks on the simple application server:     - If the custom image contains a system disk and data disks, but the simple application server is not attached with a data disk but attached only with a system disk, you cannot use the custom image to reset the simple application server.
        - If the system disk size of the custom image is greater than the system disk size of the simple application server, you cannot directly use the custom image to reset the simple application server.
        - When the system disk size of the simple application server is greater than or equal to the system disk size of the custom image, you can use the custom image to reset the simple application server. To increase the system disk size of the server, you can upgrade the simple application server. For more information, see Upgrade configurations.
        - If the data disk size of the custom image is greater than the data disk size of the simple application server, you cannot use the custom image to reset the simple application server.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: ResetSystemRequest
        @return: ResetSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_system_with_options_async(request, runtime)

    def restart_database_instance_with_options(
        self,
        request: swas__open20200601_models.RestartDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RestartDatabaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDatabaseInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RestartDatabaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_database_instance_with_options_async(
        self,
        request: swas__open20200601_models.RestartDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RestartDatabaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDatabaseInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RestartDatabaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_database_instance(
        self,
        request: swas__open20200601_models.RestartDatabaseInstanceRequest,
    ) -> swas__open20200601_models.RestartDatabaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_database_instance_with_options(request, runtime)

    async def restart_database_instance_async(
        self,
        request: swas__open20200601_models.RestartDatabaseInstanceRequest,
    ) -> swas__open20200601_models.RestartDatabaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_database_instance_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        tmp_req: swas__open20200601_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RunCommandResponse:
        """
        Command Assistant is a Simple Application Server-specific automated O\\&M tool. You can manage simple application servers by running shell, PowerShell, and batch commands in the Simple Application Server console without logging on to the servers.
        When you use Command Assistant, the following conditions must be met:
        *   The simple application server must be in the Running state.
        *   The Cloud Assistant client is installed on the server. By default, the Cloud Assistant client is installed on simple application servers. If you manually uninstall the client, you must reinstall it. For more information, see [Install the Cloud Assistant client](~~64921~~).
        
        @param tmp_req: RunCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCommandResponse
        """
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.RunCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.enable_parameter):
            query['EnableParameter'] = request.enable_parameter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.windows_password_name):
            query['WindowsPasswordName'] = request.windows_password_name
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        if not UtilClient.is_unset(request.working_user):
            query['WorkingUser'] = request.working_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_command_with_options_async(
        self,
        tmp_req: swas__open20200601_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RunCommandResponse:
        """
        Command Assistant is a Simple Application Server-specific automated O\\&M tool. You can manage simple application servers by running shell, PowerShell, and batch commands in the Simple Application Server console without logging on to the servers.
        When you use Command Assistant, the following conditions must be met:
        *   The simple application server must be in the Running state.
        *   The Cloud Assistant client is installed on the server. By default, the Cloud Assistant client is installed on simple application servers. If you manually uninstall the client, you must reinstall it. For more information, see [Install the Cloud Assistant client](~~64921~~).
        
        @param tmp_req: RunCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCommandResponse
        """
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.RunCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.enable_parameter):
            query['EnableParameter'] = request.enable_parameter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.windows_password_name):
            query['WindowsPasswordName'] = request.windows_password_name
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        if not UtilClient.is_unset(request.working_user):
            query['WorkingUser'] = request.working_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.RunCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_command(
        self,
        request: swas__open20200601_models.RunCommandRequest,
    ) -> swas__open20200601_models.RunCommandResponse:
        """
        Command Assistant is a Simple Application Server-specific automated O\\&M tool. You can manage simple application servers by running shell, PowerShell, and batch commands in the Simple Application Server console without logging on to the servers.
        When you use Command Assistant, the following conditions must be met:
        *   The simple application server must be in the Running state.
        *   The Cloud Assistant client is installed on the server. By default, the Cloud Assistant client is installed on simple application servers. If you manually uninstall the client, you must reinstall it. For more information, see [Install the Cloud Assistant client](~~64921~~).
        
        @param request: RunCommandRequest
        @return: RunCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: swas__open20200601_models.RunCommandRequest,
    ) -> swas__open20200601_models.RunCommandResponse:
        """
        Command Assistant is a Simple Application Server-specific automated O\\&M tool. You can manage simple application servers by running shell, PowerShell, and batch commands in the Simple Application Server console without logging on to the servers.
        When you use Command Assistant, the following conditions must be met:
        *   The simple application server must be in the Running state.
        *   The Cloud Assistant client is installed on the server. By default, the Cloud Assistant client is installed on simple application servers. If you manually uninstall the client, you must reinstall it. For more information, see [Install the Cloud Assistant client](~~64921~~).
        
        @param request: RunCommandRequest
        @return: RunCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def start_database_instance_with_options(
        self,
        request: swas__open20200601_models.StartDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartDatabaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDatabaseInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartDatabaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_database_instance_with_options_async(
        self,
        request: swas__open20200601_models.StartDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartDatabaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDatabaseInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartDatabaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_database_instance(
        self,
        request: swas__open20200601_models.StartDatabaseInstanceRequest,
    ) -> swas__open20200601_models.StartDatabaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_database_instance_with_options(request, runtime)

    async def start_database_instance_async(
        self,
        request: swas__open20200601_models.StartDatabaseInstanceRequest,
    ) -> swas__open20200601_models.StartDatabaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_database_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: swas__open20200601_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartInstanceResponse:
        """
        If your simple application server is in the Stopped state, you can call the StartInstance operation to start the server.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: StartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: swas__open20200601_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartInstanceResponse:
        """
        If your simple application server is in the Stopped state, you can call the StartInstance operation to start the server.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: StartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance(
        self,
        request: swas__open20200601_models.StartInstanceRequest,
    ) -> swas__open20200601_models.StartInstanceResponse:
        """
        If your simple application server is in the Stopped state, you can call the StartInstance operation to start the server.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: swas__open20200601_models.StartInstanceRequest,
    ) -> swas__open20200601_models.StartInstanceResponse:
        """
        If your simple application server is in the Stopped state, you can call the StartInstance operation to start the server.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def start_instances_with_options(
        self,
        request: swas__open20200601_models.StartInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instances_with_options_async(
        self,
        request: swas__open20200601_models.StartInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instances(
        self,
        request: swas__open20200601_models.StartInstancesRequest,
    ) -> swas__open20200601_models.StartInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instances_with_options(request, runtime)

    async def start_instances_async(
        self,
        request: swas__open20200601_models.StartInstancesRequest,
    ) -> swas__open20200601_models.StartInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instances_with_options_async(request, runtime)

    def start_terminal_session_with_options(
        self,
        request: swas__open20200601_models.StartTerminalSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartTerminalSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTerminalSession',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartTerminalSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_terminal_session_with_options_async(
        self,
        request: swas__open20200601_models.StartTerminalSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartTerminalSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTerminalSession',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StartTerminalSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_terminal_session(
        self,
        request: swas__open20200601_models.StartTerminalSessionRequest,
    ) -> swas__open20200601_models.StartTerminalSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_terminal_session_with_options(request, runtime)

    async def start_terminal_session_async(
        self,
        request: swas__open20200601_models.StartTerminalSessionRequest,
    ) -> swas__open20200601_models.StartTerminalSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_terminal_session_with_options_async(request, runtime)

    def stop_database_instance_with_options(
        self,
        request: swas__open20200601_models.StopDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopDatabaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDatabaseInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopDatabaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_database_instance_with_options_async(
        self,
        request: swas__open20200601_models.StopDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopDatabaseInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_instance_id):
            query['DatabaseInstanceId'] = request.database_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDatabaseInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopDatabaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_database_instance(
        self,
        request: swas__open20200601_models.StopDatabaseInstanceRequest,
    ) -> swas__open20200601_models.StopDatabaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_database_instance_with_options(request, runtime)

    async def stop_database_instance_async(
        self,
        request: swas__open20200601_models.StopDatabaseInstanceRequest,
    ) -> swas__open20200601_models.StopDatabaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_database_instance_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: swas__open20200601_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopInstanceResponse:
        """
        You can stop simple application servers that are not used for the time being.
        >  The stopping of simple application server may interrupt your business. We recommend that you perform the stop operation during off-peak hours.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: StopInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: swas__open20200601_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopInstanceResponse:
        """
        You can stop simple application servers that are not used for the time being.
        >  The stopping of simple application server may interrupt your business. We recommend that you perform the stop operation during off-peak hours.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: StopInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        request: swas__open20200601_models.StopInstanceRequest,
    ) -> swas__open20200601_models.StopInstanceResponse:
        """
        You can stop simple application servers that are not used for the time being.
        >  The stopping of simple application server may interrupt your business. We recommend that you perform the stop operation during off-peak hours.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: swas__open20200601_models.StopInstanceRequest,
    ) -> swas__open20200601_models.StopInstanceResponse:
        """
        You can stop simple application servers that are not used for the time being.
        >  The stopping of simple application server may interrupt your business. We recommend that you perform the stop operation during off-peak hours.
        ## QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def stop_instances_with_options(
        self,
        request: swas__open20200601_models.StopInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instances_with_options_async(
        self,
        request: swas__open20200601_models.StopInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstances',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.StopInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instances(
        self,
        request: swas__open20200601_models.StopInstancesRequest,
    ) -> swas__open20200601_models.StopInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instances_with_options(request, runtime)

    async def stop_instances_async(
        self,
        request: swas__open20200601_models.StopInstancesRequest,
    ) -> swas__open20200601_models.StopInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instances_with_options_async(request, runtime)

    def update_disk_attribute_with_options(
        self,
        request: swas__open20200601_models.UpdateDiskAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateDiskAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDiskAttribute',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpdateDiskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_disk_attribute_with_options_async(
        self,
        request: swas__open20200601_models.UpdateDiskAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateDiskAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDiskAttribute',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpdateDiskAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_disk_attribute(
        self,
        request: swas__open20200601_models.UpdateDiskAttributeRequest,
    ) -> swas__open20200601_models.UpdateDiskAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_disk_attribute_with_options(request, runtime)

    async def update_disk_attribute_async(
        self,
        request: swas__open20200601_models.UpdateDiskAttributeRequest,
    ) -> swas__open20200601_models.UpdateDiskAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_disk_attribute_with_options_async(request, runtime)

    def update_instance_attribute_with_options(
        self,
        request: swas__open20200601_models.UpdateInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateInstanceAttributeResponse:
        """
        After you change the password of a simple application server, you must restart the server by calling the [RebootInstance](~~190443~~) operation for the new password to take effect.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: UpdateInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceAttribute',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpdateInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_attribute_with_options_async(
        self,
        request: swas__open20200601_models.UpdateInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateInstanceAttributeResponse:
        """
        After you change the password of a simple application server, you must restart the server by calling the [RebootInstance](~~190443~~) operation for the new password to take effect.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: UpdateInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceAttribute',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpdateInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_attribute(
        self,
        request: swas__open20200601_models.UpdateInstanceAttributeRequest,
    ) -> swas__open20200601_models.UpdateInstanceAttributeResponse:
        """
        After you change the password of a simple application server, you must restart the server by calling the [RebootInstance](~~190443~~) operation for the new password to take effect.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: UpdateInstanceAttributeRequest
        @return: UpdateInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_attribute_with_options(request, runtime)

    async def update_instance_attribute_async(
        self,
        request: swas__open20200601_models.UpdateInstanceAttributeRequest,
    ) -> swas__open20200601_models.UpdateInstanceAttributeResponse:
        """
        After you change the password of a simple application server, you must restart the server by calling the [RebootInstance](~~190443~~) operation for the new password to take effect.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: UpdateInstanceAttributeRequest
        @return: UpdateInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_attribute_with_options_async(request, runtime)

    def update_snapshot_attribute_with_options(
        self,
        request: swas__open20200601_models.UpdateSnapshotAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateSnapshotAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSnapshotAttribute',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpdateSnapshotAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_snapshot_attribute_with_options_async(
        self,
        request: swas__open20200601_models.UpdateSnapshotAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateSnapshotAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSnapshotAttribute',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpdateSnapshotAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_snapshot_attribute(
        self,
        request: swas__open20200601_models.UpdateSnapshotAttributeRequest,
    ) -> swas__open20200601_models.UpdateSnapshotAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_snapshot_attribute_with_options(request, runtime)

    async def update_snapshot_attribute_async(
        self,
        request: swas__open20200601_models.UpdateSnapshotAttributeRequest,
    ) -> swas__open20200601_models.UpdateSnapshotAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_snapshot_attribute_with_options_async(request, runtime)

    def upgrade_instance_with_options(
        self,
        request: swas__open20200601_models.UpgradeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpgradeInstanceResponse:
        """
        The plans of simple application servers can only be upgraded. For more information about plans, see [Billable items](~~58623~~).
        *   When you call this operation to upgrade a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be upgraded.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: UpgradeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpgradeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_instance_with_options_async(
        self,
        request: swas__open20200601_models.UpgradeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpgradeInstanceResponse:
        """
        The plans of simple application servers can only be upgraded. For more information about plans, see [Billable items](~~58623~~).
        *   When you call this operation to upgrade a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be upgraded.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: UpgradeInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeInstance',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UpgradeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_instance(
        self,
        request: swas__open20200601_models.UpgradeInstanceRequest,
    ) -> swas__open20200601_models.UpgradeInstanceResponse:
        """
        The plans of simple application servers can only be upgraded. For more information about plans, see [Billable items](~~58623~~).
        *   When you call this operation to upgrade a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be upgraded.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: UpgradeInstanceRequest
        @return: UpgradeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_with_options(request, runtime)

    async def upgrade_instance_async(
        self,
        request: swas__open20200601_models.UpgradeInstanceRequest,
    ) -> swas__open20200601_models.UpgradeInstanceResponse:
        """
        The plans of simple application servers can only be upgraded. For more information about plans, see [Billable items](~~58623~~).
        *   When you call this operation to upgrade a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be upgraded.
        ## QPS limits
        The queries per second (QPS) limit for a single user for the API operation is 10 calls per minute. If the number of calls to the API operation per minute exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](/help/en/simple-application-server/latest/qps-limit-1).
        
        @param request: UpgradeInstanceRequest
        @return: UpgradeInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_instance_with_options_async(request, runtime)

    def upload_instance_key_pair_with_options(
        self,
        request: swas__open20200601_models.UploadInstanceKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UploadInstanceKeyPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.public_key):
            query['PublicKey'] = request.public_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadInstanceKeyPair',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UploadInstanceKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_instance_key_pair_with_options_async(
        self,
        request: swas__open20200601_models.UploadInstanceKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UploadInstanceKeyPairResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.public_key):
            query['PublicKey'] = request.public_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadInstanceKeyPair',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.UploadInstanceKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_instance_key_pair(
        self,
        request: swas__open20200601_models.UploadInstanceKeyPairRequest,
    ) -> swas__open20200601_models.UploadInstanceKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_instance_key_pair_with_options(request, runtime)

    async def upload_instance_key_pair_async(
        self,
        request: swas__open20200601_models.UploadInstanceKeyPairRequest,
    ) -> swas__open20200601_models.UploadInstanceKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_instance_key_pair_with_options_async(request, runtime)
