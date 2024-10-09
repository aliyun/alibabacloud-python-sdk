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

    def add_custom_image_share_account_with_options(
        self,
        request: swas__open20200601_models.AddCustomImageShareAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.AddCustomImageShareAccountResponse:
        """
        @summary Shares a custom image with other Alibaba Cloud accounts in the same region to quickly deploy the same environment configurations for multiple simple application servers at a time. This improves deployment efficiency.
        
        @description    Before you share a custom image, make sure that all sensitive data and files are removed from the image.
        The IDs of the Alibaba Cloud accounts with which you want to share the image is obtained. Move the pointer over the profile in the upper-right corner of the Simple Application Server console. In the card that appears, if Main Account is displayed, the showed account ID is the Alibaba Cloud account ID.
        
        @param request: AddCustomImageShareAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomImageShareAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
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
            action='AddCustomImageShareAccount',
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
            swas__open20200601_models.AddCustomImageShareAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_image_share_account_with_options_async(
        self,
        request: swas__open20200601_models.AddCustomImageShareAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.AddCustomImageShareAccountResponse:
        """
        @summary Shares a custom image with other Alibaba Cloud accounts in the same region to quickly deploy the same environment configurations for multiple simple application servers at a time. This improves deployment efficiency.
        
        @description    Before you share a custom image, make sure that all sensitive data and files are removed from the image.
        The IDs of the Alibaba Cloud accounts with which you want to share the image is obtained. Move the pointer over the profile in the upper-right corner of the Simple Application Server console. In the card that appears, if Main Account is displayed, the showed account ID is the Alibaba Cloud account ID.
        
        @param request: AddCustomImageShareAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomImageShareAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
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
            action='AddCustomImageShareAccount',
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
            swas__open20200601_models.AddCustomImageShareAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_image_share_account(
        self,
        request: swas__open20200601_models.AddCustomImageShareAccountRequest,
    ) -> swas__open20200601_models.AddCustomImageShareAccountResponse:
        """
        @summary Shares a custom image with other Alibaba Cloud accounts in the same region to quickly deploy the same environment configurations for multiple simple application servers at a time. This improves deployment efficiency.
        
        @description    Before you share a custom image, make sure that all sensitive data and files are removed from the image.
        The IDs of the Alibaba Cloud accounts with which you want to share the image is obtained. Move the pointer over the profile in the upper-right corner of the Simple Application Server console. In the card that appears, if Main Account is displayed, the showed account ID is the Alibaba Cloud account ID.
        
        @param request: AddCustomImageShareAccountRequest
        @return: AddCustomImageShareAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_custom_image_share_account_with_options(request, runtime)

    async def add_custom_image_share_account_async(
        self,
        request: swas__open20200601_models.AddCustomImageShareAccountRequest,
    ) -> swas__open20200601_models.AddCustomImageShareAccountResponse:
        """
        @summary Shares a custom image with other Alibaba Cloud accounts in the same region to quickly deploy the same environment configurations for multiple simple application servers at a time. This improves deployment efficiency.
        
        @description    Before you share a custom image, make sure that all sensitive data and files are removed from the image.
        The IDs of the Alibaba Cloud accounts with which you want to share the image is obtained. Move the pointer over the profile in the upper-right corner of the Simple Application Server console. In the card that appears, if Main Account is displayed, the showed account ID is the Alibaba Cloud account ID.
        
        @param request: AddCustomImageShareAccountRequest
        @return: AddCustomImageShareAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_custom_image_share_account_with_options_async(request, runtime)

    def allocate_public_connection_with_options(
        self,
        request: swas__open20200601_models.AllocatePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.AllocatePublicConnectionResponse:
        """
        @summary Applies for a public endpoint for a Simple Database Service instance.
        
        @description By default, no public endpoints are assigned to Simple Database Service instances. If you want to access the databases of a Simple Database Service instance over the Internet by using Simple Container Service or Data Management (DMS), you must apply for a public endpoint for the Simple Database Service instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: AllocatePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocatePublicConnectionResponse
        """
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
        """
        @summary Applies for a public endpoint for a Simple Database Service instance.
        
        @description By default, no public endpoints are assigned to Simple Database Service instances. If you want to access the databases of a Simple Database Service instance over the Internet by using Simple Container Service or Data Management (DMS), you must apply for a public endpoint for the Simple Database Service instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: AllocatePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocatePublicConnectionResponse
        """
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
        """
        @summary Applies for a public endpoint for a Simple Database Service instance.
        
        @description By default, no public endpoints are assigned to Simple Database Service instances. If you want to access the databases of a Simple Database Service instance over the Internet by using Simple Container Service or Data Management (DMS), you must apply for a public endpoint for the Simple Database Service instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: AllocatePublicConnectionRequest
        @return: AllocatePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_connection_with_options(request, runtime)

    async def allocate_public_connection_async(
        self,
        request: swas__open20200601_models.AllocatePublicConnectionRequest,
    ) -> swas__open20200601_models.AllocatePublicConnectionResponse:
        """
        @summary Applies for a public endpoint for a Simple Database Service instance.
        
        @description By default, no public endpoints are assigned to Simple Database Service instances. If you want to access the databases of a Simple Database Service instance over the Internet by using Simple Container Service or Data Management (DMS), you must apply for a public endpoint for the Simple Database Service instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: AllocatePublicConnectionRequest
        @return: AllocatePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_public_connection_with_options_async(request, runtime)

    def apply_firewall_template_with_options(
        self,
        request: swas__open20200601_models.ApplyFirewallTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ApplyFirewallTemplateResponse:
        """
        @summary Uses a firewall template to apply firewall rules to multiple simple application servers at a time. This improves your efficiency of setting firewall rules.
        
        @description If the port range, protocol, and source IP address of a firewall rule in a firewall template are the same as the port range, protocol, and source IP address of an existing rule, the new rule overwrites the existing rule regardless of whether the existing rule is enabled or disabled.
        
        @param request: ApplyFirewallTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyFirewallTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyFirewallTemplate',
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
            swas__open20200601_models.ApplyFirewallTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_firewall_template_with_options_async(
        self,
        request: swas__open20200601_models.ApplyFirewallTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ApplyFirewallTemplateResponse:
        """
        @summary Uses a firewall template to apply firewall rules to multiple simple application servers at a time. This improves your efficiency of setting firewall rules.
        
        @description If the port range, protocol, and source IP address of a firewall rule in a firewall template are the same as the port range, protocol, and source IP address of an existing rule, the new rule overwrites the existing rule regardless of whether the existing rule is enabled or disabled.
        
        @param request: ApplyFirewallTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyFirewallTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyFirewallTemplate',
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
            swas__open20200601_models.ApplyFirewallTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_firewall_template(
        self,
        request: swas__open20200601_models.ApplyFirewallTemplateRequest,
    ) -> swas__open20200601_models.ApplyFirewallTemplateResponse:
        """
        @summary Uses a firewall template to apply firewall rules to multiple simple application servers at a time. This improves your efficiency of setting firewall rules.
        
        @description If the port range, protocol, and source IP address of a firewall rule in a firewall template are the same as the port range, protocol, and source IP address of an existing rule, the new rule overwrites the existing rule regardless of whether the existing rule is enabled or disabled.
        
        @param request: ApplyFirewallTemplateRequest
        @return: ApplyFirewallTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_firewall_template_with_options(request, runtime)

    async def apply_firewall_template_async(
        self,
        request: swas__open20200601_models.ApplyFirewallTemplateRequest,
    ) -> swas__open20200601_models.ApplyFirewallTemplateResponse:
        """
        @summary Uses a firewall template to apply firewall rules to multiple simple application servers at a time. This improves your efficiency of setting firewall rules.
        
        @description If the port range, protocol, and source IP address of a firewall rule in a firewall template are the same as the port range, protocol, and source IP address of an existing rule, the new rule overwrites the existing rule regardless of whether the existing rule is enabled or disabled.
        
        @param request: ApplyFirewallTemplateRequest
        @return: ApplyFirewallTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_firewall_template_with_options_async(request, runtime)

    def attach_key_pair_with_options(
        self,
        request: swas__open20200601_models.AttachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.AttachKeyPairResponse:
        """
        @summary Binds a key pair to simple application servers.
        
        @description You can bind only one key pair to a simple application server in the Simple Application Server console. If a simple application server has a key pair bound, the new key pair overwrites the original key pair.
        
        @param request: AttachKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachKeyPair',
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
            swas__open20200601_models.AttachKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_key_pair_with_options_async(
        self,
        request: swas__open20200601_models.AttachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.AttachKeyPairResponse:
        """
        @summary Binds a key pair to simple application servers.
        
        @description You can bind only one key pair to a simple application server in the Simple Application Server console. If a simple application server has a key pair bound, the new key pair overwrites the original key pair.
        
        @param request: AttachKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachKeyPair',
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
            swas__open20200601_models.AttachKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_key_pair(
        self,
        request: swas__open20200601_models.AttachKeyPairRequest,
    ) -> swas__open20200601_models.AttachKeyPairResponse:
        """
        @summary Binds a key pair to simple application servers.
        
        @description You can bind only one key pair to a simple application server in the Simple Application Server console. If a simple application server has a key pair bound, the new key pair overwrites the original key pair.
        
        @param request: AttachKeyPairRequest
        @return: AttachKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_key_pair_with_options(request, runtime)

    async def attach_key_pair_async(
        self,
        request: swas__open20200601_models.AttachKeyPairRequest,
    ) -> swas__open20200601_models.AttachKeyPairResponse:
        """
        @summary Binds a key pair to simple application servers.
        
        @description You can bind only one key pair to a simple application server in the Simple Application Server console. If a simple application server has a key pair bound, the new key pair overwrites the original key pair.
        
        @param request: AttachKeyPairRequest
        @return: AttachKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_key_pair_with_options_async(request, runtime)

    def create_command_with_options(
        self,
        request: swas__open20200601_models.CreateCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateCommandResponse:
        """
        @summary Creates a Cloud Assistant command.
        
        @param request: CreateCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_parameter):
            query['EnableParameter'] = request.enable_parameter
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCommand',
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
            swas__open20200601_models.CreateCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_command_with_options_async(
        self,
        request: swas__open20200601_models.CreateCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateCommandResponse:
        """
        @summary Creates a Cloud Assistant command.
        
        @param request: CreateCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_parameter):
            query['EnableParameter'] = request.enable_parameter
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCommand',
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
            swas__open20200601_models.CreateCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_command(
        self,
        request: swas__open20200601_models.CreateCommandRequest,
    ) -> swas__open20200601_models.CreateCommandResponse:
        """
        @summary Creates a Cloud Assistant command.
        
        @param request: CreateCommandRequest
        @return: CreateCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_command_with_options(request, runtime)

    async def create_command_async(
        self,
        request: swas__open20200601_models.CreateCommandRequest,
    ) -> swas__open20200601_models.CreateCommandResponse:
        """
        @summary Creates a Cloud Assistant command.
        
        @param request: CreateCommandRequest
        @return: CreateCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_command_with_options_async(request, runtime)

    def create_custom_image_with_options(
        self,
        request: swas__open20200601_models.CreateCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateCustomImageResponse:
        """
        @summary Creates a custom image based on a snapshot of a simple application server.
        
        @description A custom image is created based on a snapshot of a simple application server. You can use a custom image to create multiple simple application servers that have the same configurations. You can also share custom images to ECS and use the shared images to create ECS instances or replace the OSs of existing ECS instances. For more information about custom images, see [Overview of custom images](https://help.aliyun.com/document_detail/199375.html).
        You must create a system disk snapshot of a simple application server before you create a custom image based on the snapshot. For more information, see [CreateSnapshot](https://help.aliyun.com/document_detail/190452.html).
        > If you need the data on the data disk of a simple application server when you create a custom image, create a snapshot for the data disk first.
        Before you create a custom image, take note of the following items:
        The custom image and the corresponding simple application server must reside in the same region.
        The maximum number of custom images that can be maintained in an Alibaba Cloud account is triple the number of simple application servers in the account. The value cannot be greater than 15.
        You can directly create a custom image only based on the system disk snapshot of a simple application server. If you want a custom image to contain the data on the data disk of the simple application server, you must select a data disk snapshot when you create the custom image.
        If a simple application server is released due to expiration or refunds, the custom images that are created based on a snapshot of the server are also released.
        If you reset a simple application server by changing the application system or OS of the server or replacing the image of the server, the disk data on the server is cleared. Back up the disk data as needed.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        @summary Creates a custom image based on a snapshot of a simple application server.
        
        @description A custom image is created based on a snapshot of a simple application server. You can use a custom image to create multiple simple application servers that have the same configurations. You can also share custom images to ECS and use the shared images to create ECS instances or replace the OSs of existing ECS instances. For more information about custom images, see [Overview of custom images](https://help.aliyun.com/document_detail/199375.html).
        You must create a system disk snapshot of a simple application server before you create a custom image based on the snapshot. For more information, see [CreateSnapshot](https://help.aliyun.com/document_detail/190452.html).
        > If you need the data on the data disk of a simple application server when you create a custom image, create a snapshot for the data disk first.
        Before you create a custom image, take note of the following items:
        The custom image and the corresponding simple application server must reside in the same region.
        The maximum number of custom images that can be maintained in an Alibaba Cloud account is triple the number of simple application servers in the account. The value cannot be greater than 15.
        You can directly create a custom image only based on the system disk snapshot of a simple application server. If you want a custom image to contain the data on the data disk of the simple application server, you must select a data disk snapshot when you create the custom image.
        If a simple application server is released due to expiration or refunds, the custom images that are created based on a snapshot of the server are also released.
        If you reset a simple application server by changing the application system or OS of the server or replacing the image of the server, the disk data on the server is cleared. Back up the disk data as needed.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        @summary Creates a custom image based on a snapshot of a simple application server.
        
        @description A custom image is created based on a snapshot of a simple application server. You can use a custom image to create multiple simple application servers that have the same configurations. You can also share custom images to ECS and use the shared images to create ECS instances or replace the OSs of existing ECS instances. For more information about custom images, see [Overview of custom images](https://help.aliyun.com/document_detail/199375.html).
        You must create a system disk snapshot of a simple application server before you create a custom image based on the snapshot. For more information, see [CreateSnapshot](https://help.aliyun.com/document_detail/190452.html).
        > If you need the data on the data disk of a simple application server when you create a custom image, create a snapshot for the data disk first.
        Before you create a custom image, take note of the following items:
        The custom image and the corresponding simple application server must reside in the same region.
        The maximum number of custom images that can be maintained in an Alibaba Cloud account is triple the number of simple application servers in the account. The value cannot be greater than 15.
        You can directly create a custom image only based on the system disk snapshot of a simple application server. If you want a custom image to contain the data on the data disk of the simple application server, you must select a data disk snapshot when you create the custom image.
        If a simple application server is released due to expiration or refunds, the custom images that are created based on a snapshot of the server are also released.
        If you reset a simple application server by changing the application system or OS of the server or replacing the image of the server, the disk data on the server is cleared. Back up the disk data as needed.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Creates a custom image based on a snapshot of a simple application server.
        
        @description A custom image is created based on a snapshot of a simple application server. You can use a custom image to create multiple simple application servers that have the same configurations. You can also share custom images to ECS and use the shared images to create ECS instances or replace the OSs of existing ECS instances. For more information about custom images, see [Overview of custom images](https://help.aliyun.com/document_detail/199375.html).
        You must create a system disk snapshot of a simple application server before you create a custom image based on the snapshot. For more information, see [CreateSnapshot](https://help.aliyun.com/document_detail/190452.html).
        > If you need the data on the data disk of a simple application server when you create a custom image, create a snapshot for the data disk first.
        Before you create a custom image, take note of the following items:
        The custom image and the corresponding simple application server must reside in the same region.
        The maximum number of custom images that can be maintained in an Alibaba Cloud account is triple the number of simple application servers in the account. The value cannot be greater than 15.
        You can directly create a custom image only based on the system disk snapshot of a simple application server. If you want a custom image to contain the data on the data disk of the simple application server, you must select a data disk snapshot when you create the custom image.
        If a simple application server is released due to expiration or refunds, the custom images that are created based on a snapshot of the server are also released.
        If you reset a simple application server by changing the application system or OS of the server or replacing the image of the server, the disk data on the server is cleared. Back up the disk data as needed.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Creates a firewall rule for a simple application server.
        
        @description Firewalls serve to control network access to simple application servers and isolate security domains in the cloud. By default, SSH port 22, HTTP port 80, and HTTPS port 443 are enabled for simple application servers. Other ports are disabled. You can add firewall rules to enable more ports.
        ### QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Creates a firewall rule for a simple application server.
        
        @description Firewalls serve to control network access to simple application servers and isolate security domains in the cloud. By default, SSH port 22, HTTP port 80, and HTTPS port 443 are enabled for simple application servers. Other ports are disabled. You can add firewall rules to enable more ports.
        ### QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Creates a firewall rule for a simple application server.
        
        @description Firewalls serve to control network access to simple application servers and isolate security domains in the cloud. By default, SSH port 22, HTTP port 80, and HTTPS port 443 are enabled for simple application servers. Other ports are disabled. You can add firewall rules to enable more ports.
        ### QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Creates a firewall rule for a simple application server.
        
        @description Firewalls serve to control network access to simple application servers and isolate security domains in the cloud. By default, SSH port 22, HTTP port 80, and HTTPS port 443 are enabled for simple application servers. Other ports are disabled. You can add firewall rules to enable more ports.
        ### QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        """
        @summary Creates multiple firewall rules for a simple application server at a time.
        
        @description Firewalls serve to control network access to simple application servers and isolate security domains in the cloud. By default, SSH port 22, HTTP port 80, and HTTPS port 443 are enabled for simple application servers. Other ports are disabled. You can add firewall rules to enable more ports.
        
        @param tmp_req: CreateFirewallRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFirewallRulesResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        @summary Creates multiple firewall rules for a simple application server at a time.
        
        @description Firewalls serve to control network access to simple application servers and isolate security domains in the cloud. By default, SSH port 22, HTTP port 80, and HTTPS port 443 are enabled for simple application servers. Other ports are disabled. You can add firewall rules to enable more ports.
        
        @param tmp_req: CreateFirewallRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFirewallRulesResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        @summary Creates multiple firewall rules for a simple application server at a time.
        
        @description Firewalls serve to control network access to simple application servers and isolate security domains in the cloud. By default, SSH port 22, HTTP port 80, and HTTPS port 443 are enabled for simple application servers. Other ports are disabled. You can add firewall rules to enable more ports.
        
        @param request: CreateFirewallRulesRequest
        @return: CreateFirewallRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_firewall_rules_with_options(request, runtime)

    async def create_firewall_rules_async(
        self,
        request: swas__open20200601_models.CreateFirewallRulesRequest,
    ) -> swas__open20200601_models.CreateFirewallRulesResponse:
        """
        @summary Creates multiple firewall rules for a simple application server at a time.
        
        @description Firewalls serve to control network access to simple application servers and isolate security domains in the cloud. By default, SSH port 22, HTTP port 80, and HTTPS port 443 are enabled for simple application servers. Other ports are disabled. You can add firewall rules to enable more ports.
        
        @param request: CreateFirewallRulesRequest
        @return: CreateFirewallRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_firewall_rules_with_options_async(request, runtime)

    def create_firewall_template_with_options(
        self,
        request: swas__open20200601_models.CreateFirewallTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateFirewallTemplateResponse:
        """
        @summary Creates a firewall template.
        
        @description Simple Application Server supports the firewall template feature that provides multiple firewall rules. You can use a template to add a group of firewall rules to one or more simple application servers at a time. This improves the efficiency of setting firewall rules.
        
        @param request: CreateFirewallTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFirewallTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.firewall_rule):
            query['FirewallRule'] = request.firewall_rule
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFirewallTemplate',
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
            swas__open20200601_models.CreateFirewallTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_firewall_template_with_options_async(
        self,
        request: swas__open20200601_models.CreateFirewallTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateFirewallTemplateResponse:
        """
        @summary Creates a firewall template.
        
        @description Simple Application Server supports the firewall template feature that provides multiple firewall rules. You can use a template to add a group of firewall rules to one or more simple application servers at a time. This improves the efficiency of setting firewall rules.
        
        @param request: CreateFirewallTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFirewallTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.firewall_rule):
            query['FirewallRule'] = request.firewall_rule
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFirewallTemplate',
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
            swas__open20200601_models.CreateFirewallTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_firewall_template(
        self,
        request: swas__open20200601_models.CreateFirewallTemplateRequest,
    ) -> swas__open20200601_models.CreateFirewallTemplateResponse:
        """
        @summary Creates a firewall template.
        
        @description Simple Application Server supports the firewall template feature that provides multiple firewall rules. You can use a template to add a group of firewall rules to one or more simple application servers at a time. This improves the efficiency of setting firewall rules.
        
        @param request: CreateFirewallTemplateRequest
        @return: CreateFirewallTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_firewall_template_with_options(request, runtime)

    async def create_firewall_template_async(
        self,
        request: swas__open20200601_models.CreateFirewallTemplateRequest,
    ) -> swas__open20200601_models.CreateFirewallTemplateResponse:
        """
        @summary Creates a firewall template.
        
        @description Simple Application Server supports the firewall template feature that provides multiple firewall rules. You can use a template to add a group of firewall rules to one or more simple application servers at a time. This improves the efficiency of setting firewall rules.
        
        @param request: CreateFirewallTemplateRequest
        @return: CreateFirewallTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_firewall_template_with_options_async(request, runtime)

    def create_firewall_template_rules_with_options(
        self,
        request: swas__open20200601_models.CreateFirewallTemplateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateFirewallTemplateRulesResponse:
        """
        @summary Adds firewall rules to a firewall template based on your business requirements.
        
        @description Adding firewall rules to a firewall template does not affect the firewall rules that have been applied to simple application servers..
        
        @param request: CreateFirewallTemplateRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFirewallTemplateRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_rule):
            query['FirewallRule'] = request.firewall_rule
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFirewallTemplateRules',
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
            swas__open20200601_models.CreateFirewallTemplateRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_firewall_template_rules_with_options_async(
        self,
        request: swas__open20200601_models.CreateFirewallTemplateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateFirewallTemplateRulesResponse:
        """
        @summary Adds firewall rules to a firewall template based on your business requirements.
        
        @description Adding firewall rules to a firewall template does not affect the firewall rules that have been applied to simple application servers..
        
        @param request: CreateFirewallTemplateRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFirewallTemplateRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_rule):
            query['FirewallRule'] = request.firewall_rule
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFirewallTemplateRules',
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
            swas__open20200601_models.CreateFirewallTemplateRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_firewall_template_rules(
        self,
        request: swas__open20200601_models.CreateFirewallTemplateRulesRequest,
    ) -> swas__open20200601_models.CreateFirewallTemplateRulesResponse:
        """
        @summary Adds firewall rules to a firewall template based on your business requirements.
        
        @description Adding firewall rules to a firewall template does not affect the firewall rules that have been applied to simple application servers..
        
        @param request: CreateFirewallTemplateRulesRequest
        @return: CreateFirewallTemplateRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_firewall_template_rules_with_options(request, runtime)

    async def create_firewall_template_rules_async(
        self,
        request: swas__open20200601_models.CreateFirewallTemplateRulesRequest,
    ) -> swas__open20200601_models.CreateFirewallTemplateRulesResponse:
        """
        @summary Adds firewall rules to a firewall template based on your business requirements.
        
        @description Adding firewall rules to a firewall template does not affect the firewall rules that have been applied to simple application servers..
        
        @param request: CreateFirewallTemplateRulesRequest
        @return: CreateFirewallTemplateRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_firewall_template_rules_with_options_async(request, runtime)

    def create_instance_key_pair_with_options(
        self,
        request: swas__open20200601_models.CreateInstanceKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateInstanceKeyPairResponse:
        """
        @summary Creates a key pair for a simple application server.
        
        @param request: CreateInstanceKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceKeyPairResponse
        """
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
        """
        @summary Creates a key pair for a simple application server.
        
        @param request: CreateInstanceKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceKeyPairResponse
        """
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
        """
        @summary Creates a key pair for a simple application server.
        
        @param request: CreateInstanceKeyPairRequest
        @return: CreateInstanceKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_key_pair_with_options(request, runtime)

    async def create_instance_key_pair_async(
        self,
        request: swas__open20200601_models.CreateInstanceKeyPairRequest,
    ) -> swas__open20200601_models.CreateInstanceKeyPairResponse:
        """
        @summary Creates a key pair for a simple application server.
        
        @param request: CreateInstanceKeyPairRequest
        @return: CreateInstanceKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_key_pair_with_options_async(request, runtime)

    def create_instances_with_options(
        self,
        request: swas__open20200601_models.CreateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateInstancesResponse:
        """
        @summary Creates subscription simple application servers.
        
        @description    Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](https://help.aliyun.com/document_detail/58623.html).
        A maximum of 20 simple application servers can be maintained in an Alibaba Cloud account.
        When you call this operation to create simple application servers, make sure that the balance in your account is sufficient to pay for the servers. If the balance in your account is insufficient, the servers cannot be created.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Creates subscription simple application servers.
        
        @description    Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](https://help.aliyun.com/document_detail/58623.html).
        A maximum of 20 simple application servers can be maintained in an Alibaba Cloud account.
        When you call this operation to create simple application servers, make sure that the balance in your account is sufficient to pay for the servers. If the balance in your account is insufficient, the servers cannot be created.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Creates subscription simple application servers.
        
        @description    Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](https://help.aliyun.com/document_detail/58623.html).
        A maximum of 20 simple application servers can be maintained in an Alibaba Cloud account.
        When you call this operation to create simple application servers, make sure that the balance in your account is sufficient to pay for the servers. If the balance in your account is insufficient, the servers cannot be created.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Creates subscription simple application servers.
        
        @description    Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](https://help.aliyun.com/document_detail/58623.html).
        A maximum of 20 simple application servers can be maintained in an Alibaba Cloud account.
        When you call this operation to create simple application servers, make sure that the balance in your account is sufficient to pay for the servers. If the balance in your account is insufficient, the servers cannot be created.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: CreateInstancesRequest
        @return: CreateInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instances_with_options_async(request, runtime)

    def create_key_pair_with_options(
        self,
        request: swas__open20200601_models.CreateKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateKeyPairResponse:
        """
        @summary Creates a key pair.
        
        @description Alibaba Cloud SSH key pairs offer a secure and efficient logon authentication mechanism, facilitating both verification and encrypted communication within the SSH protocol framework. An SSH key pair is essentially constituted by a public key and a private key. Tailored for Linux-based simple application servers, this security measure enhances security and convenience, effectively addressing your heightened security requirements.
        The key pair logon method is only valid for Linux-based simple application servers.
        A maximum of 10 key pairs can be created in a region for an Alibaba Cloud account.
        Only RSA 2048-bit key pairs can be created in the Simple Application Server console.
        
        @param request: CreateKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeyPair',
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
            swas__open20200601_models.CreateKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_key_pair_with_options_async(
        self,
        request: swas__open20200601_models.CreateKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateKeyPairResponse:
        """
        @summary Creates a key pair.
        
        @description Alibaba Cloud SSH key pairs offer a secure and efficient logon authentication mechanism, facilitating both verification and encrypted communication within the SSH protocol framework. An SSH key pair is essentially constituted by a public key and a private key. Tailored for Linux-based simple application servers, this security measure enhances security and convenience, effectively addressing your heightened security requirements.
        The key pair logon method is only valid for Linux-based simple application servers.
        A maximum of 10 key pairs can be created in a region for an Alibaba Cloud account.
        Only RSA 2048-bit key pairs can be created in the Simple Application Server console.
        
        @param request: CreateKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeyPair',
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
            swas__open20200601_models.CreateKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_key_pair(
        self,
        request: swas__open20200601_models.CreateKeyPairRequest,
    ) -> swas__open20200601_models.CreateKeyPairResponse:
        """
        @summary Creates a key pair.
        
        @description Alibaba Cloud SSH key pairs offer a secure and efficient logon authentication mechanism, facilitating both verification and encrypted communication within the SSH protocol framework. An SSH key pair is essentially constituted by a public key and a private key. Tailored for Linux-based simple application servers, this security measure enhances security and convenience, effectively addressing your heightened security requirements.
        The key pair logon method is only valid for Linux-based simple application servers.
        A maximum of 10 key pairs can be created in a region for an Alibaba Cloud account.
        Only RSA 2048-bit key pairs can be created in the Simple Application Server console.
        
        @param request: CreateKeyPairRequest
        @return: CreateKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_key_pair_with_options(request, runtime)

    async def create_key_pair_async(
        self,
        request: swas__open20200601_models.CreateKeyPairRequest,
    ) -> swas__open20200601_models.CreateKeyPairResponse:
        """
        @summary Creates a key pair.
        
        @description Alibaba Cloud SSH key pairs offer a secure and efficient logon authentication mechanism, facilitating both verification and encrypted communication within the SSH protocol framework. An SSH key pair is essentially constituted by a public key and a private key. Tailored for Linux-based simple application servers, this security measure enhances security and convenience, effectively addressing your heightened security requirements.
        The key pair logon method is only valid for Linux-based simple application servers.
        A maximum of 10 key pairs can be created in a region for an Alibaba Cloud account.
        Only RSA 2048-bit key pairs can be created in the Simple Application Server console.
        
        @param request: CreateKeyPairRequest
        @return: CreateKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_key_pair_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: swas__open20200601_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.CreateSnapshotResponse:
        """
        @summary Creates a snapshot for a disk.
        
        @description A snapshot is a point-in-time backup of a disk. Snapshots can be used to back up data, recover data after accidental operations on instances, recover data after network attacks, and create custom images.
        > You are not charged for creating snapshots for disks of simple application servers.
        ### Precautions
        You can create up to three snapshots for disks of each simple application server.
        The maximum number of snapshots that can be retained in an Alibaba Cloud account is triple the number of simple application servers that you maintain. The value cannot be greater than 15.
        If a simple application server is automatically released due to expiration, the snapshots created for the server are deleted.
        If you reset the simple application server after you create a snapshot for a server, the snapshot is retained but cannot be used to roll back the disks of the server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        @summary Creates a snapshot for a disk.
        
        @description A snapshot is a point-in-time backup of a disk. Snapshots can be used to back up data, recover data after accidental operations on instances, recover data after network attacks, and create custom images.
        > You are not charged for creating snapshots for disks of simple application servers.
        ### Precautions
        You can create up to three snapshots for disks of each simple application server.
        The maximum number of snapshots that can be retained in an Alibaba Cloud account is triple the number of simple application servers that you maintain. The value cannot be greater than 15.
        If a simple application server is automatically released due to expiration, the snapshots created for the server are deleted.
        If you reset the simple application server after you create a snapshot for a server, the snapshot is retained but cannot be used to roll back the disks of the server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        @summary Creates a snapshot for a disk.
        
        @description A snapshot is a point-in-time backup of a disk. Snapshots can be used to back up data, recover data after accidental operations on instances, recover data after network attacks, and create custom images.
        > You are not charged for creating snapshots for disks of simple application servers.
        ### Precautions
        You can create up to three snapshots for disks of each simple application server.
        The maximum number of snapshots that can be retained in an Alibaba Cloud account is triple the number of simple application servers that you maintain. The value cannot be greater than 15.
        If a simple application server is automatically released due to expiration, the snapshots created for the server are deleted.
        If you reset the simple application server after you create a snapshot for a server, the snapshot is retained but cannot be used to roll back the disks of the server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Creates a snapshot for a disk.
        
        @description A snapshot is a point-in-time backup of a disk. Snapshots can be used to back up data, recover data after accidental operations on instances, recover data after network attacks, and create custom images.
        > You are not charged for creating snapshots for disks of simple application servers.
        ### Precautions
        You can create up to three snapshots for disks of each simple application server.
        The maximum number of snapshots that can be retained in an Alibaba Cloud account is triple the number of simple application servers that you maintain. The value cannot be greater than 15.
        If a simple application server is automatically released due to expiration, the snapshots created for the server are deleted.
        If you reset the simple application server after you create a snapshot for a server, the snapshot is retained but cannot be used to roll back the disks of the server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: CreateSnapshotRequest
        @return: CreateSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def delete_command_with_options(
        self,
        request: swas__open20200601_models.DeleteCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteCommandResponse:
        """
        @summary Deletes a Command Assistant command.
        
        @description You cannot delete commands that are being run.
        
        @param request: DeleteCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCommand',
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
            swas__open20200601_models.DeleteCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_command_with_options_async(
        self,
        request: swas__open20200601_models.DeleteCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteCommandResponse:
        """
        @summary Deletes a Command Assistant command.
        
        @description You cannot delete commands that are being run.
        
        @param request: DeleteCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCommandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCommand',
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
            swas__open20200601_models.DeleteCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_command(
        self,
        request: swas__open20200601_models.DeleteCommandRequest,
    ) -> swas__open20200601_models.DeleteCommandResponse:
        """
        @summary Deletes a Command Assistant command.
        
        @description You cannot delete commands that are being run.
        
        @param request: DeleteCommandRequest
        @return: DeleteCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_command_with_options(request, runtime)

    async def delete_command_async(
        self,
        request: swas__open20200601_models.DeleteCommandRequest,
    ) -> swas__open20200601_models.DeleteCommandResponse:
        """
        @summary Deletes a Command Assistant command.
        
        @description You cannot delete commands that are being run.
        
        @param request: DeleteCommandRequest
        @return: DeleteCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_command_with_options_async(request, runtime)

    def delete_custom_image_with_options(
        self,
        request: swas__open20200601_models.DeleteCustomImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteCustomImageResponse:
        """
        @summary Deletes a custom image.
        
        @description You can delete a custom image that you no longer need. After the custom image is deleted, you cannot use the custom image to reset the simple application servers that were created based on the custom image.
        > If a custom image is shared to Elastic Compute Service (ECS), you must unshare the image before you can delete it. After you unshare the custom image, you cannot query the custom image by using the ECS console or by calling ECS API operations. If you need to use the custom image in ECS, we recommend that you copy the image before you delete it. For more information, see [Copy a shared image of a simple application server in the ECS console](https://help.aliyun.com/document_detail/199378.html).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Deletes a custom image.
        
        @description You can delete a custom image that you no longer need. After the custom image is deleted, you cannot use the custom image to reset the simple application servers that were created based on the custom image.
        > If a custom image is shared to Elastic Compute Service (ECS), you must unshare the image before you can delete it. After you unshare the custom image, you cannot query the custom image by using the ECS console or by calling ECS API operations. If you need to use the custom image in ECS, we recommend that you copy the image before you delete it. For more information, see [Copy a shared image of a simple application server in the ECS console](https://help.aliyun.com/document_detail/199378.html).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Deletes a custom image.
        
        @description You can delete a custom image that you no longer need. After the custom image is deleted, you cannot use the custom image to reset the simple application servers that were created based on the custom image.
        > If a custom image is shared to Elastic Compute Service (ECS), you must unshare the image before you can delete it. After you unshare the custom image, you cannot query the custom image by using the ECS console or by calling ECS API operations. If you need to use the custom image in ECS, we recommend that you copy the image before you delete it. For more information, see [Copy a shared image of a simple application server in the ECS console](https://help.aliyun.com/document_detail/199378.html).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Deletes a custom image.
        
        @description You can delete a custom image that you no longer need. After the custom image is deleted, you cannot use the custom image to reset the simple application servers that were created based on the custom image.
        > If a custom image is shared to Elastic Compute Service (ECS), you must unshare the image before you can delete it. After you unshare the custom image, you cannot query the custom image by using the ECS console or by calling ECS API operations. If you need to use the custom image in ECS, we recommend that you copy the image before you delete it. For more information, see [Copy a shared image of a simple application server in the ECS console](https://help.aliyun.com/document_detail/199378.html).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DeleteCustomImageRequest
        @return: DeleteCustomImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_image_with_options_async(request, runtime)

    def delete_custom_images_with_options(
        self,
        request: swas__open20200601_models.DeleteCustomImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteCustomImagesResponse:
        """
        @summary Deletes custom images. If you no longer require a custom image, you can call this operation to delete the custom image. You can also call this operation to delete multiple custom images at the same time. After a custom image is deleted, you cannot use the custom image to reset the simple application servers that were created based on the custom image.
        
        @description If a custom image is shared, you must unshare the image before you can delete it. After a custom image is unshared, you cannot query the custom image by using the Elastic Compute Service (ECS) console or by calling an ECS API operation. If you want to use a custom image to create ECS instances, we recommend that you copy the custom image before you delete it. For more information, see the "Copy custom images" topic.
        
        @param request: DeleteCustomImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomImages',
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
            swas__open20200601_models.DeleteCustomImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_images_with_options_async(
        self,
        request: swas__open20200601_models.DeleteCustomImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteCustomImagesResponse:
        """
        @summary Deletes custom images. If you no longer require a custom image, you can call this operation to delete the custom image. You can also call this operation to delete multiple custom images at the same time. After a custom image is deleted, you cannot use the custom image to reset the simple application servers that were created based on the custom image.
        
        @description If a custom image is shared, you must unshare the image before you can delete it. After a custom image is unshared, you cannot query the custom image by using the Elastic Compute Service (ECS) console or by calling an ECS API operation. If you want to use a custom image to create ECS instances, we recommend that you copy the custom image before you delete it. For more information, see the "Copy custom images" topic.
        
        @param request: DeleteCustomImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_ids):
            query['ImageIds'] = request.image_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomImages',
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
            swas__open20200601_models.DeleteCustomImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_images(
        self,
        request: swas__open20200601_models.DeleteCustomImagesRequest,
    ) -> swas__open20200601_models.DeleteCustomImagesResponse:
        """
        @summary Deletes custom images. If you no longer require a custom image, you can call this operation to delete the custom image. You can also call this operation to delete multiple custom images at the same time. After a custom image is deleted, you cannot use the custom image to reset the simple application servers that were created based on the custom image.
        
        @description If a custom image is shared, you must unshare the image before you can delete it. After a custom image is unshared, you cannot query the custom image by using the Elastic Compute Service (ECS) console or by calling an ECS API operation. If you want to use a custom image to create ECS instances, we recommend that you copy the custom image before you delete it. For more information, see the "Copy custom images" topic.
        
        @param request: DeleteCustomImagesRequest
        @return: DeleteCustomImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_images_with_options(request, runtime)

    async def delete_custom_images_async(
        self,
        request: swas__open20200601_models.DeleteCustomImagesRequest,
    ) -> swas__open20200601_models.DeleteCustomImagesResponse:
        """
        @summary Deletes custom images. If you no longer require a custom image, you can call this operation to delete the custom image. You can also call this operation to delete multiple custom images at the same time. After a custom image is deleted, you cannot use the custom image to reset the simple application servers that were created based on the custom image.
        
        @description If a custom image is shared, you must unshare the image before you can delete it. After a custom image is unshared, you cannot query the custom image by using the Elastic Compute Service (ECS) console or by calling an ECS API operation. If you want to use a custom image to create ECS instances, we recommend that you copy the custom image before you delete it. For more information, see the "Copy custom images" topic.
        
        @param request: DeleteCustomImagesRequest
        @return: DeleteCustomImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_images_with_options_async(request, runtime)

    def delete_firewall_rule_with_options(
        self,
        request: swas__open20200601_models.DeleteFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteFirewallRuleResponse:
        """
        @summary Deletes a firewall rule of a simple application server.
        
        @description After a firewall rule is deleted, your business deployed on the simple application server may become inaccessible. Before you delete a firewall rule, make sure that the firewall rule is no longer needed by the simple application server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Deletes a firewall rule of a simple application server.
        
        @description After a firewall rule is deleted, your business deployed on the simple application server may become inaccessible. Before you delete a firewall rule, make sure that the firewall rule is no longer needed by the simple application server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Deletes a firewall rule of a simple application server.
        
        @description After a firewall rule is deleted, your business deployed on the simple application server may become inaccessible. Before you delete a firewall rule, make sure that the firewall rule is no longer needed by the simple application server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Deletes a firewall rule of a simple application server.
        
        @description After a firewall rule is deleted, your business deployed on the simple application server may become inaccessible. Before you delete a firewall rule, make sure that the firewall rule is no longer needed by the simple application server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DeleteFirewallRuleRequest
        @return: DeleteFirewallRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_firewall_rule_with_options_async(request, runtime)

    def delete_firewall_rules_with_options(
        self,
        tmp_req: swas__open20200601_models.DeleteFirewallRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteFirewallRulesResponse:
        """
        @summary Deletes multiple firewall rules of a simple application server.
        
        @description After a firewall rule is deleted, your business deployed on the simple application server may become inaccessible. Before you delete a firewall rule, make sure that the firewall rule is no longer needed by the simple application server.
        
        @param tmp_req: DeleteFirewallRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFirewallRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.DeleteFirewallRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rule_ids):
            request.rule_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rule_ids, 'RuleIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_ids_shrink):
            query['RuleIds'] = request.rule_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFirewallRules',
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
            swas__open20200601_models.DeleteFirewallRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_firewall_rules_with_options_async(
        self,
        tmp_req: swas__open20200601_models.DeleteFirewallRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteFirewallRulesResponse:
        """
        @summary Deletes multiple firewall rules of a simple application server.
        
        @description After a firewall rule is deleted, your business deployed on the simple application server may become inaccessible. Before you delete a firewall rule, make sure that the firewall rule is no longer needed by the simple application server.
        
        @param tmp_req: DeleteFirewallRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFirewallRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.DeleteFirewallRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rule_ids):
            request.rule_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rule_ids, 'RuleIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_ids_shrink):
            query['RuleIds'] = request.rule_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFirewallRules',
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
            swas__open20200601_models.DeleteFirewallRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_firewall_rules(
        self,
        request: swas__open20200601_models.DeleteFirewallRulesRequest,
    ) -> swas__open20200601_models.DeleteFirewallRulesResponse:
        """
        @summary Deletes multiple firewall rules of a simple application server.
        
        @description After a firewall rule is deleted, your business deployed on the simple application server may become inaccessible. Before you delete a firewall rule, make sure that the firewall rule is no longer needed by the simple application server.
        
        @param request: DeleteFirewallRulesRequest
        @return: DeleteFirewallRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_firewall_rules_with_options(request, runtime)

    async def delete_firewall_rules_async(
        self,
        request: swas__open20200601_models.DeleteFirewallRulesRequest,
    ) -> swas__open20200601_models.DeleteFirewallRulesResponse:
        """
        @summary Deletes multiple firewall rules of a simple application server.
        
        @description After a firewall rule is deleted, your business deployed on the simple application server may become inaccessible. Before you delete a firewall rule, make sure that the firewall rule is no longer needed by the simple application server.
        
        @param request: DeleteFirewallRulesRequest
        @return: DeleteFirewallRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_firewall_rules_with_options_async(request, runtime)

    def delete_firewall_template_rules_with_options(
        self,
        request: swas__open20200601_models.DeleteFirewallTemplateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteFirewallTemplateRulesResponse:
        """
        @summary Deletes firewall rules from a firewall template based on your requirements.
        
        @description Deletion of firewall rules does not affect the firewall rules that have been applied to simple application servers.
        
        @param request: DeleteFirewallTemplateRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFirewallTemplateRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.firewall_template_rule_id):
            query['FirewallTemplateRuleId'] = request.firewall_template_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFirewallTemplateRules',
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
            swas__open20200601_models.DeleteFirewallTemplateRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_firewall_template_rules_with_options_async(
        self,
        request: swas__open20200601_models.DeleteFirewallTemplateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteFirewallTemplateRulesResponse:
        """
        @summary Deletes firewall rules from a firewall template based on your requirements.
        
        @description Deletion of firewall rules does not affect the firewall rules that have been applied to simple application servers.
        
        @param request: DeleteFirewallTemplateRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFirewallTemplateRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.firewall_template_rule_id):
            query['FirewallTemplateRuleId'] = request.firewall_template_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFirewallTemplateRules',
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
            swas__open20200601_models.DeleteFirewallTemplateRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_firewall_template_rules(
        self,
        request: swas__open20200601_models.DeleteFirewallTemplateRulesRequest,
    ) -> swas__open20200601_models.DeleteFirewallTemplateRulesResponse:
        """
        @summary Deletes firewall rules from a firewall template based on your requirements.
        
        @description Deletion of firewall rules does not affect the firewall rules that have been applied to simple application servers.
        
        @param request: DeleteFirewallTemplateRulesRequest
        @return: DeleteFirewallTemplateRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_firewall_template_rules_with_options(request, runtime)

    async def delete_firewall_template_rules_async(
        self,
        request: swas__open20200601_models.DeleteFirewallTemplateRulesRequest,
    ) -> swas__open20200601_models.DeleteFirewallTemplateRulesResponse:
        """
        @summary Deletes firewall rules from a firewall template based on your requirements.
        
        @description Deletion of firewall rules does not affect the firewall rules that have been applied to simple application servers.
        
        @param request: DeleteFirewallTemplateRulesRequest
        @return: DeleteFirewallTemplateRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_firewall_template_rules_with_options_async(request, runtime)

    def delete_firewall_templates_with_options(
        self,
        request: swas__open20200601_models.DeleteFirewallTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteFirewallTemplatesResponse:
        """
        @summary Deletes firewall templates from a simple application server.
        
        @description Deleting a firewall template does not affect the firewall rules that have been applied to simple application servers. You can delete firewall templates that you no longer need.
        
        @param request: DeleteFirewallTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFirewallTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFirewallTemplates',
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
            swas__open20200601_models.DeleteFirewallTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_firewall_templates_with_options_async(
        self,
        request: swas__open20200601_models.DeleteFirewallTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteFirewallTemplatesResponse:
        """
        @summary Deletes firewall templates from a simple application server.
        
        @description Deleting a firewall template does not affect the firewall rules that have been applied to simple application servers. You can delete firewall templates that you no longer need.
        
        @param request: DeleteFirewallTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFirewallTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFirewallTemplates',
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
            swas__open20200601_models.DeleteFirewallTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_firewall_templates(
        self,
        request: swas__open20200601_models.DeleteFirewallTemplatesRequest,
    ) -> swas__open20200601_models.DeleteFirewallTemplatesResponse:
        """
        @summary Deletes firewall templates from a simple application server.
        
        @description Deleting a firewall template does not affect the firewall rules that have been applied to simple application servers. You can delete firewall templates that you no longer need.
        
        @param request: DeleteFirewallTemplatesRequest
        @return: DeleteFirewallTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_firewall_templates_with_options(request, runtime)

    async def delete_firewall_templates_async(
        self,
        request: swas__open20200601_models.DeleteFirewallTemplatesRequest,
    ) -> swas__open20200601_models.DeleteFirewallTemplatesResponse:
        """
        @summary Deletes firewall templates from a simple application server.
        
        @description Deleting a firewall template does not affect the firewall rules that have been applied to simple application servers. You can delete firewall templates that you no longer need.
        
        @param request: DeleteFirewallTemplatesRequest
        @return: DeleteFirewallTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_firewall_templates_with_options_async(request, runtime)

    def delete_instance_key_pair_with_options(
        self,
        request: swas__open20200601_models.DeleteInstanceKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteInstanceKeyPairResponse:
        """
        @summary Deletes the key pair of a simple application server.
        
        @param request: DeleteInstanceKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceKeyPairResponse
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
        """
        @summary Deletes the key pair of a simple application server.
        
        @param request: DeleteInstanceKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceKeyPairResponse
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
        """
        @summary Deletes the key pair of a simple application server.
        
        @param request: DeleteInstanceKeyPairRequest
        @return: DeleteInstanceKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_key_pair_with_options(request, runtime)

    async def delete_instance_key_pair_async(
        self,
        request: swas__open20200601_models.DeleteInstanceKeyPairRequest,
    ) -> swas__open20200601_models.DeleteInstanceKeyPairResponse:
        """
        @summary Deletes the key pair of a simple application server.
        
        @param request: DeleteInstanceKeyPairRequest
        @return: DeleteInstanceKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_key_pair_with_options_async(request, runtime)

    def delete_key_pairs_with_options(
        self,
        request: swas__open20200601_models.DeleteKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteKeyPairsResponse:
        """
        @summary Deletes the SSH key pairs of simple application servers.
        
        @description You must unbind SSH key pairs that you no longer use from simple application servers before you delete the SSH key pairs.
        
        @param request: DeleteKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.key_pair_names):
            query['KeyPairNames'] = request.key_pair_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyPairs',
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
            swas__open20200601_models.DeleteKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_key_pairs_with_options_async(
        self,
        request: swas__open20200601_models.DeleteKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteKeyPairsResponse:
        """
        @summary Deletes the SSH key pairs of simple application servers.
        
        @description You must unbind SSH key pairs that you no longer use from simple application servers before you delete the SSH key pairs.
        
        @param request: DeleteKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.key_pair_names):
            query['KeyPairNames'] = request.key_pair_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyPairs',
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
            swas__open20200601_models.DeleteKeyPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_key_pairs(
        self,
        request: swas__open20200601_models.DeleteKeyPairsRequest,
    ) -> swas__open20200601_models.DeleteKeyPairsResponse:
        """
        @summary Deletes the SSH key pairs of simple application servers.
        
        @description You must unbind SSH key pairs that you no longer use from simple application servers before you delete the SSH key pairs.
        
        @param request: DeleteKeyPairsRequest
        @return: DeleteKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_key_pairs_with_options(request, runtime)

    async def delete_key_pairs_async(
        self,
        request: swas__open20200601_models.DeleteKeyPairsRequest,
    ) -> swas__open20200601_models.DeleteKeyPairsResponse:
        """
        @summary Deletes the SSH key pairs of simple application servers.
        
        @description You must unbind SSH key pairs that you no longer use from simple application servers before you delete the SSH key pairs.
        
        @param request: DeleteKeyPairsRequest
        @return: DeleteKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_key_pairs_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: swas__open20200601_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DeleteSnapshotResponse:
        """
        @summary Deletes a snapshot of a simple application server.
        
        @description You can delete a snapshot if you no longer need it.
        > If a custom image was created based on the snapshot, delete the custom image before you delete the snapshot.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Deletes a snapshot of a simple application server.
        
        @description You can delete a snapshot if you no longer need it.
        > If a custom image was created based on the snapshot, delete the custom image before you delete the snapshot.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Deletes a snapshot of a simple application server.
        
        @description You can delete a snapshot if you no longer need it.
        > If a custom image was created based on the snapshot, delete the custom image before you delete the snapshot.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Deletes a snapshot of a simple application server.
        
        @description You can delete a snapshot if you no longer need it.
        > If a custom image was created based on the snapshot, delete the custom image before you delete the snapshot.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        """
        @summary Deletes snapshots of a simple application server.
        
        @param request: DeleteSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSnapshotsResponse
        """
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
        """
        @summary Deletes snapshots of a simple application server.
        
        @param request: DeleteSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSnapshotsResponse
        """
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
        """
        @summary Deletes snapshots of a simple application server.
        
        @param request: DeleteSnapshotsRequest
        @return: DeleteSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshots_with_options(request, runtime)

    async def delete_snapshots_async(
        self,
        request: swas__open20200601_models.DeleteSnapshotsRequest,
    ) -> swas__open20200601_models.DeleteSnapshotsResponse:
        """
        @summary Deletes snapshots of a simple application server.
        
        @param request: DeleteSnapshotsRequest
        @return: DeleteSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshots_with_options_async(request, runtime)

    def describe_cloud_assistant_attributes_with_options(
        self,
        tmp_req: swas__open20200601_models.DescribeCloudAssistantAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCloudAssistantAttributesResponse:
        """
        @summary Queries the Command Assistant information of simple application servers.
        
        @param tmp_req: DescribeCloudAssistantAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudAssistantAttributesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.DescribeCloudAssistantAttributesShrinkRequest()
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
            action='DescribeCloudAssistantAttributes',
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
            swas__open20200601_models.DescribeCloudAssistantAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_assistant_attributes_with_options_async(
        self,
        tmp_req: swas__open20200601_models.DescribeCloudAssistantAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCloudAssistantAttributesResponse:
        """
        @summary Queries the Command Assistant information of simple application servers.
        
        @param tmp_req: DescribeCloudAssistantAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudAssistantAttributesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.DescribeCloudAssistantAttributesShrinkRequest()
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
            action='DescribeCloudAssistantAttributes',
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
            swas__open20200601_models.DescribeCloudAssistantAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_assistant_attributes(
        self,
        request: swas__open20200601_models.DescribeCloudAssistantAttributesRequest,
    ) -> swas__open20200601_models.DescribeCloudAssistantAttributesResponse:
        """
        @summary Queries the Command Assistant information of simple application servers.
        
        @param request: DescribeCloudAssistantAttributesRequest
        @return: DescribeCloudAssistantAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_assistant_attributes_with_options(request, runtime)

    async def describe_cloud_assistant_attributes_async(
        self,
        request: swas__open20200601_models.DescribeCloudAssistantAttributesRequest,
    ) -> swas__open20200601_models.DescribeCloudAssistantAttributesResponse:
        """
        @summary Queries the Command Assistant information of simple application servers.
        
        @param request: DescribeCloudAssistantAttributesRequest
        @return: DescribeCloudAssistantAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_assistant_attributes_with_options_async(request, runtime)

    def describe_cloud_assistant_status_with_options(
        self,
        tmp_req: swas__open20200601_models.DescribeCloudAssistantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCloudAssistantStatusResponse:
        """
        @summary Queries whether the Cloud Assistant client is installed on simple application servers.
        
        @description By default, the Cloud Assistant client is installed on simple application servers. If you have manually uninstalled the client, you must reinstall the client. Otherwise, you cannot run commands on the servers.
        
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
        @summary Queries whether the Cloud Assistant client is installed on simple application servers.
        
        @description By default, the Cloud Assistant client is installed on simple application servers. If you have manually uninstalled the client, you must reinstall the client. Otherwise, you cannot run commands on the servers.
        
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
        @summary Queries whether the Cloud Assistant client is installed on simple application servers.
        
        @description By default, the Cloud Assistant client is installed on simple application servers. If you have manually uninstalled the client, you must reinstall the client. Otherwise, you cannot run commands on the servers.
        
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
        @summary Queries whether the Cloud Assistant client is installed on simple application servers.
        
        @description By default, the Cloud Assistant client is installed on simple application servers. If you have manually uninstalled the client, you must reinstall the client. Otherwise, you cannot run commands on the servers.
        
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
        """
        @summary Queries the status of the CloudMonitor agent on simple application servers.
        
        @param request: DescribeCloudMonitorAgentStatusesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudMonitorAgentStatusesResponse
        """
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
        """
        @summary Queries the status of the CloudMonitor agent on simple application servers.
        
        @param request: DescribeCloudMonitorAgentStatusesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudMonitorAgentStatusesResponse
        """
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
        """
        @summary Queries the status of the CloudMonitor agent on simple application servers.
        
        @param request: DescribeCloudMonitorAgentStatusesRequest
        @return: DescribeCloudMonitorAgentStatusesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_monitor_agent_statuses_with_options(request, runtime)

    async def describe_cloud_monitor_agent_statuses_async(
        self,
        request: swas__open20200601_models.DescribeCloudMonitorAgentStatusesRequest,
    ) -> swas__open20200601_models.DescribeCloudMonitorAgentStatusesResponse:
        """
        @summary Queries the status of the CloudMonitor agent on simple application servers.
        
        @param request: DescribeCloudMonitorAgentStatusesRequest
        @return: DescribeCloudMonitorAgentStatusesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_monitor_agent_statuses_with_options_async(request, runtime)

    def describe_command_invocations_with_options(
        self,
        request: swas__open20200601_models.DescribeCommandInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCommandInvocationsResponse:
        """
        @summary Queries the executions and execution status of a Cloud Assistant command.
        
        @param request: DescribeCommandInvocationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCommandInvocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.command_name):
            query['CommandName'] = request.command_name
        if not UtilClient.is_unset(request.command_type):
            query['CommandType'] = request.command_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invocation_status):
            query['InvocationStatus'] = request.invocation_status
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
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
            action='DescribeCommandInvocations',
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
            swas__open20200601_models.DescribeCommandInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_command_invocations_with_options_async(
        self,
        request: swas__open20200601_models.DescribeCommandInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCommandInvocationsResponse:
        """
        @summary Queries the executions and execution status of a Cloud Assistant command.
        
        @param request: DescribeCommandInvocationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCommandInvocationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.command_name):
            query['CommandName'] = request.command_name
        if not UtilClient.is_unset(request.command_type):
            query['CommandType'] = request.command_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.invocation_status):
            query['InvocationStatus'] = request.invocation_status
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
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
            action='DescribeCommandInvocations',
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
            swas__open20200601_models.DescribeCommandInvocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_command_invocations(
        self,
        request: swas__open20200601_models.DescribeCommandInvocationsRequest,
    ) -> swas__open20200601_models.DescribeCommandInvocationsResponse:
        """
        @summary Queries the executions and execution status of a Cloud Assistant command.
        
        @param request: DescribeCommandInvocationsRequest
        @return: DescribeCommandInvocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_command_invocations_with_options(request, runtime)

    async def describe_command_invocations_async(
        self,
        request: swas__open20200601_models.DescribeCommandInvocationsRequest,
    ) -> swas__open20200601_models.DescribeCommandInvocationsResponse:
        """
        @summary Queries the executions and execution status of a Cloud Assistant command.
        
        @param request: DescribeCommandInvocationsRequest
        @return: DescribeCommandInvocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_command_invocations_with_options_async(request, runtime)

    def describe_commands_with_options(
        self,
        request: swas__open20200601_models.DescribeCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCommandsResponse:
        """
        @summary Queries the commands that you created or the common commands that Alibaba Cloud provides.
        
        @param request: DescribeCommandsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCommandsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommands',
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
            swas__open20200601_models.DescribeCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_commands_with_options_async(
        self,
        request: swas__open20200601_models.DescribeCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeCommandsResponse:
        """
        @summary Queries the commands that you created or the common commands that Alibaba Cloud provides.
        
        @param request: DescribeCommandsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCommandsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCommands',
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
            swas__open20200601_models.DescribeCommandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_commands(
        self,
        request: swas__open20200601_models.DescribeCommandsRequest,
    ) -> swas__open20200601_models.DescribeCommandsResponse:
        """
        @summary Queries the commands that you created or the common commands that Alibaba Cloud provides.
        
        @param request: DescribeCommandsRequest
        @return: DescribeCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_commands_with_options(request, runtime)

    async def describe_commands_async(
        self,
        request: swas__open20200601_models.DescribeCommandsRequest,
    ) -> swas__open20200601_models.DescribeCommandsResponse:
        """
        @summary Queries the commands that you created or the common commands that Alibaba Cloud provides.
        
        @param request: DescribeCommandsRequest
        @return: DescribeCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_commands_with_options_async(request, runtime)

    def describe_database_error_logs_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseErrorLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseErrorLogsResponse:
        """
        @summary Queries error logs of databases in a Simple Database Service instance.
        
        @description You can call this operation to query the error logs of databases in a Simple Database Service instance and locate faults based on the error logs.
        \\### QPS limit You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseErrorLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabaseErrorLogsResponse
        """
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
        """
        @summary Queries error logs of databases in a Simple Database Service instance.
        
        @description You can call this operation to query the error logs of databases in a Simple Database Service instance and locate faults based on the error logs.
        \\### QPS limit You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseErrorLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabaseErrorLogsResponse
        """
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
        """
        @summary Queries error logs of databases in a Simple Database Service instance.
        
        @description You can call this operation to query the error logs of databases in a Simple Database Service instance and locate faults based on the error logs.
        \\### QPS limit You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseErrorLogsRequest
        @return: DescribeDatabaseErrorLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_database_error_logs_with_options(request, runtime)

    async def describe_database_error_logs_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseErrorLogsRequest,
    ) -> swas__open20200601_models.DescribeDatabaseErrorLogsResponse:
        """
        @summary Queries error logs of databases in a Simple Database Service instance.
        
        @description You can call this operation to query the error logs of databases in a Simple Database Service instance and locate faults based on the error logs.
        \\### QPS limit You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseErrorLogsRequest
        @return: DescribeDatabaseErrorLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_error_logs_with_options_async(request, runtime)

    def describe_database_instance_metric_data_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse:
        """
        @summary Queries the monitoring information about a Simple Database Service instance.
        
        @description After you create a Simple Database Service instance, you can query the details about the vCPU, memory, disk size, storage IOPS (input/output operations per second), and total current connection number of the instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseInstanceMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabaseInstanceMetricDataResponse
        """
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
        """
        @summary Queries the monitoring information about a Simple Database Service instance.
        
        @description After you create a Simple Database Service instance, you can query the details about the vCPU, memory, disk size, storage IOPS (input/output operations per second), and total current connection number of the instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseInstanceMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabaseInstanceMetricDataResponse
        """
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
        """
        @summary Queries the monitoring information about a Simple Database Service instance.
        
        @description After you create a Simple Database Service instance, you can query the details about the vCPU, memory, disk size, storage IOPS (input/output operations per second), and total current connection number of the instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseInstanceMetricDataRequest
        @return: DescribeDatabaseInstanceMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_database_instance_metric_data_with_options(request, runtime)

    async def describe_database_instance_metric_data_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceMetricDataRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceMetricDataResponse:
        """
        @summary Queries the monitoring information about a Simple Database Service instance.
        
        @description After you create a Simple Database Service instance, you can query the details about the vCPU, memory, disk size, storage IOPS (input/output operations per second), and total current connection number of the instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseInstanceMetricDataRequest
        @return: DescribeDatabaseInstanceMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_instance_metric_data_with_options_async(request, runtime)

    def describe_database_instance_parameters_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceParametersResponse:
        """
        @summary Queries the parameters of a Simple Database Service instance.
        
        @description You can call this operation to query the information about parameters of a Simple Database Service instance.
        
        @param request: DescribeDatabaseInstanceParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabaseInstanceParametersResponse
        """
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
        """
        @summary Queries the parameters of a Simple Database Service instance.
        
        @description You can call this operation to query the information about parameters of a Simple Database Service instance.
        
        @param request: DescribeDatabaseInstanceParametersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabaseInstanceParametersResponse
        """
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
        """
        @summary Queries the parameters of a Simple Database Service instance.
        
        @description You can call this operation to query the information about parameters of a Simple Database Service instance.
        
        @param request: DescribeDatabaseInstanceParametersRequest
        @return: DescribeDatabaseInstanceParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_database_instance_parameters_with_options(request, runtime)

    async def describe_database_instance_parameters_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstanceParametersRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstanceParametersResponse:
        """
        @summary Queries the parameters of a Simple Database Service instance.
        
        @description You can call this operation to query the information about parameters of a Simple Database Service instance.
        
        @param request: DescribeDatabaseInstanceParametersRequest
        @return: DescribeDatabaseInstanceParametersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_instance_parameters_with_options_async(request, runtime)

    def describe_database_instances_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseInstancesResponse:
        """
        @summary Queries the information about Simple Database Service instances.
        
        @description You can call this operation to query the details of Simple Database Service instances in a region, including the IDs, names, plans, database versions, public endpoint, internal endpoint, creation time, and expiration time of the instances.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabaseInstancesResponse
        """
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
        """
        @summary Queries the information about Simple Database Service instances.
        
        @description You can call this operation to query the details of Simple Database Service instances in a region, including the IDs, names, plans, database versions, public endpoint, internal endpoint, creation time, and expiration time of the instances.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabaseInstancesResponse
        """
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
        """
        @summary Queries the information about Simple Database Service instances.
        
        @description You can call this operation to query the details of Simple Database Service instances in a region, including the IDs, names, plans, database versions, public endpoint, internal endpoint, creation time, and expiration time of the instances.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseInstancesRequest
        @return: DescribeDatabaseInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_database_instances_with_options(request, runtime)

    async def describe_database_instances_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseInstancesRequest,
    ) -> swas__open20200601_models.DescribeDatabaseInstancesResponse:
        """
        @summary Queries the information about Simple Database Service instances.
        
        @description You can call this operation to query the details of Simple Database Service instances in a region, including the IDs, names, plans, database versions, public endpoint, internal endpoint, creation time, and expiration time of the instances.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseInstancesRequest
        @return: DescribeDatabaseInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_instances_with_options_async(request, runtime)

    def describe_database_slow_log_records_with_options(
        self,
        request: swas__open20200601_models.DescribeDatabaseSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse:
        """
        @summary Queries the slow query log details of a Simple Database Service instance.
        
        @description You can query the slow query log details of a Simple Database Service instance and locate faults based on the log details.
        > Slow query log details are retained for 7 days.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabaseSlowLogRecordsResponse
        """
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
        """
        @summary Queries the slow query log details of a Simple Database Service instance.
        
        @description You can query the slow query log details of a Simple Database Service instance and locate faults based on the log details.
        > Slow query log details are retained for 7 days.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDatabaseSlowLogRecordsResponse
        """
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
        """
        @summary Queries the slow query log details of a Simple Database Service instance.
        
        @description You can query the slow query log details of a Simple Database Service instance and locate faults based on the log details.
        > Slow query log details are retained for 7 days.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseSlowLogRecordsRequest
        @return: DescribeDatabaseSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_database_slow_log_records_with_options(request, runtime)

    async def describe_database_slow_log_records_async(
        self,
        request: swas__open20200601_models.DescribeDatabaseSlowLogRecordsRequest,
    ) -> swas__open20200601_models.DescribeDatabaseSlowLogRecordsResponse:
        """
        @summary Queries the slow query log details of a Simple Database Service instance.
        
        @description You can query the slow query log details of a Simple Database Service instance and locate faults based on the log details.
        > Slow query log details are retained for 7 days.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: DescribeDatabaseSlowLogRecordsRequest
        @return: DescribeDatabaseSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_database_slow_log_records_with_options_async(request, runtime)

    def describe_firewall_template_apply_results_with_options(
        self,
        request: swas__open20200601_models.DescribeFirewallTemplateApplyResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeFirewallTemplateApplyResultsResponse:
        """
        @summary Queries the result of applying a firewall template to simple application servers.
        
        @param request: DescribeFirewallTemplateApplyResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFirewallTemplateApplyResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFirewallTemplateApplyResults',
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
            swas__open20200601_models.DescribeFirewallTemplateApplyResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_firewall_template_apply_results_with_options_async(
        self,
        request: swas__open20200601_models.DescribeFirewallTemplateApplyResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeFirewallTemplateApplyResultsResponse:
        """
        @summary Queries the result of applying a firewall template to simple application servers.
        
        @param request: DescribeFirewallTemplateApplyResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFirewallTemplateApplyResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFirewallTemplateApplyResults',
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
            swas__open20200601_models.DescribeFirewallTemplateApplyResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_firewall_template_apply_results(
        self,
        request: swas__open20200601_models.DescribeFirewallTemplateApplyResultsRequest,
    ) -> swas__open20200601_models.DescribeFirewallTemplateApplyResultsResponse:
        """
        @summary Queries the result of applying a firewall template to simple application servers.
        
        @param request: DescribeFirewallTemplateApplyResultsRequest
        @return: DescribeFirewallTemplateApplyResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_firewall_template_apply_results_with_options(request, runtime)

    async def describe_firewall_template_apply_results_async(
        self,
        request: swas__open20200601_models.DescribeFirewallTemplateApplyResultsRequest,
    ) -> swas__open20200601_models.DescribeFirewallTemplateApplyResultsResponse:
        """
        @summary Queries the result of applying a firewall template to simple application servers.
        
        @param request: DescribeFirewallTemplateApplyResultsRequest
        @return: DescribeFirewallTemplateApplyResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_firewall_template_apply_results_with_options_async(request, runtime)

    def describe_firewall_template_rules_apply_result_with_options(
        self,
        request: swas__open20200601_models.DescribeFirewallTemplateRulesApplyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeFirewallTemplateRulesApplyResultResponse:
        """
        @summary Queries the result of applying a firewall template rule to simple application servers.
        
        @param request: DescribeFirewallTemplateRulesApplyResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFirewallTemplateRulesApplyResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFirewallTemplateRulesApplyResult',
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
            swas__open20200601_models.DescribeFirewallTemplateRulesApplyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_firewall_template_rules_apply_result_with_options_async(
        self,
        request: swas__open20200601_models.DescribeFirewallTemplateRulesApplyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeFirewallTemplateRulesApplyResultResponse:
        """
        @summary Queries the result of applying a firewall template rule to simple application servers.
        
        @param request: DescribeFirewallTemplateRulesApplyResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFirewallTemplateRulesApplyResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFirewallTemplateRulesApplyResult',
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
            swas__open20200601_models.DescribeFirewallTemplateRulesApplyResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_firewall_template_rules_apply_result(
        self,
        request: swas__open20200601_models.DescribeFirewallTemplateRulesApplyResultRequest,
    ) -> swas__open20200601_models.DescribeFirewallTemplateRulesApplyResultResponse:
        """
        @summary Queries the result of applying a firewall template rule to simple application servers.
        
        @param request: DescribeFirewallTemplateRulesApplyResultRequest
        @return: DescribeFirewallTemplateRulesApplyResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_firewall_template_rules_apply_result_with_options(request, runtime)

    async def describe_firewall_template_rules_apply_result_async(
        self,
        request: swas__open20200601_models.DescribeFirewallTemplateRulesApplyResultRequest,
    ) -> swas__open20200601_models.DescribeFirewallTemplateRulesApplyResultResponse:
        """
        @summary Queries the result of applying a firewall template rule to simple application servers.
        
        @param request: DescribeFirewallTemplateRulesApplyResultRequest
        @return: DescribeFirewallTemplateRulesApplyResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_firewall_template_rules_apply_result_with_options_async(request, runtime)

    def describe_firewall_templates_with_options(
        self,
        request: swas__open20200601_models.DescribeFirewallTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeFirewallTemplatesResponse:
        """
        @summary Queries details about firewall templates.
        
        @param request: DescribeFirewallTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFirewallTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
            action='DescribeFirewallTemplates',
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
            swas__open20200601_models.DescribeFirewallTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_firewall_templates_with_options_async(
        self,
        request: swas__open20200601_models.DescribeFirewallTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeFirewallTemplatesResponse:
        """
        @summary Queries details about firewall templates.
        
        @param request: DescribeFirewallTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFirewallTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
            action='DescribeFirewallTemplates',
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
            swas__open20200601_models.DescribeFirewallTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_firewall_templates(
        self,
        request: swas__open20200601_models.DescribeFirewallTemplatesRequest,
    ) -> swas__open20200601_models.DescribeFirewallTemplatesResponse:
        """
        @summary Queries details about firewall templates.
        
        @param request: DescribeFirewallTemplatesRequest
        @return: DescribeFirewallTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_firewall_templates_with_options(request, runtime)

    async def describe_firewall_templates_async(
        self,
        request: swas__open20200601_models.DescribeFirewallTemplatesRequest,
    ) -> swas__open20200601_models.DescribeFirewallTemplatesResponse:
        """
        @summary Queries details about firewall templates.
        
        @param request: DescribeFirewallTemplatesRequest
        @return: DescribeFirewallTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_firewall_templates_with_options_async(request, runtime)

    def describe_instance_key_pair_with_options(
        self,
        request: swas__open20200601_models.DescribeInstanceKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInstanceKeyPairResponse:
        """
        @summary Queries information about the key pair of a simple application server.
        
        @param request: DescribeInstanceKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceKeyPairResponse
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
        """
        @summary Queries information about the key pair of a simple application server.
        
        @param request: DescribeInstanceKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceKeyPairResponse
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
        """
        @summary Queries information about the key pair of a simple application server.
        
        @param request: DescribeInstanceKeyPairRequest
        @return: DescribeInstanceKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_key_pair_with_options(request, runtime)

    async def describe_instance_key_pair_async(
        self,
        request: swas__open20200601_models.DescribeInstanceKeyPairRequest,
    ) -> swas__open20200601_models.DescribeInstanceKeyPairResponse:
        """
        @summary Queries information about the key pair of a simple application server.
        
        @param request: DescribeInstanceKeyPairRequest
        @return: DescribeInstanceKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_key_pair_with_options_async(request, runtime)

    def describe_instance_passwords_setting_with_options(
        self,
        request: swas__open20200601_models.DescribeInstancePasswordsSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInstancePasswordsSettingResponse:
        """
        @summary Checks whether a password is set for a simple application server.
        
        @param request: DescribeInstancePasswordsSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancePasswordsSettingResponse
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
        """
        @summary Checks whether a password is set for a simple application server.
        
        @param request: DescribeInstancePasswordsSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancePasswordsSettingResponse
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
        """
        @summary Checks whether a password is set for a simple application server.
        
        @param request: DescribeInstancePasswordsSettingRequest
        @return: DescribeInstancePasswordsSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_passwords_setting_with_options(request, runtime)

    async def describe_instance_passwords_setting_async(
        self,
        request: swas__open20200601_models.DescribeInstancePasswordsSettingRequest,
    ) -> swas__open20200601_models.DescribeInstancePasswordsSettingResponse:
        """
        @summary Checks whether a password is set for a simple application server.
        
        @param request: DescribeInstancePasswordsSettingRequest
        @return: DescribeInstancePasswordsSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_passwords_setting_with_options_async(request, runtime)

    def describe_instance_vnc_url_with_options(
        self,
        request: swas__open20200601_models.DescribeInstanceVncUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInstanceVncUrlResponse:
        """
        @summary Queries the VNC connection address of a simple application server.
        
        @param request: DescribeInstanceVncUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceVncUrlResponse
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
        """
        @summary Queries the VNC connection address of a simple application server.
        
        @param request: DescribeInstanceVncUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceVncUrlResponse
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
        """
        @summary Queries the VNC connection address of a simple application server.
        
        @param request: DescribeInstanceVncUrlRequest
        @return: DescribeInstanceVncUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_vnc_url_with_options(request, runtime)

    async def describe_instance_vnc_url_async(
        self,
        request: swas__open20200601_models.DescribeInstanceVncUrlRequest,
    ) -> swas__open20200601_models.DescribeInstanceVncUrlResponse:
        """
        @summary Queries the VNC connection address of a simple application server.
        
        @param request: DescribeInstanceVncUrlRequest
        @return: DescribeInstanceVncUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_vnc_url_with_options_async(request, runtime)

    def describe_invocation_result_with_options(
        self,
        request: swas__open20200601_models.DescribeInvocationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeInvocationResultResponse:
        """
        @summary Queries the execution result of a command.
        
        @description    After you execute a command, the command may not succeed or return the expected results. You can call this operation to query the execution result of a command.
        You can query the execution results that were generated within the last two weeks. A maximum of 100,000 entries of execution results can be retained.
        
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
        @summary Queries the execution result of a command.
        
        @description    After you execute a command, the command may not succeed or return the expected results. You can call this operation to query the execution result of a command.
        You can query the execution results that were generated within the last two weeks. A maximum of 100,000 entries of execution results can be retained.
        
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
        @summary Queries the execution result of a command.
        
        @description    After you execute a command, the command may not succeed or return the expected results. You can call this operation to query the execution result of a command.
        You can query the execution results that were generated within the last two weeks. A maximum of 100,000 entries of execution results can be retained.
        
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
        @summary Queries the execution result of a command.
        
        @description    After you execute a command, the command may not succeed or return the expected results. You can call this operation to query the execution result of a command.
        You can query the execution results that were generated within the last two weeks. A maximum of 100,000 entries of execution results can be retained.
        
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
        @summary Queries details about command execution.
        
        @description    After you execute a command, the command may not succeed or return the expected results. You can call this operation to query the actual execution results.
        You can query the execution results that were generated within the last two weeks. Up to 100,000 entries of execution results can be retained.
        
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
        @summary Queries details about command execution.
        
        @description    After you execute a command, the command may not succeed or return the expected results. You can call this operation to query the actual execution results.
        You can query the execution results that were generated within the last two weeks. Up to 100,000 entries of execution results can be retained.
        
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
        @summary Queries details about command execution.
        
        @description    After you execute a command, the command may not succeed or return the expected results. You can call this operation to query the actual execution results.
        You can query the execution results that were generated within the last two weeks. Up to 100,000 entries of execution results can be retained.
        
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
        @summary Queries details about command execution.
        
        @description    After you execute a command, the command may not succeed or return the expected results. You can call this operation to query the actual execution results.
        You can query the execution results that were generated within the last two weeks. Up to 100,000 entries of execution results can be retained.
        
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
        """
        @summary Queries the monitoring information about vCPUs, memory, disk IOPS, and traffic of a simple application server.
        
        @param request: DescribeMonitorDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMonitorDataResponse
        """
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
        """
        @summary Queries the monitoring information about vCPUs, memory, disk IOPS, and traffic of a simple application server.
        
        @param request: DescribeMonitorDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMonitorDataResponse
        """
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
        """
        @summary Queries the monitoring information about vCPUs, memory, disk IOPS, and traffic of a simple application server.
        
        @param request: DescribeMonitorDataRequest
        @return: DescribeMonitorDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_data_with_options(request, runtime)

    async def describe_monitor_data_async(
        self,
        request: swas__open20200601_models.DescribeMonitorDataRequest,
    ) -> swas__open20200601_models.DescribeMonitorDataResponse:
        """
        @summary Queries the monitoring information about vCPUs, memory, disk IOPS, and traffic of a simple application server.
        
        @param request: DescribeMonitorDataRequest
        @return: DescribeMonitorDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_data_with_options_async(request, runtime)

    def describe_security_agent_status_with_options(
        self,
        request: swas__open20200601_models.DescribeSecurityAgentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DescribeSecurityAgentStatusResponse:
        """
        @summary Queries the status of the Security Center agent on a simple application server.
        
        @param request: DescribeSecurityAgentStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityAgentStatusResponse
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
        """
        @summary Queries the status of the Security Center agent on a simple application server.
        
        @param request: DescribeSecurityAgentStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityAgentStatusResponse
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
        """
        @summary Queries the status of the Security Center agent on a simple application server.
        
        @param request: DescribeSecurityAgentStatusRequest
        @return: DescribeSecurityAgentStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_security_agent_status_with_options(request, runtime)

    async def describe_security_agent_status_async(
        self,
        request: swas__open20200601_models.DescribeSecurityAgentStatusRequest,
    ) -> swas__open20200601_models.DescribeSecurityAgentStatusResponse:
        """
        @summary Queries the status of the Security Center agent on a simple application server.
        
        @param request: DescribeSecurityAgentStatusRequest
        @return: DescribeSecurityAgentStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_agent_status_with_options_async(request, runtime)

    def detach_key_pair_with_options(
        self,
        request: swas__open20200601_models.DetachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DetachKeyPairResponse:
        """
        @summary Unbinds key pairs from simple application servers.
        
        @description If you want to change the SSH key pairs that are bound to your simple application servers or your end user no longer needs to access a specific simple application server, you can unbind the SSH key pairs from simple application servers to improve the security of the simple application servers or restrict access to the specific simple application server.
        
        @param request: DetachKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachKeyPair',
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
            swas__open20200601_models.DetachKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_key_pair_with_options_async(
        self,
        request: swas__open20200601_models.DetachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DetachKeyPairResponse:
        """
        @summary Unbinds key pairs from simple application servers.
        
        @description If you want to change the SSH key pairs that are bound to your simple application servers or your end user no longer needs to access a specific simple application server, you can unbind the SSH key pairs from simple application servers to improve the security of the simple application servers or restrict access to the specific simple application server.
        
        @param request: DetachKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachKeyPair',
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
            swas__open20200601_models.DetachKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_key_pair(
        self,
        request: swas__open20200601_models.DetachKeyPairRequest,
    ) -> swas__open20200601_models.DetachKeyPairResponse:
        """
        @summary Unbinds key pairs from simple application servers.
        
        @description If you want to change the SSH key pairs that are bound to your simple application servers or your end user no longer needs to access a specific simple application server, you can unbind the SSH key pairs from simple application servers to improve the security of the simple application servers or restrict access to the specific simple application server.
        
        @param request: DetachKeyPairRequest
        @return: DetachKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_key_pair_with_options(request, runtime)

    async def detach_key_pair_async(
        self,
        request: swas__open20200601_models.DetachKeyPairRequest,
    ) -> swas__open20200601_models.DetachKeyPairResponse:
        """
        @summary Unbinds key pairs from simple application servers.
        
        @description If you want to change the SSH key pairs that are bound to your simple application servers or your end user no longer needs to access a specific simple application server, you can unbind the SSH key pairs from simple application servers to improve the security of the simple application servers or restrict access to the specific simple application server.
        
        @param request: DetachKeyPairRequest
        @return: DetachKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_key_pair_with_options_async(request, runtime)

    def disable_firewall_rule_with_options(
        self,
        request: swas__open20200601_models.DisableFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.DisableFirewallRuleResponse:
        """
        @summary Disables a firewall rule of a simple application server.
        
        @param request: DisableFirewallRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableFirewallRuleResponse
        """
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
        """
        @summary Disables a firewall rule of a simple application server.
        
        @param request: DisableFirewallRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableFirewallRuleResponse
        """
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
        """
        @summary Disables a firewall rule of a simple application server.
        
        @param request: DisableFirewallRuleRequest
        @return: DisableFirewallRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_firewall_rule_with_options(request, runtime)

    async def disable_firewall_rule_async(
        self,
        request: swas__open20200601_models.DisableFirewallRuleRequest,
    ) -> swas__open20200601_models.DisableFirewallRuleResponse:
        """
        @summary Disables a firewall rule of a simple application server.
        
        @param request: DisableFirewallRuleRequest
        @return: DisableFirewallRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_firewall_rule_with_options_async(request, runtime)

    def enable_firewall_rule_with_options(
        self,
        request: swas__open20200601_models.EnableFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.EnableFirewallRuleResponse:
        """
        @summary Enables a firewall rule for a simple application server.
        
        @param request: EnableFirewallRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableFirewallRuleResponse
        """
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
        """
        @summary Enables a firewall rule for a simple application server.
        
        @param request: EnableFirewallRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableFirewallRuleResponse
        """
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
        """
        @summary Enables a firewall rule for a simple application server.
        
        @param request: EnableFirewallRuleRequest
        @return: EnableFirewallRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_firewall_rule_with_options(request, runtime)

    async def enable_firewall_rule_async(
        self,
        request: swas__open20200601_models.EnableFirewallRuleRequest,
    ) -> swas__open20200601_models.EnableFirewallRuleResponse:
        """
        @summary Enables a firewall rule for a simple application server.
        
        @param request: EnableFirewallRuleRequest
        @return: EnableFirewallRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_firewall_rule_with_options_async(request, runtime)

    def import_key_pair_with_options(
        self,
        request: swas__open20200601_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ImportKeyPairResponse:
        """
        @summary Imports an existing key pair to the Simple Application Server console.
        
        @description You can call this operation to import an existing key pair to the Simple Application Server console. This way, you can use the key pair to log on to simple application servers. The existing key pair that you want to import must use a supported encryption method. For more information, see [Q2: Which encryption methods must be used by key pairs when I import existing key pairs to the Simple Application Server console?](https://help.aliyun.com/document_detail/59085.html)
        
        @param request: ImportKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeyPair',
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
            swas__open20200601_models.ImportKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_key_pair_with_options_async(
        self,
        request: swas__open20200601_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ImportKeyPairResponse:
        """
        @summary Imports an existing key pair to the Simple Application Server console.
        
        @description You can call this operation to import an existing key pair to the Simple Application Server console. This way, you can use the key pair to log on to simple application servers. The existing key pair that you want to import must use a supported encryption method. For more information, see [Q2: Which encryption methods must be used by key pairs when I import existing key pairs to the Simple Application Server console?](https://help.aliyun.com/document_detail/59085.html)
        
        @param request: ImportKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeyPair',
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
            swas__open20200601_models.ImportKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_key_pair(
        self,
        request: swas__open20200601_models.ImportKeyPairRequest,
    ) -> swas__open20200601_models.ImportKeyPairResponse:
        """
        @summary Imports an existing key pair to the Simple Application Server console.
        
        @description You can call this operation to import an existing key pair to the Simple Application Server console. This way, you can use the key pair to log on to simple application servers. The existing key pair that you want to import must use a supported encryption method. For more information, see [Q2: Which encryption methods must be used by key pairs when I import existing key pairs to the Simple Application Server console?](https://help.aliyun.com/document_detail/59085.html)
        
        @param request: ImportKeyPairRequest
        @return: ImportKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_key_pair_with_options(request, runtime)

    async def import_key_pair_async(
        self,
        request: swas__open20200601_models.ImportKeyPairRequest,
    ) -> swas__open20200601_models.ImportKeyPairResponse:
        """
        @summary Imports an existing key pair to the Simple Application Server console.
        
        @description You can call this operation to import an existing key pair to the Simple Application Server console. This way, you can use the key pair to log on to simple application servers. The existing key pair that you want to import must use a supported encryption method. For more information, see [Q2: Which encryption methods must be used by key pairs when I import existing key pairs to the Simple Application Server console?](https://help.aliyun.com/document_detail/59085.html)
        
        @param request: ImportKeyPairRequest
        @return: ImportKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_key_pair_with_options_async(request, runtime)

    def install_cloud_assistant_with_options(
        self,
        tmp_req: swas__open20200601_models.InstallCloudAssistantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.InstallCloudAssistantResponse:
        """
        @summary Installs the Cloud Assistant client on simple application servers at a time.
        
        @description To run commands on your simple application servers, you must install the Cloud Assistant client on your servers. You can call the [DescribeCloudAssistantStatus](https://help.aliyun.com/document_detail/439512.html) operation to check whether the Cloud Assistant client is installed on your simple application servers. If you have not installed the Cloud Assistant client, you can call the InstallCloudAssistant operation to install the client. Then, you can call the [RebootInstance](https://help.aliyun.com/document_detail/190443.html) operation to restart the servers to allow the client to take effect.
        
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
        @summary Installs the Cloud Assistant client on simple application servers at a time.
        
        @description To run commands on your simple application servers, you must install the Cloud Assistant client on your servers. You can call the [DescribeCloudAssistantStatus](https://help.aliyun.com/document_detail/439512.html) operation to check whether the Cloud Assistant client is installed on your simple application servers. If you have not installed the Cloud Assistant client, you can call the InstallCloudAssistant operation to install the client. Then, you can call the [RebootInstance](https://help.aliyun.com/document_detail/190443.html) operation to restart the servers to allow the client to take effect.
        
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
        @summary Installs the Cloud Assistant client on simple application servers at a time.
        
        @description To run commands on your simple application servers, you must install the Cloud Assistant client on your servers. You can call the [DescribeCloudAssistantStatus](https://help.aliyun.com/document_detail/439512.html) operation to check whether the Cloud Assistant client is installed on your simple application servers. If you have not installed the Cloud Assistant client, you can call the InstallCloudAssistant operation to install the client. Then, you can call the [RebootInstance](https://help.aliyun.com/document_detail/190443.html) operation to restart the servers to allow the client to take effect.
        
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
        @summary Installs the Cloud Assistant client on simple application servers at a time.
        
        @description To run commands on your simple application servers, you must install the Cloud Assistant client on your servers. You can call the [DescribeCloudAssistantStatus](https://help.aliyun.com/document_detail/439512.html) operation to check whether the Cloud Assistant client is installed on your simple application servers. If you have not installed the Cloud Assistant client, you can call the InstallCloudAssistant operation to install the client. Then, you can call the [RebootInstance](https://help.aliyun.com/document_detail/190443.html) operation to restart the servers to allow the client to take effect.
        
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
        """
        @summary Installs the CloudMonitor agent for a simple application server.
        
        @param request: InstallCloudMonitorAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallCloudMonitorAgentResponse
        """
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
        """
        @summary Installs the CloudMonitor agent for a simple application server.
        
        @param request: InstallCloudMonitorAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallCloudMonitorAgentResponse
        """
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
        """
        @summary Installs the CloudMonitor agent for a simple application server.
        
        @param request: InstallCloudMonitorAgentRequest
        @return: InstallCloudMonitorAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_cloud_monitor_agent_with_options(request, runtime)

    async def install_cloud_monitor_agent_async(
        self,
        request: swas__open20200601_models.InstallCloudMonitorAgentRequest,
    ) -> swas__open20200601_models.InstallCloudMonitorAgentResponse:
        """
        @summary Installs the CloudMonitor agent for a simple application server.
        
        @param request: InstallCloudMonitorAgentRequest
        @return: InstallCloudMonitorAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.install_cloud_monitor_agent_with_options_async(request, runtime)

    def invoke_command_with_options(
        self,
        tmp_req: swas__open20200601_models.InvokeCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.InvokeCommandResponse:
        """
        @summary Runs a Command Assistant command for one or more simple application servers.
        
        @description    The simple application servers for which you want to call the operation must meet the following conditions. If a simple application server cannot meet the conditions, you must call this operation again.
        The simple application servers are in the `Running` state. You can call the [ListInstances](https://help.aliyun.com/document_detail/2361065.html) operation to query the status of simple application servers.
        Cloud Assistant Agent is installed on the simple application servers. For more information, see [InstallCloudAssistant](https://help.aliyun.com/document_detail/2361030.html).
        If you run a PowerShell command, make sure that the PowerShell module is configured for the simple application servers.
        The command may fail to be run due to the abnormal states of simple application servers, network exceptions, or exceptions in Cloud Assistant Agent. If the command fails to be run, no execution information is generated.
        If you enable the custom parameter feature when you create a command, you must set the `Parameters` parameter to specify custom parameters when you run the command.
        When you call this operation, you can select only one common command or a custom command that you have created.
        
        @param tmp_req: InvokeCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokeCommandResponse
        """
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.InvokeCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvokeCommand',
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
            swas__open20200601_models.InvokeCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_command_with_options_async(
        self,
        tmp_req: swas__open20200601_models.InvokeCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.InvokeCommandResponse:
        """
        @summary Runs a Command Assistant command for one or more simple application servers.
        
        @description    The simple application servers for which you want to call the operation must meet the following conditions. If a simple application server cannot meet the conditions, you must call this operation again.
        The simple application servers are in the `Running` state. You can call the [ListInstances](https://help.aliyun.com/document_detail/2361065.html) operation to query the status of simple application servers.
        Cloud Assistant Agent is installed on the simple application servers. For more information, see [InstallCloudAssistant](https://help.aliyun.com/document_detail/2361030.html).
        If you run a PowerShell command, make sure that the PowerShell module is configured for the simple application servers.
        The command may fail to be run due to the abnormal states of simple application servers, network exceptions, or exceptions in Cloud Assistant Agent. If the command fails to be run, no execution information is generated.
        If you enable the custom parameter feature when you create a command, you must set the `Parameters` parameter to specify custom parameters when you run the command.
        When you call this operation, you can select only one common command or a custom command that you have created.
        
        @param tmp_req: InvokeCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvokeCommandResponse
        """
        UtilClient.validate_model(tmp_req)
        request = swas__open20200601_models.InvokeCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvokeCommand',
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
            swas__open20200601_models.InvokeCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_command(
        self,
        request: swas__open20200601_models.InvokeCommandRequest,
    ) -> swas__open20200601_models.InvokeCommandResponse:
        """
        @summary Runs a Command Assistant command for one or more simple application servers.
        
        @description    The simple application servers for which you want to call the operation must meet the following conditions. If a simple application server cannot meet the conditions, you must call this operation again.
        The simple application servers are in the `Running` state. You can call the [ListInstances](https://help.aliyun.com/document_detail/2361065.html) operation to query the status of simple application servers.
        Cloud Assistant Agent is installed on the simple application servers. For more information, see [InstallCloudAssistant](https://help.aliyun.com/document_detail/2361030.html).
        If you run a PowerShell command, make sure that the PowerShell module is configured for the simple application servers.
        The command may fail to be run due to the abnormal states of simple application servers, network exceptions, or exceptions in Cloud Assistant Agent. If the command fails to be run, no execution information is generated.
        If you enable the custom parameter feature when you create a command, you must set the `Parameters` parameter to specify custom parameters when you run the command.
        When you call this operation, you can select only one common command or a custom command that you have created.
        
        @param request: InvokeCommandRequest
        @return: InvokeCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.invoke_command_with_options(request, runtime)

    async def invoke_command_async(
        self,
        request: swas__open20200601_models.InvokeCommandRequest,
    ) -> swas__open20200601_models.InvokeCommandResponse:
        """
        @summary Runs a Command Assistant command for one or more simple application servers.
        
        @description    The simple application servers for which you want to call the operation must meet the following conditions. If a simple application server cannot meet the conditions, you must call this operation again.
        The simple application servers are in the `Running` state. You can call the [ListInstances](https://help.aliyun.com/document_detail/2361065.html) operation to query the status of simple application servers.
        Cloud Assistant Agent is installed on the simple application servers. For more information, see [InstallCloudAssistant](https://help.aliyun.com/document_detail/2361030.html).
        If you run a PowerShell command, make sure that the PowerShell module is configured for the simple application servers.
        The command may fail to be run due to the abnormal states of simple application servers, network exceptions, or exceptions in Cloud Assistant Agent. If the command fails to be run, no execution information is generated.
        If you enable the custom parameter feature when you create a command, you must set the `Parameters` parameter to specify custom parameters when you run the command.
        When you call this operation, you can select only one common command or a custom command that you have created.
        
        @param request: InvokeCommandRequest
        @return: InvokeCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.invoke_command_with_options_async(request, runtime)

    def list_custom_image_share_accounts_with_options(
        self,
        request: swas__open20200601_models.ListCustomImageShareAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListCustomImageShareAccountsResponse:
        """
        @summary Queries information about custom images that are shared across Alibaba Cloud accounts in a region.
        
        @param request: ListCustomImageShareAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomImageShareAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
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
            action='ListCustomImageShareAccounts',
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
            swas__open20200601_models.ListCustomImageShareAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_image_share_accounts_with_options_async(
        self,
        request: swas__open20200601_models.ListCustomImageShareAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListCustomImageShareAccountsResponse:
        """
        @summary Queries information about custom images that are shared across Alibaba Cloud accounts in a region.
        
        @param request: ListCustomImageShareAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomImageShareAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
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
            action='ListCustomImageShareAccounts',
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
            swas__open20200601_models.ListCustomImageShareAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_image_share_accounts(
        self,
        request: swas__open20200601_models.ListCustomImageShareAccountsRequest,
    ) -> swas__open20200601_models.ListCustomImageShareAccountsResponse:
        """
        @summary Queries information about custom images that are shared across Alibaba Cloud accounts in a region.
        
        @param request: ListCustomImageShareAccountsRequest
        @return: ListCustomImageShareAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_image_share_accounts_with_options(request, runtime)

    async def list_custom_image_share_accounts_async(
        self,
        request: swas__open20200601_models.ListCustomImageShareAccountsRequest,
    ) -> swas__open20200601_models.ListCustomImageShareAccountsResponse:
        """
        @summary Queries information about custom images that are shared across Alibaba Cloud accounts in a region.
        
        @param request: ListCustomImageShareAccountsRequest
        @return: ListCustomImageShareAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_image_share_accounts_with_options_async(request, runtime)

    def list_custom_images_with_options(
        self,
        request: swas__open20200601_models.ListCustomImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListCustomImagesResponse:
        """
        @summary Queries the information about custom images in a region.
        
        @param request: ListCustomImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomImagesResponse
        """
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.share):
            query['Share'] = request.share
        if not UtilClient.is_unset(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        @summary Queries the information about custom images in a region.
        
        @param request: ListCustomImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomImagesResponse
        """
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
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.share):
            query['Share'] = request.share
        if not UtilClient.is_unset(request.system_snapshot_id):
            query['SystemSnapshotId'] = request.system_snapshot_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        @summary Queries the information about custom images in a region.
        
        @param request: ListCustomImagesRequest
        @return: ListCustomImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_images_with_options(request, runtime)

    async def list_custom_images_async(
        self,
        request: swas__open20200601_models.ListCustomImagesRequest,
    ) -> swas__open20200601_models.ListCustomImagesResponse:
        """
        @summary Queries the information about custom images in a region.
        
        @param request: ListCustomImagesRequest
        @return: ListCustomImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_images_with_options_async(request, runtime)

    def list_disks_with_options(
        self,
        request: swas__open20200601_models.ListDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListDisksResponse:
        """
        @summary Queries the information about disks in a region.
        
        @description You can specify multiple request parameters that you want to query, such as `InstanceId`, `DiskIds`, and `ResourceGroupId`. Specified request parameters have logical AND relations. Only the specified parameters are included in the filter conditions.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        @summary Queries the information about disks in a region.
        
        @description You can specify multiple request parameters that you want to query, such as `InstanceId`, `DiskIds`, and `ResourceGroupId`. Specified request parameters have logical AND relations. Only the specified parameters are included in the filter conditions.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        @summary Queries the information about disks in a region.
        
        @description You can specify multiple request parameters that you want to query, such as `InstanceId`, `DiskIds`, and `ResourceGroupId`. Specified request parameters have logical AND relations. Only the specified parameters are included in the filter conditions.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the information about disks in a region.
        
        @description You can specify multiple request parameters that you want to query, such as `InstanceId`, `DiskIds`, and `ResourceGroupId`. Specified request parameters have logical AND relations. Only the specified parameters are included in the filter conditions.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the firewall rules of a simple application server.
        
        @description You can call the ListFirewallRules operation to query the firewall rule details of a simple application server, including the port range, firewall rule ID, and transport layer protocol.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ListFirewallRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFirewallRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_rule_id):
            query['FirewallRuleId'] = request.firewall_rule_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        @summary Queries the firewall rules of a simple application server.
        
        @description You can call the ListFirewallRules operation to query the firewall rule details of a simple application server, including the port range, firewall rule ID, and transport layer protocol.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ListFirewallRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFirewallRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_rule_id):
            query['FirewallRuleId'] = request.firewall_rule_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        @summary Queries the firewall rules of a simple application server.
        
        @description You can call the ListFirewallRules operation to query the firewall rule details of a simple application server, including the port range, firewall rule ID, and transport layer protocol.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the firewall rules of a simple application server.
        
        @description You can call the ListFirewallRules operation to query the firewall rule details of a simple application server, including the port range, firewall rule ID, and transport layer protocol.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the information about images in a region.
        
        @description You can query information about images in a region, including the IDs, names, and types of the images.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the information about images in a region.
        
        @description You can query information about images in a region, including the IDs, names, and types of the images.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the information about images in a region.
        
        @description You can query information about images in a region, including the IDs, names, and types of the images.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the information about images in a region.
        
        @description You can query information about images in a region, including the IDs, names, and types of the images.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the plans to which you can upgrade your simple application server.
        
        @description If the plan of your simple application server does not meet your business requirements, you can call the ListInstancePlansModification operation to obtain a list of plans to which you can upgrade your simple application server. Then, you can call the [UpgradeInstance](https://help.aliyun.com/document_detail/190445.html) operation to upgrade the server.
        > We recommend that you create snapshots for the disks of your simple application server to back up data before you upgrade the server. For more information, see [CreateSnapshot](https://help.aliyun.com/document_detail/190452.html).
        For the precautions about plan upgrade, see [Upgrade a simple application server](https://help.aliyun.com/document_detail/61433.html).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the plans to which you can upgrade your simple application server.
        
        @description If the plan of your simple application server does not meet your business requirements, you can call the ListInstancePlansModification operation to obtain a list of plans to which you can upgrade your simple application server. Then, you can call the [UpgradeInstance](https://help.aliyun.com/document_detail/190445.html) operation to upgrade the server.
        > We recommend that you create snapshots for the disks of your simple application server to back up data before you upgrade the server. For more information, see [CreateSnapshot](https://help.aliyun.com/document_detail/190452.html).
        For the precautions about plan upgrade, see [Upgrade a simple application server](https://help.aliyun.com/document_detail/61433.html).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the plans to which you can upgrade your simple application server.
        
        @description If the plan of your simple application server does not meet your business requirements, you can call the ListInstancePlansModification operation to obtain a list of plans to which you can upgrade your simple application server. Then, you can call the [UpgradeInstance](https://help.aliyun.com/document_detail/190445.html) operation to upgrade the server.
        > We recommend that you create snapshots for the disks of your simple application server to back up data before you upgrade the server. For more information, see [CreateSnapshot](https://help.aliyun.com/document_detail/190452.html).
        For the precautions about plan upgrade, see [Upgrade a simple application server](https://help.aliyun.com/document_detail/61433.html).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the plans to which you can upgrade your simple application server.
        
        @description If the plan of your simple application server does not meet your business requirements, you can call the ListInstancePlansModification operation to obtain a list of plans to which you can upgrade your simple application server. Then, you can call the [UpgradeInstance](https://help.aliyun.com/document_detail/190445.html) operation to upgrade the server.
        > We recommend that you create snapshots for the disks of your simple application server to back up data before you upgrade the server. For more information, see [CreateSnapshot](https://help.aliyun.com/document_detail/190452.html).
        For the precautions about plan upgrade, see [Upgrade a simple application server](https://help.aliyun.com/document_detail/61433.html).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        """
        @summary Queries the status of simple application servers.
        
        @param request: ListInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceStatusResponse
        """
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
        """
        @summary Queries the status of simple application servers.
        
        @param request: ListInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceStatusResponse
        """
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
        """
        @summary Queries the status of simple application servers.
        
        @param request: ListInstanceStatusRequest
        @return: ListInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_status_with_options(request, runtime)

    async def list_instance_status_async(
        self,
        request: swas__open20200601_models.ListInstanceStatusRequest,
    ) -> swas__open20200601_models.ListInstanceStatusResponse:
        """
        @summary Queries the status of simple application servers.
        
        @param request: ListInstanceStatusRequest
        @return: ListInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_status_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: swas__open20200601_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListInstancesResponse:
        """
        @summary Queries the information about simple application servers in a region.
        
        @description You can call this operation to query the details of simple application servers in a specified region, including the names, public IP addresses, internal IP addresses, creation time, and expiration time of the servers.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.public_ip_addresses):
            query['PublicIpAddresses'] = request.public_ip_addresses
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        @summary Queries the information about simple application servers in a region.
        
        @description You can call this operation to query the details of simple application servers in a specified region, including the names, public IP addresses, internal IP addresses, creation time, and expiration time of the servers.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.public_ip_addresses):
            query['PublicIpAddresses'] = request.public_ip_addresses
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        @summary Queries the information about simple application servers in a region.
        
        @description You can call this operation to query the details of simple application servers in a specified region, including the names, public IP addresses, internal IP addresses, creation time, and expiration time of the servers.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the information about simple application servers in a region.
        
        @description You can call this operation to query the details of simple application servers in a specified region, including the names, public IP addresses, internal IP addresses, creation time, and expiration time of the servers.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the details about data transfer plans of simple application servers.
        
        @description You can query the details of data transfer plans of simple application servers, including the data transfer quota, used amount and unused amount of the data transfer quota, and excess data transfers beyond the quota in the current month.
        Simple Application Server provides data transfer quotas in plans. Plan prices include prices of data transfer quotas. You are charged for data transfers that exceed the quotas. Take note of the following items:
        Only outbound data transfers of simple application servers over the Internet are calculated. Outbound data transfers include the data transfer quota and the excess data transfers beyond the quota. Inbound data transfers of simple application servers over the Internet are not calculated.
        Outbound data transfers from simple application servers to other Alibaba Cloud services over the Internet first consume data transfer quotas. If the quotas are exhausted, you are charged for excess data transfers.
        You are not charged for data transfers between simple application servers within the same virtual private cloud (VPC).
        For more information, see [Quotas and billing of data transfers](https://help.aliyun.com/document_detail/86281.html).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the details about data transfer plans of simple application servers.
        
        @description You can query the details of data transfer plans of simple application servers, including the data transfer quota, used amount and unused amount of the data transfer quota, and excess data transfers beyond the quota in the current month.
        Simple Application Server provides data transfer quotas in plans. Plan prices include prices of data transfer quotas. You are charged for data transfers that exceed the quotas. Take note of the following items:
        Only outbound data transfers of simple application servers over the Internet are calculated. Outbound data transfers include the data transfer quota and the excess data transfers beyond the quota. Inbound data transfers of simple application servers over the Internet are not calculated.
        Outbound data transfers from simple application servers to other Alibaba Cloud services over the Internet first consume data transfer quotas. If the quotas are exhausted, you are charged for excess data transfers.
        You are not charged for data transfers between simple application servers within the same virtual private cloud (VPC).
        For more information, see [Quotas and billing of data transfers](https://help.aliyun.com/document_detail/86281.html).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the details about data transfer plans of simple application servers.
        
        @description You can query the details of data transfer plans of simple application servers, including the data transfer quota, used amount and unused amount of the data transfer quota, and excess data transfers beyond the quota in the current month.
        Simple Application Server provides data transfer quotas in plans. Plan prices include prices of data transfer quotas. You are charged for data transfers that exceed the quotas. Take note of the following items:
        Only outbound data transfers of simple application servers over the Internet are calculated. Outbound data transfers include the data transfer quota and the excess data transfers beyond the quota. Inbound data transfers of simple application servers over the Internet are not calculated.
        Outbound data transfers from simple application servers to other Alibaba Cloud services over the Internet first consume data transfer quotas. If the quotas are exhausted, you are charged for excess data transfers.
        You are not charged for data transfers between simple application servers within the same virtual private cloud (VPC).
        For more information, see [Quotas and billing of data transfers](https://help.aliyun.com/document_detail/86281.html).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the details about data transfer plans of simple application servers.
        
        @description You can query the details of data transfer plans of simple application servers, including the data transfer quota, used amount and unused amount of the data transfer quota, and excess data transfers beyond the quota in the current month.
        Simple Application Server provides data transfer quotas in plans. Plan prices include prices of data transfer quotas. You are charged for data transfers that exceed the quotas. Take note of the following items:
        Only outbound data transfers of simple application servers over the Internet are calculated. Outbound data transfers include the data transfer quota and the excess data transfers beyond the quota. Inbound data transfers of simple application servers over the Internet are not calculated.
        Outbound data transfers from simple application servers to other Alibaba Cloud services over the Internet first consume data transfer quotas. If the quotas are exhausted, you are charged for excess data transfers.
        You are not charged for data transfers between simple application servers within the same virtual private cloud (VPC).
        For more information, see [Quotas and billing of data transfers](https://help.aliyun.com/document_detail/86281.html).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ListInstancesTrafficPackagesRequest
        @return: ListInstancesTrafficPackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_traffic_packages_with_options_async(request, runtime)

    def list_key_pairs_with_options(
        self,
        request: swas__open20200601_models.ListKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListKeyPairsResponse:
        """
        @summary Queries the AccessKey pairs that are bound to simple application servers in a specific region.
        
        @param request: ListKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKeyPairs',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_key_pairs_with_options_async(
        self,
        request: swas__open20200601_models.ListKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListKeyPairsResponse:
        """
        @summary Queries the AccessKey pairs that are bound to simple application servers in a specific region.
        
        @param request: ListKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKeyPairs',
            version='2020-06-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            swas__open20200601_models.ListKeyPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_key_pairs(
        self,
        request: swas__open20200601_models.ListKeyPairsRequest,
    ) -> swas__open20200601_models.ListKeyPairsResponse:
        """
        @summary Queries the AccessKey pairs that are bound to simple application servers in a specific region.
        
        @param request: ListKeyPairsRequest
        @return: ListKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_key_pairs_with_options(request, runtime)

    async def list_key_pairs_async(
        self,
        request: swas__open20200601_models.ListKeyPairsRequest,
    ) -> swas__open20200601_models.ListKeyPairsResponse:
        """
        @summary Queries the AccessKey pairs that are bound to simple application servers in a specific region.
        
        @param request: ListKeyPairsRequest
        @return: ListKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_key_pairs_with_options_async(request, runtime)

    def list_plans_with_options(
        self,
        request: swas__open20200601_models.ListPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListPlansResponse:
        """
        @summary Queries all plans provided by Simple Application Server in a region.
        
        @description You can query the details of all plans provided by Simple Application Server in a region, including the IDs, prices, disk sizes, and disk categories of the plans.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries all plans provided by Simple Application Server in a region.
        
        @description You can query the details of all plans provided by Simple Application Server in a region, including the IDs, prices, disk sizes, and disk categories of the plans.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries all plans provided by Simple Application Server in a region.
        
        @description You can query the details of all plans provided by Simple Application Server in a region, including the IDs, prices, disk sizes, and disk categories of the plans.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries all plans provided by Simple Application Server in a region.
        
        @description You can query the details of all plans provided by Simple Application Server in a region, including the IDs, prices, disk sizes, and disk categories of the plans.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ListPlansRequest
        @return: ListPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_plans_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: swas__open20200601_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListRegionsResponse:
        """
        @summary Queries all regions in which Simple Application Server is supported.
        
        @description The query results include all the Alibaba Cloud regions where Simple Application Server is supported on the international site (alibabacloud.com) and the China site (aliyun.com).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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
        request: swas__open20200601_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListRegionsResponse:
        """
        @summary Queries all regions in which Simple Application Server is supported.
        
        @description The query results include all the Alibaba Cloud regions where Simple Application Server is supported on the international site (alibabacloud.com) and the China site (aliyun.com).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
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

    def list_regions(
        self,
        request: swas__open20200601_models.ListRegionsRequest,
    ) -> swas__open20200601_models.ListRegionsResponse:
        """
        @summary Queries all regions in which Simple Application Server is supported.
        
        @description The query results include all the Alibaba Cloud regions where Simple Application Server is supported on the international site (alibabacloud.com) and the China site (aliyun.com).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ListRegionsRequest
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: swas__open20200601_models.ListRegionsRequest,
    ) -> swas__open20200601_models.ListRegionsResponse:
        """
        @summary Queries all regions in which Simple Application Server is supported.
        
        @description The query results include all the Alibaba Cloud regions where Simple Application Server is supported on the international site (alibabacloud.com) and the China site (aliyun.com).
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ListRegionsRequest
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_snapshots_with_options(
        self,
        request: swas__open20200601_models.ListSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListSnapshotsResponse:
        """
        @summary Queries the information about snapshots that are created for a simple application server.
        
        @description You can specify multiple request parameters that you want to query, such as `InstanceId`, `DiskId`, `SnapshotIds`, and `ResourceGroupId`. Specified parameters have logical AND relations. Only the specified parameters are included in the filter conditions.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.source_disk_type):
            query['SourceDiskType'] = request.source_disk_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        @summary Queries the information about snapshots that are created for a simple application server.
        
        @description You can specify multiple request parameters that you want to query, such as `InstanceId`, `DiskId`, `SnapshotIds`, and `ResourceGroupId`. Specified parameters have logical AND relations. Only the specified parameters are included in the filter conditions.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.source_disk_type):
            query['SourceDiskType'] = request.source_disk_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        @summary Queries the information about snapshots that are created for a simple application server.
        
        @description You can specify multiple request parameters that you want to query, such as `InstanceId`, `DiskId`, `SnapshotIds`, and `ResourceGroupId`. Specified parameters have logical AND relations. Only the specified parameters are included in the filter conditions.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Queries the information about snapshots that are created for a simple application server.
        
        @description You can specify multiple request parameters that you want to query, such as `InstanceId`, `DiskId`, `SnapshotIds`, and `ResourceGroupId`. Specified parameters have logical AND relations. Only the specified parameters are included in the filter conditions.
        ### [](#qps-)QPS limits
        You can call this operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ListSnapshotsRequest
        @return: ListSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_snapshots_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: swas__open20200601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to simple resources, such as instances, snapshots, disks, images, commands, and firewall rules.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            swas__open20200601_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: swas__open20200601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to simple resources, such as instances, snapshots, disks, images, commands, and firewall rules.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            swas__open20200601_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: swas__open20200601_models.ListTagResourcesRequest,
    ) -> swas__open20200601_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to simple resources, such as instances, snapshots, disks, images, commands, and firewall rules.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: swas__open20200601_models.ListTagResourcesRequest,
    ) -> swas__open20200601_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to simple resources, such as instances, snapshots, disks, images, commands, and firewall rules.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def login_instance_with_options(
        self,
        request: swas__open20200601_models.LoginInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.LoginInstanceResponse:
        """
        @summary Logs on to a simple application server on Workbench.
        
        @description After you create a simple application server, you can log on to the simple application server to build environments and applications on the server.
        
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
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
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
        @summary Logs on to a simple application server on Workbench.
        
        @description After you create a simple application server, you can log on to the simple application server to build environments and applications on the server.
        
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
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
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
        @summary Logs on to a simple application server on Workbench.
        
        @description After you create a simple application server, you can log on to the simple application server to build environments and applications on the server.
        
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
        @summary Logs on to a simple application server on Workbench.
        
        @description After you create a simple application server, you can log on to the simple application server to build environments and applications on the server.
        
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
        """
        @summary Modifies the description of a Simple Database Service instance.
        
        @description You can call this operation to modify the description of a Simple Database Service instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ModifyDatabaseInstanceDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseInstanceDescriptionResponse
        """
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
        """
        @summary Modifies the description of a Simple Database Service instance.
        
        @description You can call this operation to modify the description of a Simple Database Service instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ModifyDatabaseInstanceDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseInstanceDescriptionResponse
        """
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
        """
        @summary Modifies the description of a Simple Database Service instance.
        
        @description You can call this operation to modify the description of a Simple Database Service instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ModifyDatabaseInstanceDescriptionRequest
        @return: ModifyDatabaseInstanceDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_database_instance_description_with_options(request, runtime)

    async def modify_database_instance_description_async(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceDescriptionRequest,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceDescriptionResponse:
        """
        @summary Modifies the description of a Simple Database Service instance.
        
        @description You can call this operation to modify the description of a Simple Database Service instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ModifyDatabaseInstanceDescriptionRequest
        @return: ModifyDatabaseInstanceDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_instance_description_with_options_async(request, runtime)

    def modify_database_instance_parameter_with_options(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceParameterResponse:
        """
        @summary Modifies the parameters of a Simple Database Service instance.
        
        @description After you create a Simple Database Service instance, you can view the parameters of the instance or modify the parameters of the instance based on your business requirements.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ModifyDatabaseInstanceParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseInstanceParameterResponse
        """
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
        """
        @summary Modifies the parameters of a Simple Database Service instance.
        
        @description After you create a Simple Database Service instance, you can view the parameters of the instance or modify the parameters of the instance based on your business requirements.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ModifyDatabaseInstanceParameterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseInstanceParameterResponse
        """
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
        """
        @summary Modifies the parameters of a Simple Database Service instance.
        
        @description After you create a Simple Database Service instance, you can view the parameters of the instance or modify the parameters of the instance based on your business requirements.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ModifyDatabaseInstanceParameterRequest
        @return: ModifyDatabaseInstanceParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_database_instance_parameter_with_options(request, runtime)

    async def modify_database_instance_parameter_async(
        self,
        request: swas__open20200601_models.ModifyDatabaseInstanceParameterRequest,
    ) -> swas__open20200601_models.ModifyDatabaseInstanceParameterResponse:
        """
        @summary Modifies the parameters of a Simple Database Service instance.
        
        @description After you create a Simple Database Service instance, you can view the parameters of the instance or modify the parameters of the instance based on your business requirements.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ModifyDatabaseInstanceParameterRequest
        @return: ModifyDatabaseInstanceParameterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_instance_parameter_with_options_async(request, runtime)

    def modify_firewall_rule_with_options(
        self,
        request: swas__open20200601_models.ModifyFirewallRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyFirewallRuleResponse:
        """
        @summary Modifies the firewall rule of a simple application server.
        
        @param request: ModifyFirewallRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFirewallRuleResponse
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
        """
        @summary Modifies the firewall rule of a simple application server.
        
        @param request: ModifyFirewallRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFirewallRuleResponse
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
        """
        @summary Modifies the firewall rule of a simple application server.
        
        @param request: ModifyFirewallRuleRequest
        @return: ModifyFirewallRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_firewall_rule_with_options(request, runtime)

    async def modify_firewall_rule_async(
        self,
        request: swas__open20200601_models.ModifyFirewallRuleRequest,
    ) -> swas__open20200601_models.ModifyFirewallRuleResponse:
        """
        @summary Modifies the firewall rule of a simple application server.
        
        @param request: ModifyFirewallRuleRequest
        @return: ModifyFirewallRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_firewall_rule_with_options_async(request, runtime)

    def modify_firewall_template_with_options(
        self,
        request: swas__open20200601_models.ModifyFirewallTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyFirewallTemplateResponse:
        """
        @summary Modifies the firewall rule in a firewall template. You can apply the new firewall rule to simple application servers.
        
        @description Modifying a firewall template does not affect the firewall rules that have been applied to simple application servers.
        
        @param request: ModifyFirewallTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFirewallTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.firewall_template_rule):
            query['FirewallTemplateRule'] = request.firewall_template_rule
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFirewallTemplate',
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
            swas__open20200601_models.ModifyFirewallTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_firewall_template_with_options_async(
        self,
        request: swas__open20200601_models.ModifyFirewallTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyFirewallTemplateResponse:
        """
        @summary Modifies the firewall rule in a firewall template. You can apply the new firewall rule to simple application servers.
        
        @description Modifying a firewall template does not affect the firewall rules that have been applied to simple application servers.
        
        @param request: ModifyFirewallTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFirewallTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.firewall_template_id):
            query['FirewallTemplateId'] = request.firewall_template_id
        if not UtilClient.is_unset(request.firewall_template_rule):
            query['FirewallTemplateRule'] = request.firewall_template_rule
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFirewallTemplate',
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
            swas__open20200601_models.ModifyFirewallTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_firewall_template(
        self,
        request: swas__open20200601_models.ModifyFirewallTemplateRequest,
    ) -> swas__open20200601_models.ModifyFirewallTemplateResponse:
        """
        @summary Modifies the firewall rule in a firewall template. You can apply the new firewall rule to simple application servers.
        
        @description Modifying a firewall template does not affect the firewall rules that have been applied to simple application servers.
        
        @param request: ModifyFirewallTemplateRequest
        @return: ModifyFirewallTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_firewall_template_with_options(request, runtime)

    async def modify_firewall_template_async(
        self,
        request: swas__open20200601_models.ModifyFirewallTemplateRequest,
    ) -> swas__open20200601_models.ModifyFirewallTemplateResponse:
        """
        @summary Modifies the firewall rule in a firewall template. You can apply the new firewall rule to simple application servers.
        
        @description Modifying a firewall template does not affect the firewall rules that have been applied to simple application servers.
        
        @param request: ModifyFirewallTemplateRequest
        @return: ModifyFirewallTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_firewall_template_with_options_async(request, runtime)

    def modify_image_share_status_with_options(
        self,
        request: swas__open20200601_models.ModifyImageShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ModifyImageShareStatusResponse:
        """
        @summary Shares or unshares a custom image to Elastic Compute Service (ECS).
        
        @description You can share a custom image with ECS. If the configurations of your simple application server cannot meet your business requirements, or you want to use ECS instances to deploy your business, you can share your custom image with ECS to transfer your business from Simple Application Server to ECS.
        > The shared image in ECS resides in the same region as the custom image in Simple Application Server.
        You can unshare a custom image based on your business requirements or when you want to delete the custom image. Take note of the following items:
        After you unshare a custom image, you cannot query or use the custom image in the ECS console or by calling ECS API operations.
        After you unshare a custom image, you cannot re-initialize the disks of the ECS instances that were created based on the shared image.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Shares or unshares a custom image to Elastic Compute Service (ECS).
        
        @description You can share a custom image with ECS. If the configurations of your simple application server cannot meet your business requirements, or you want to use ECS instances to deploy your business, you can share your custom image with ECS to transfer your business from Simple Application Server to ECS.
        > The shared image in ECS resides in the same region as the custom image in Simple Application Server.
        You can unshare a custom image based on your business requirements or when you want to delete the custom image. Take note of the following items:
        After you unshare a custom image, you cannot query or use the custom image in the ECS console or by calling ECS API operations.
        After you unshare a custom image, you cannot re-initialize the disks of the ECS instances that were created based on the shared image.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Shares or unshares a custom image to Elastic Compute Service (ECS).
        
        @description You can share a custom image with ECS. If the configurations of your simple application server cannot meet your business requirements, or you want to use ECS instances to deploy your business, you can share your custom image with ECS to transfer your business from Simple Application Server to ECS.
        > The shared image in ECS resides in the same region as the custom image in Simple Application Server.
        You can unshare a custom image based on your business requirements or when you want to delete the custom image. Take note of the following items:
        After you unshare a custom image, you cannot query or use the custom image in the ECS console or by calling ECS API operations.
        After you unshare a custom image, you cannot re-initialize the disks of the ECS instances that were created based on the shared image.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Shares or unshares a custom image to Elastic Compute Service (ECS).
        
        @description You can share a custom image with ECS. If the configurations of your simple application server cannot meet your business requirements, or you want to use ECS instances to deploy your business, you can share your custom image with ECS to transfer your business from Simple Application Server to ECS.
        > The shared image in ECS resides in the same region as the custom image in Simple Application Server.
        You can unshare a custom image based on your business requirements or when you want to delete the custom image. Take note of the following items:
        After you unshare a custom image, you cannot query or use the custom image in the ECS console or by calling ECS API operations.
        After you unshare a custom image, you cannot re-initialize the disks of the ECS instances that were created based on the shared image.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        """
        @summary Changes the VNC password of a simple application server.
        
        @param request: ModifyInstanceVncPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceVncPasswordResponse
        """
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
        """
        @summary Changes the VNC password of a simple application server.
        
        @param request: ModifyInstanceVncPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceVncPasswordResponse
        """
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
        """
        @summary Changes the VNC password of a simple application server.
        
        @param request: ModifyInstanceVncPasswordRequest
        @return: ModifyInstanceVncPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vnc_password_with_options(request, runtime)

    async def modify_instance_vnc_password_async(
        self,
        request: swas__open20200601_models.ModifyInstanceVncPasswordRequest,
    ) -> swas__open20200601_models.ModifyInstanceVncPasswordResponse:
        """
        @summary Changes the VNC password of a simple application server.
        
        @param request: ModifyInstanceVncPasswordRequest
        @return: ModifyInstanceVncPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vnc_password_with_options_async(request, runtime)

    def reboot_instance_with_options(
        self,
        request: swas__open20200601_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RebootInstanceResponse:
        """
        @summary Restarts a simple application server.
        
        @description    Only simple application servers that are in the Running state can be restarted.
        After you restart a simple application server, it enters the Starting state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Restarts a simple application server.
        
        @description    Only simple application servers that are in the Running state can be restarted.
        After you restart a simple application server, it enters the Starting state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Restarts a simple application server.
        
        @description    Only simple application servers that are in the Running state can be restarted.
        After you restart a simple application server, it enters the Starting state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Restarts a simple application server.
        
        @description    Only simple application servers that are in the Running state can be restarted.
        After you restart a simple application server, it enters the Starting state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        """
        @summary Restarts simple application servers.
        
        @param request: RebootInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootInstancesResponse
        """
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
        """
        @summary Restarts simple application servers.
        
        @param request: RebootInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootInstancesResponse
        """
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
        """
        @summary Restarts simple application servers.
        
        @param request: RebootInstancesRequest
        @return: RebootInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reboot_instances_with_options(request, runtime)

    async def reboot_instances_async(
        self,
        request: swas__open20200601_models.RebootInstancesRequest,
    ) -> swas__open20200601_models.RebootInstancesResponse:
        """
        @summary Restarts simple application servers.
        
        @param request: RebootInstancesRequest
        @return: RebootInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reboot_instances_with_options_async(request, runtime)

    def release_public_connection_with_options(
        self,
        request: swas__open20200601_models.ReleasePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ReleasePublicConnectionResponse:
        """
        @summary Releases the public endpoint of a Simple Database Service instance.
        
        @description If you no longer need to use a public endpoint to access a Simple Database Service instance, you can release the public endpoint.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ReleasePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleasePublicConnectionResponse
        """
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
        """
        @summary Releases the public endpoint of a Simple Database Service instance.
        
        @description If you no longer need to use a public endpoint to access a Simple Database Service instance, you can release the public endpoint.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ReleasePublicConnectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleasePublicConnectionResponse
        """
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
        """
        @summary Releases the public endpoint of a Simple Database Service instance.
        
        @description If you no longer need to use a public endpoint to access a Simple Database Service instance, you can release the public endpoint.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ReleasePublicConnectionRequest
        @return: ReleasePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_public_connection_with_options(request, runtime)

    async def release_public_connection_async(
        self,
        request: swas__open20200601_models.ReleasePublicConnectionRequest,
    ) -> swas__open20200601_models.ReleasePublicConnectionResponse:
        """
        @summary Releases the public endpoint of a Simple Database Service instance.
        
        @description If you no longer need to use a public endpoint to access a Simple Database Service instance, you can release the public endpoint.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ReleasePublicConnectionRequest
        @return: ReleasePublicConnectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_public_connection_with_options_async(request, runtime)

    def remove_custom_image_share_account_with_options(
        self,
        request: swas__open20200601_models.RemoveCustomImageShareAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RemoveCustomImageShareAccountResponse:
        """
        @summary Unshares a custom image that is shared across Alibaba Cloud accounts.
        
        @param request: RemoveCustomImageShareAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveCustomImageShareAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
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
            action='RemoveCustomImageShareAccount',
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
            swas__open20200601_models.RemoveCustomImageShareAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_custom_image_share_account_with_options_async(
        self,
        request: swas__open20200601_models.RemoveCustomImageShareAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RemoveCustomImageShareAccountResponse:
        """
        @summary Unshares a custom image that is shared across Alibaba Cloud accounts.
        
        @param request: RemoveCustomImageShareAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveCustomImageShareAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
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
            action='RemoveCustomImageShareAccount',
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
            swas__open20200601_models.RemoveCustomImageShareAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_custom_image_share_account(
        self,
        request: swas__open20200601_models.RemoveCustomImageShareAccountRequest,
    ) -> swas__open20200601_models.RemoveCustomImageShareAccountResponse:
        """
        @summary Unshares a custom image that is shared across Alibaba Cloud accounts.
        
        @param request: RemoveCustomImageShareAccountRequest
        @return: RemoveCustomImageShareAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_custom_image_share_account_with_options(request, runtime)

    async def remove_custom_image_share_account_async(
        self,
        request: swas__open20200601_models.RemoveCustomImageShareAccountRequest,
    ) -> swas__open20200601_models.RemoveCustomImageShareAccountResponse:
        """
        @summary Unshares a custom image that is shared across Alibaba Cloud accounts.
        
        @param request: RemoveCustomImageShareAccountRequest
        @return: RemoveCustomImageShareAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_custom_image_share_account_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: swas__open20200601_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RenewInstanceResponse:
        """
        @summary Renews a simple application server.
        
        @description    Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](https://help.aliyun.com/document_detail/58623.html).
        When you call this operation to renew a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be renewed.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Renews a simple application server.
        
        @description    Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](https://help.aliyun.com/document_detail/58623.html).
        When you call this operation to renew a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be renewed.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Renews a simple application server.
        
        @description    Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](https://help.aliyun.com/document_detail/58623.html).
        When you call this operation to renew a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be renewed.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Renews a simple application server.
        
        @description    Before you call this operation, we recommend that you understand the billing of Simple Application Server. For more information, see [Billable items](https://help.aliyun.com/document_detail/58623.html).
        When you call this operation to renew a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be renewed.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        """
        @summary Resets the password of the administrator account of a Simple Database Service instance.
        
        @description If the password of your Simple Database Service instance is not strong, you can call this operation to change the password of the administrator account of the instance. To ensure security of the instance, we recommend that you regularly change the password of the instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ResetDatabaseAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetDatabaseAccountPasswordResponse
        """
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
        """
        @summary Resets the password of the administrator account of a Simple Database Service instance.
        
        @description If the password of your Simple Database Service instance is not strong, you can call this operation to change the password of the administrator account of the instance. To ensure security of the instance, we recommend that you regularly change the password of the instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ResetDatabaseAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetDatabaseAccountPasswordResponse
        """
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
        """
        @summary Resets the password of the administrator account of a Simple Database Service instance.
        
        @description If the password of your Simple Database Service instance is not strong, you can call this operation to change the password of the administrator account of the instance. To ensure security of the instance, we recommend that you regularly change the password of the instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ResetDatabaseAccountPasswordRequest
        @return: ResetDatabaseAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_database_account_password_with_options(request, runtime)

    async def reset_database_account_password_async(
        self,
        request: swas__open20200601_models.ResetDatabaseAccountPasswordRequest,
    ) -> swas__open20200601_models.ResetDatabaseAccountPasswordResponse:
        """
        @summary Resets the password of the administrator account of a Simple Database Service instance.
        
        @description If the password of your Simple Database Service instance is not strong, you can call this operation to change the password of the administrator account of the instance. To ensure security of the instance, we recommend that you regularly change the password of the instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: ResetDatabaseAccountPasswordRequest
        @return: ResetDatabaseAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_database_account_password_with_options_async(request, runtime)

    def reset_disk_with_options(
        self,
        request: swas__open20200601_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.ResetDiskResponse:
        """
        @summary Rolls back a disk based on a snapshot.
        
        @description    You can call this operation to roll back a disk only if the associated simple application server is in the Stopped state.
        After a disk is rolled back, all data changes that are made from when the snapshot was created to when the disk is rolled back are lost. Back up disk data based on your needs before you roll back the disk.
        ### Precautions
        After you reset a simple application server, the disk data on the server is deleted. Snapshots created before the resetting operation are retained but cannot be used to roll back the disks of the server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Rolls back a disk based on a snapshot.
        
        @description    You can call this operation to roll back a disk only if the associated simple application server is in the Stopped state.
        After a disk is rolled back, all data changes that are made from when the snapshot was created to when the disk is rolled back are lost. Back up disk data based on your needs before you roll back the disk.
        ### Precautions
        After you reset a simple application server, the disk data on the server is deleted. Snapshots created before the resetting operation are retained but cannot be used to roll back the disks of the server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Rolls back a disk based on a snapshot.
        
        @description    You can call this operation to roll back a disk only if the associated simple application server is in the Stopped state.
        After a disk is rolled back, all data changes that are made from when the snapshot was created to when the disk is rolled back are lost. Back up disk data based on your needs before you roll back the disk.
        ### Precautions
        After you reset a simple application server, the disk data on the server is deleted. Snapshots created before the resetting operation are retained but cannot be used to roll back the disks of the server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Rolls back a disk based on a snapshot.
        
        @description    You can call this operation to roll back a disk only if the associated simple application server is in the Stopped state.
        After a disk is rolled back, all data changes that are made from when the snapshot was created to when the disk is rolled back are lost. Back up disk data based on your needs before you roll back the disk.
        ### Precautions
        After you reset a simple application server, the disk data on the server is deleted. Snapshots created before the resetting operation are retained but cannot be used to roll back the disks of the server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Resets a simple application server.
        
        @description You can reset a simple application server to re-install its application system or OS and re-initialize the server. You can reset a simple application server by resetting the current system or replacing the image.
        You can use one of the following methods to reset a simple application server:
        Reset the current system. You can re-install the operating system without replacing the image.
        Replace the image. You can select an Alibaba Cloud image or a custom image that is different from the existing image of the server to reinstall the OS of the server.
        ### Precautions
        After you reset a simple application server, the disk data on the server is cleared. Back up the data as needed.
        After you reset a simple application server, the monitoring operations that are performed on the server may fail. In this case, you can use one of the following methods to install the CloudMonitor agent on the server:
        Connect to the server: For more information, see [Manually install the CloudMonitor agent for C++ on an ECS instance](https://help.aliyun.com/document_detail/183482.html).
        Use Command Assistant: For more information, see [Use Command Assistant](https://help.aliyun.com/document_detail/438681.html). You can obtain the command that can be used to install CloudMonitor from the "Common commands" section of the [Use Command Assistant](https://help.aliyun.com/document_detail/438681.html) topic.
        ### Limits
        Snapshots that are created before a server is reset are retained, but the snapshots cannot be used to roll back the disks of the server.
        You cannot reset simple application servers that were created based on custom images that contain data of data disks.
        Before you reset a simple application server by replacing the existing image with a custom image, take note of the following items:
        The custom image must reside in the same region as the current server.
        The custom image cannot be created based on the current server. If you want to recover the data on the server, you can use a snapshot of the server to roll back the disks of the server.
        If your simple application server resides outside the Chinese mainland, you cannot switch the OS of the server between Windows Server and Linux. You cannot use a Windows Server custom image to reset a Linux simple application server. You also cannot use a Linux custom image to reset a Windows Server simple application server. You can switch the OSs of simple application servers only between Windows Server OSs or between Linux distributions.
        The following limits apply to the disks attached to the simple application server:
        If the custom image contains a system disk and a data disk but only a system disk is attached to the simple application server and no data disk is attached, you cannot use the custom image to reset the simple application server.
        If the system disk size of the custom image is greater than the system disk size of the simple application server, you cannot directly use the custom image to reset the simple application server.
        Only if the system disk size of the simple application server is greater than or equal to the system disk size of the custom image, you can use the custom image to reset the simple application server. To increase the system disk size of your simple application server, you can upgrade the server. For more information, see Upgrade a simple application server.
        If the data disk size of the custom image is greater than the data disk size of the simple application server, you cannot use the custom image to reset the simple application server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Resets a simple application server.
        
        @description You can reset a simple application server to re-install its application system or OS and re-initialize the server. You can reset a simple application server by resetting the current system or replacing the image.
        You can use one of the following methods to reset a simple application server:
        Reset the current system. You can re-install the operating system without replacing the image.
        Replace the image. You can select an Alibaba Cloud image or a custom image that is different from the existing image of the server to reinstall the OS of the server.
        ### Precautions
        After you reset a simple application server, the disk data on the server is cleared. Back up the data as needed.
        After you reset a simple application server, the monitoring operations that are performed on the server may fail. In this case, you can use one of the following methods to install the CloudMonitor agent on the server:
        Connect to the server: For more information, see [Manually install the CloudMonitor agent for C++ on an ECS instance](https://help.aliyun.com/document_detail/183482.html).
        Use Command Assistant: For more information, see [Use Command Assistant](https://help.aliyun.com/document_detail/438681.html). You can obtain the command that can be used to install CloudMonitor from the "Common commands" section of the [Use Command Assistant](https://help.aliyun.com/document_detail/438681.html) topic.
        ### Limits
        Snapshots that are created before a server is reset are retained, but the snapshots cannot be used to roll back the disks of the server.
        You cannot reset simple application servers that were created based on custom images that contain data of data disks.
        Before you reset a simple application server by replacing the existing image with a custom image, take note of the following items:
        The custom image must reside in the same region as the current server.
        The custom image cannot be created based on the current server. If you want to recover the data on the server, you can use a snapshot of the server to roll back the disks of the server.
        If your simple application server resides outside the Chinese mainland, you cannot switch the OS of the server between Windows Server and Linux. You cannot use a Windows Server custom image to reset a Linux simple application server. You also cannot use a Linux custom image to reset a Windows Server simple application server. You can switch the OSs of simple application servers only between Windows Server OSs or between Linux distributions.
        The following limits apply to the disks attached to the simple application server:
        If the custom image contains a system disk and a data disk but only a system disk is attached to the simple application server and no data disk is attached, you cannot use the custom image to reset the simple application server.
        If the system disk size of the custom image is greater than the system disk size of the simple application server, you cannot directly use the custom image to reset the simple application server.
        Only if the system disk size of the simple application server is greater than or equal to the system disk size of the custom image, you can use the custom image to reset the simple application server. To increase the system disk size of your simple application server, you can upgrade the server. For more information, see Upgrade a simple application server.
        If the data disk size of the custom image is greater than the data disk size of the simple application server, you cannot use the custom image to reset the simple application server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Resets a simple application server.
        
        @description You can reset a simple application server to re-install its application system or OS and re-initialize the server. You can reset a simple application server by resetting the current system or replacing the image.
        You can use one of the following methods to reset a simple application server:
        Reset the current system. You can re-install the operating system without replacing the image.
        Replace the image. You can select an Alibaba Cloud image or a custom image that is different from the existing image of the server to reinstall the OS of the server.
        ### Precautions
        After you reset a simple application server, the disk data on the server is cleared. Back up the data as needed.
        After you reset a simple application server, the monitoring operations that are performed on the server may fail. In this case, you can use one of the following methods to install the CloudMonitor agent on the server:
        Connect to the server: For more information, see [Manually install the CloudMonitor agent for C++ on an ECS instance](https://help.aliyun.com/document_detail/183482.html).
        Use Command Assistant: For more information, see [Use Command Assistant](https://help.aliyun.com/document_detail/438681.html). You can obtain the command that can be used to install CloudMonitor from the "Common commands" section of the [Use Command Assistant](https://help.aliyun.com/document_detail/438681.html) topic.
        ### Limits
        Snapshots that are created before a server is reset are retained, but the snapshots cannot be used to roll back the disks of the server.
        You cannot reset simple application servers that were created based on custom images that contain data of data disks.
        Before you reset a simple application server by replacing the existing image with a custom image, take note of the following items:
        The custom image must reside in the same region as the current server.
        The custom image cannot be created based on the current server. If you want to recover the data on the server, you can use a snapshot of the server to roll back the disks of the server.
        If your simple application server resides outside the Chinese mainland, you cannot switch the OS of the server between Windows Server and Linux. You cannot use a Windows Server custom image to reset a Linux simple application server. You also cannot use a Linux custom image to reset a Windows Server simple application server. You can switch the OSs of simple application servers only between Windows Server OSs or between Linux distributions.
        The following limits apply to the disks attached to the simple application server:
        If the custom image contains a system disk and a data disk but only a system disk is attached to the simple application server and no data disk is attached, you cannot use the custom image to reset the simple application server.
        If the system disk size of the custom image is greater than the system disk size of the simple application server, you cannot directly use the custom image to reset the simple application server.
        Only if the system disk size of the simple application server is greater than or equal to the system disk size of the custom image, you can use the custom image to reset the simple application server. To increase the system disk size of your simple application server, you can upgrade the server. For more information, see Upgrade a simple application server.
        If the data disk size of the custom image is greater than the data disk size of the simple application server, you cannot use the custom image to reset the simple application server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Resets a simple application server.
        
        @description You can reset a simple application server to re-install its application system or OS and re-initialize the server. You can reset a simple application server by resetting the current system or replacing the image.
        You can use one of the following methods to reset a simple application server:
        Reset the current system. You can re-install the operating system without replacing the image.
        Replace the image. You can select an Alibaba Cloud image or a custom image that is different from the existing image of the server to reinstall the OS of the server.
        ### Precautions
        After you reset a simple application server, the disk data on the server is cleared. Back up the data as needed.
        After you reset a simple application server, the monitoring operations that are performed on the server may fail. In this case, you can use one of the following methods to install the CloudMonitor agent on the server:
        Connect to the server: For more information, see [Manually install the CloudMonitor agent for C++ on an ECS instance](https://help.aliyun.com/document_detail/183482.html).
        Use Command Assistant: For more information, see [Use Command Assistant](https://help.aliyun.com/document_detail/438681.html). You can obtain the command that can be used to install CloudMonitor from the "Common commands" section of the [Use Command Assistant](https://help.aliyun.com/document_detail/438681.html) topic.
        ### Limits
        Snapshots that are created before a server is reset are retained, but the snapshots cannot be used to roll back the disks of the server.
        You cannot reset simple application servers that were created based on custom images that contain data of data disks.
        Before you reset a simple application server by replacing the existing image with a custom image, take note of the following items:
        The custom image must reside in the same region as the current server.
        The custom image cannot be created based on the current server. If you want to recover the data on the server, you can use a snapshot of the server to roll back the disks of the server.
        If your simple application server resides outside the Chinese mainland, you cannot switch the OS of the server between Windows Server and Linux. You cannot use a Windows Server custom image to reset a Linux simple application server. You also cannot use a Linux custom image to reset a Windows Server simple application server. You can switch the OSs of simple application servers only between Windows Server OSs or between Linux distributions.
        The following limits apply to the disks attached to the simple application server:
        If the custom image contains a system disk and a data disk but only a system disk is attached to the simple application server and no data disk is attached, you cannot use the custom image to reset the simple application server.
        If the system disk size of the custom image is greater than the system disk size of the simple application server, you cannot directly use the custom image to reset the simple application server.
        Only if the system disk size of the simple application server is greater than or equal to the system disk size of the custom image, you can use the custom image to reset the simple application server. To increase the system disk size of your simple application server, you can upgrade the server. For more information, see Upgrade a simple application server.
        If the data disk size of the custom image is greater than the data disk size of the simple application server, you cannot use the custom image to reset the simple application server.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        """
        @summary Restarts a Simple Database Service instance.
        
        @description You can call this operation to restart a Simple Database Service instance that is in the Running state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: RestartDatabaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDatabaseInstanceResponse
        """
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
        """
        @summary Restarts a Simple Database Service instance.
        
        @description You can call this operation to restart a Simple Database Service instance that is in the Running state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: RestartDatabaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDatabaseInstanceResponse
        """
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
        """
        @summary Restarts a Simple Database Service instance.
        
        @description You can call this operation to restart a Simple Database Service instance that is in the Running state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: RestartDatabaseInstanceRequest
        @return: RestartDatabaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_database_instance_with_options(request, runtime)

    async def restart_database_instance_async(
        self,
        request: swas__open20200601_models.RestartDatabaseInstanceRequest,
    ) -> swas__open20200601_models.RestartDatabaseInstanceResponse:
        """
        @summary Restarts a Simple Database Service instance.
        
        @description You can call this operation to restart a Simple Database Service instance that is in the Running state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: RestartDatabaseInstanceRequest
        @return: RestartDatabaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_database_instance_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        tmp_req: swas__open20200601_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.RunCommandResponse:
        """
        @summary Runs commands on a simple application server.
        
        @description Command Assistant is an automated O\\&M tool for Simple Application Server. You can maintain simple application servers by running shell, PowerShell, and batch commands in the Simple Application Server console without remotely logging on to the servers.
        Before you use Command Assistant, take note of the following items:
        The simple application server must be in the Running state.
        The Cloud Assistant client is installed on the server. By default, the Cloud Assistant client is installed on simple application servers. If you have manually uninstalled the client, you must reinstall it. For more information, see [Install the Cloud Assistant Agent](https://help.aliyun.com/document_detail/64921.html).
        
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
        @summary Runs commands on a simple application server.
        
        @description Command Assistant is an automated O\\&M tool for Simple Application Server. You can maintain simple application servers by running shell, PowerShell, and batch commands in the Simple Application Server console without remotely logging on to the servers.
        Before you use Command Assistant, take note of the following items:
        The simple application server must be in the Running state.
        The Cloud Assistant client is installed on the server. By default, the Cloud Assistant client is installed on simple application servers. If you have manually uninstalled the client, you must reinstall it. For more information, see [Install the Cloud Assistant Agent](https://help.aliyun.com/document_detail/64921.html).
        
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
        @summary Runs commands on a simple application server.
        
        @description Command Assistant is an automated O\\&M tool for Simple Application Server. You can maintain simple application servers by running shell, PowerShell, and batch commands in the Simple Application Server console without remotely logging on to the servers.
        Before you use Command Assistant, take note of the following items:
        The simple application server must be in the Running state.
        The Cloud Assistant client is installed on the server. By default, the Cloud Assistant client is installed on simple application servers. If you have manually uninstalled the client, you must reinstall it. For more information, see [Install the Cloud Assistant Agent](https://help.aliyun.com/document_detail/64921.html).
        
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
        @summary Runs commands on a simple application server.
        
        @description Command Assistant is an automated O\\&M tool for Simple Application Server. You can maintain simple application servers by running shell, PowerShell, and batch commands in the Simple Application Server console without remotely logging on to the servers.
        Before you use Command Assistant, take note of the following items:
        The simple application server must be in the Running state.
        The Cloud Assistant client is installed on the server. By default, the Cloud Assistant client is installed on simple application servers. If you have manually uninstalled the client, you must reinstall it. For more information, see [Install the Cloud Assistant Agent](https://help.aliyun.com/document_detail/64921.html).
        
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
        """
        @summary Starts a Simple Database Service instance.
        
        @description You can call this operation to start a Simple Database Service instance that is in the Stopped state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: StartDatabaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDatabaseInstanceResponse
        """
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
        """
        @summary Starts a Simple Database Service instance.
        
        @description You can call this operation to start a Simple Database Service instance that is in the Stopped state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: StartDatabaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDatabaseInstanceResponse
        """
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
        """
        @summary Starts a Simple Database Service instance.
        
        @description You can call this operation to start a Simple Database Service instance that is in the Stopped state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: StartDatabaseInstanceRequest
        @return: StartDatabaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_database_instance_with_options(request, runtime)

    async def start_database_instance_async(
        self,
        request: swas__open20200601_models.StartDatabaseInstanceRequest,
    ) -> swas__open20200601_models.StartDatabaseInstanceResponse:
        """
        @summary Starts a Simple Database Service instance.
        
        @description You can call this operation to start a Simple Database Service instance that is in the Stopped state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: StartDatabaseInstanceRequest
        @return: StartDatabaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_database_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: swas__open20200601_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartInstanceResponse:
        """
        @summary Starts a simple application server.
        
        @description You can call this operation to start a simple application server that is in the Stopped state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Starts a simple application server.
        
        @description You can call this operation to start a simple application server that is in the Stopped state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Starts a simple application server.
        
        @description You can call this operation to start a simple application server that is in the Stopped state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Starts a simple application server.
        
        @description You can call this operation to start a simple application server that is in the Stopped state.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        """
        @summary Starts simple application servers.
        
        @param request: StartInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstancesResponse
        """
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
        """
        @summary Starts simple application servers.
        
        @param request: StartInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstancesResponse
        """
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
        """
        @summary Starts simple application servers.
        
        @param request: StartInstancesRequest
        @return: StartInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_instances_with_options(request, runtime)

    async def start_instances_async(
        self,
        request: swas__open20200601_models.StartInstancesRequest,
    ) -> swas__open20200601_models.StartInstancesResponse:
        """
        @summary Starts simple application servers.
        
        @param request: StartInstancesRequest
        @return: StartInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_instances_with_options_async(request, runtime)

    def start_terminal_session_with_options(
        self,
        request: swas__open20200601_models.StartTerminalSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StartTerminalSessionResponse:
        """
        @summary Creates a session for a simple application server.
        
        @param request: StartTerminalSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTerminalSessionResponse
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
        """
        @summary Creates a session for a simple application server.
        
        @param request: StartTerminalSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTerminalSessionResponse
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
        """
        @summary Creates a session for a simple application server.
        
        @param request: StartTerminalSessionRequest
        @return: StartTerminalSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_terminal_session_with_options(request, runtime)

    async def start_terminal_session_async(
        self,
        request: swas__open20200601_models.StartTerminalSessionRequest,
    ) -> swas__open20200601_models.StartTerminalSessionResponse:
        """
        @summary Creates a session for a simple application server.
        
        @param request: StartTerminalSessionRequest
        @return: StartTerminalSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_terminal_session_with_options_async(request, runtime)

    def stop_database_instance_with_options(
        self,
        request: swas__open20200601_models.StopDatabaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopDatabaseInstanceResponse:
        """
        @summary Stops a Simple Database Service instance.
        
        @description You can call this operation to stop a Simple Database Service instance that is in the Running state. After the instance is stopped, you cannot log on to or access the instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: StopDatabaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDatabaseInstanceResponse
        """
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
        """
        @summary Stops a Simple Database Service instance.
        
        @description You can call this operation to stop a Simple Database Service instance that is in the Running state. After the instance is stopped, you cannot log on to or access the instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: StopDatabaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDatabaseInstanceResponse
        """
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
        """
        @summary Stops a Simple Database Service instance.
        
        @description You can call this operation to stop a Simple Database Service instance that is in the Running state. After the instance is stopped, you cannot log on to or access the instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: StopDatabaseInstanceRequest
        @return: StopDatabaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_database_instance_with_options(request, runtime)

    async def stop_database_instance_async(
        self,
        request: swas__open20200601_models.StopDatabaseInstanceRequest,
    ) -> swas__open20200601_models.StopDatabaseInstanceResponse:
        """
        @summary Stops a Simple Database Service instance.
        
        @description You can call this operation to stop a Simple Database Service instance that is in the Running state. After the instance is stopped, you cannot log on to or access the instance.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
        @param request: StopDatabaseInstanceRequest
        @return: StopDatabaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_database_instance_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: swas__open20200601_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.StopInstanceResponse:
        """
        @summary Stops a simple application server.
        
        @description You can stop a simple application server that you do not use for the time being.
        >  Stopping a simple application server may interrupt your business. We recommend that you perform the stop operation during off-peak hours.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Stops a simple application server.
        
        @description You can stop a simple application server that you do not use for the time being.
        >  Stopping a simple application server may interrupt your business. We recommend that you perform the stop operation during off-peak hours.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Stops a simple application server.
        
        @description You can stop a simple application server that you do not use for the time being.
        >  Stopping a simple application server may interrupt your business. We recommend that you perform the stop operation during off-peak hours.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Stops a simple application server.
        
        @description You can stop a simple application server that you do not use for the time being.
        >  Stopping a simple application server may interrupt your business. We recommend that you perform the stop operation during off-peak hours.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        """
        @summary Stops simple application servers.
        
        @param request: StopInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstancesResponse
        """
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
        """
        @summary Stops simple application servers.
        
        @param request: StopInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstancesResponse
        """
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
        """
        @summary Stops simple application servers.
        
        @param request: StopInstancesRequest
        @return: StopInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_instances_with_options(request, runtime)

    async def stop_instances_async(
        self,
        request: swas__open20200601_models.StopInstancesRequest,
    ) -> swas__open20200601_models.StopInstancesResponse:
        """
        @summary Stops simple application servers.
        
        @param request: StopInstancesRequest
        @return: StopInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_instances_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: swas__open20200601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.TagResourcesResponse:
        """
        @summary Adds tags to simple application servers, snapshots, custom images, commands, firewall rules, and disks to facilitate the viewing and management of the preceding resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            swas__open20200601_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: swas__open20200601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.TagResourcesResponse:
        """
        @summary Adds tags to simple application servers, snapshots, custom images, commands, firewall rules, and disks to facilitate the viewing and management of the preceding resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            swas__open20200601_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: swas__open20200601_models.TagResourcesRequest,
    ) -> swas__open20200601_models.TagResourcesResponse:
        """
        @summary Adds tags to simple application servers, snapshots, custom images, commands, firewall rules, and disks to facilitate the viewing and management of the preceding resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: swas__open20200601_models.TagResourcesRequest,
    ) -> swas__open20200601_models.TagResourcesResponse:
        """
        @summary Adds tags to simple application servers, snapshots, custom images, commands, firewall rules, and disks to facilitate the viewing and management of the preceding resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: swas__open20200601_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UntagResourcesResponse:
        """
        @summary 删标签接口
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            swas__open20200601_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: swas__open20200601_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UntagResourcesResponse:
        """
        @summary 删标签接口
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            swas__open20200601_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: swas__open20200601_models.UntagResourcesRequest,
    ) -> swas__open20200601_models.UntagResourcesResponse:
        """
        @summary 删标签接口
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: swas__open20200601_models.UntagResourcesRequest,
    ) -> swas__open20200601_models.UntagResourcesResponse:
        """
        @summary 删标签接口
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_command_attribute_with_options(
        self,
        request: swas__open20200601_models.UpdateCommandAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateCommandAttributeResponse:
        """
        @summary Modifys the parameter of a command.
        
        @param request: UpdateCommandAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCommandAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCommandAttribute',
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
            swas__open20200601_models.UpdateCommandAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_command_attribute_with_options_async(
        self,
        request: swas__open20200601_models.UpdateCommandAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateCommandAttributeResponse:
        """
        @summary Modifys the parameter of a command.
        
        @param request: UpdateCommandAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCommandAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.working_dir):
            query['WorkingDir'] = request.working_dir
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCommandAttribute',
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
            swas__open20200601_models.UpdateCommandAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_command_attribute(
        self,
        request: swas__open20200601_models.UpdateCommandAttributeRequest,
    ) -> swas__open20200601_models.UpdateCommandAttributeResponse:
        """
        @summary Modifys the parameter of a command.
        
        @param request: UpdateCommandAttributeRequest
        @return: UpdateCommandAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_command_attribute_with_options(request, runtime)

    async def update_command_attribute_async(
        self,
        request: swas__open20200601_models.UpdateCommandAttributeRequest,
    ) -> swas__open20200601_models.UpdateCommandAttributeResponse:
        """
        @summary Modifys the parameter of a command.
        
        @param request: UpdateCommandAttributeRequest
        @return: UpdateCommandAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_command_attribute_with_options_async(request, runtime)

    def update_disk_attribute_with_options(
        self,
        request: swas__open20200601_models.UpdateDiskAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateDiskAttributeResponse:
        """
        @summary Modifies the remarks for the data disk that is attached to a simple application server.
        
        @param request: UpdateDiskAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDiskAttributeResponse
        """
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
        """
        @summary Modifies the remarks for the data disk that is attached to a simple application server.
        
        @param request: UpdateDiskAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDiskAttributeResponse
        """
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
        """
        @summary Modifies the remarks for the data disk that is attached to a simple application server.
        
        @param request: UpdateDiskAttributeRequest
        @return: UpdateDiskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_disk_attribute_with_options(request, runtime)

    async def update_disk_attribute_async(
        self,
        request: swas__open20200601_models.UpdateDiskAttributeRequest,
    ) -> swas__open20200601_models.UpdateDiskAttributeResponse:
        """
        @summary Modifies the remarks for the data disk that is attached to a simple application server.
        
        @param request: UpdateDiskAttributeRequest
        @return: UpdateDiskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_disk_attribute_with_options_async(request, runtime)

    def update_instance_attribute_with_options(
        self,
        request: swas__open20200601_models.UpdateInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpdateInstanceAttributeResponse:
        """
        @summary Modifies the information of a simple application server, including the server name and the password that you use to log on to the server.
        
        @description ## Usage notes
        After you change the password of a simple application server, you must restart the server by calling the [RebootInstance](https://help.aliyun.com/document_detail/190443.html) operation to allow the new password to take effect.
        ### QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Modifies the information of a simple application server, including the server name and the password that you use to log on to the server.
        
        @description ## Usage notes
        After you change the password of a simple application server, you must restart the server by calling the [RebootInstance](https://help.aliyun.com/document_detail/190443.html) operation to allow the new password to take effect.
        ### QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Modifies the information of a simple application server, including the server name and the password that you use to log on to the server.
        
        @description ## Usage notes
        After you change the password of a simple application server, you must restart the server by calling the [RebootInstance](https://help.aliyun.com/document_detail/190443.html) operation to allow the new password to take effect.
        ### QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Modifies the information of a simple application server, including the server name and the password that you use to log on to the server.
        
        @description ## Usage notes
        After you change the password of a simple application server, you must restart the server by calling the [RebootInstance](https://help.aliyun.com/document_detail/190443.html) operation to allow the new password to take effect.
        ### QPS limits
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        """
        @summary Modifies the remarks of a snapshot of a simple application server.
        
        @param request: UpdateSnapshotAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSnapshotAttributeResponse
        """
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
        """
        @summary Modifies the remarks of a snapshot of a simple application server.
        
        @param request: UpdateSnapshotAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSnapshotAttributeResponse
        """
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
        """
        @summary Modifies the remarks of a snapshot of a simple application server.
        
        @param request: UpdateSnapshotAttributeRequest
        @return: UpdateSnapshotAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_snapshot_attribute_with_options(request, runtime)

    async def update_snapshot_attribute_async(
        self,
        request: swas__open20200601_models.UpdateSnapshotAttributeRequest,
    ) -> swas__open20200601_models.UpdateSnapshotAttributeResponse:
        """
        @summary Modifies the remarks of a snapshot of a simple application server.
        
        @param request: UpdateSnapshotAttributeRequest
        @return: UpdateSnapshotAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_snapshot_attribute_with_options_async(request, runtime)

    def upgrade_instance_with_options(
        self,
        request: swas__open20200601_models.UpgradeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> swas__open20200601_models.UpgradeInstanceResponse:
        """
        @summary Upgrades the plan for a simple application server.
        
        @description    The plan of a simple application server cannot be downgraded, but can only be upgraded. For more information about plans, see [Billable items](https://help.aliyun.com/document_detail/58623.html).
        When you call this operation to upgrade a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be upgraded.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Upgrades the plan for a simple application server.
        
        @description    The plan of a simple application server cannot be downgraded, but can only be upgraded. For more information about plans, see [Billable items](https://help.aliyun.com/document_detail/58623.html).
        When you call this operation to upgrade a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be upgraded.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Upgrades the plan for a simple application server.
        
        @description    The plan of a simple application server cannot be downgraded, but can only be upgraded. For more information about plans, see [Billable items](https://help.aliyun.com/document_detail/58623.html).
        When you call this operation to upgrade a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be upgraded.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        @summary Upgrades the plan for a simple application server.
        
        @description    The plan of a simple application server cannot be downgraded, but can only be upgraded. For more information about plans, see [Billable items](https://help.aliyun.com/document_detail/58623.html).
        When you call this operation to upgrade a server, make sure that the balance in your account is sufficient. If the balance in your account is insufficient, the server cannot be upgraded.
        ### QPS limit
        You can call this API operation up to 10 times per minute per account. Requests that exceed this limit are dropped and you may experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/347607.html).
        
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
        """
        @summary Imports a key pair for a simple application server.
        
        @param request: UploadInstanceKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadInstanceKeyPairResponse
        """
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
        """
        @summary Imports a key pair for a simple application server.
        
        @param request: UploadInstanceKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadInstanceKeyPairResponse
        """
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
        """
        @summary Imports a key pair for a simple application server.
        
        @param request: UploadInstanceKeyPairRequest
        @return: UploadInstanceKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_instance_key_pair_with_options(request, runtime)

    async def upload_instance_key_pair_async(
        self,
        request: swas__open20200601_models.UploadInstanceKeyPairRequest,
    ) -> swas__open20200601_models.UploadInstanceKeyPairResponse:
        """
        @summary Imports a key pair for a simple application server.
        
        @param request: UploadInstanceKeyPairRequest
        @return: UploadInstanceKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_instance_key_pair_with_options_async(request, runtime)
