# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alb20200616 import models as alb_20200616_models
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
        self._endpoint = self.get_endpoint('alb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_entries_to_acl_with_options(
        self,
        request: alb_20200616_models.AddEntriesToAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AddEntriesToAclResponse:
        """
        @summary Adds IP entries to an access control list (ACL).
        
        @description    Each ACL can contain IP addresses or CIDR blocks. Take note of the following limits on ACLs:
        The maximum number of IP entries that can be added to an ACL with each Alibaba Cloud account at a time: 20
        The maximum number of IP entries that each ACL can contain: 1,000
        **AddEntriesToAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclEntries](https://help.aliyun.com/document_detail/213616.html) operation to query the status of the task.
        If the ACL is in the **Adding** state, the IP entries are being added.
        If the ACL is in the **Available** state, the IP entries are added.
        
        @param request: AddEntriesToAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddEntriesToAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entries):
            query['AclEntries'] = request.acl_entries
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEntriesToAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AddEntriesToAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_entries_to_acl_with_options_async(
        self,
        request: alb_20200616_models.AddEntriesToAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AddEntriesToAclResponse:
        """
        @summary Adds IP entries to an access control list (ACL).
        
        @description    Each ACL can contain IP addresses or CIDR blocks. Take note of the following limits on ACLs:
        The maximum number of IP entries that can be added to an ACL with each Alibaba Cloud account at a time: 20
        The maximum number of IP entries that each ACL can contain: 1,000
        **AddEntriesToAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclEntries](https://help.aliyun.com/document_detail/213616.html) operation to query the status of the task.
        If the ACL is in the **Adding** state, the IP entries are being added.
        If the ACL is in the **Available** state, the IP entries are added.
        
        @param request: AddEntriesToAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddEntriesToAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entries):
            query['AclEntries'] = request.acl_entries
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEntriesToAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AddEntriesToAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_entries_to_acl(
        self,
        request: alb_20200616_models.AddEntriesToAclRequest,
    ) -> alb_20200616_models.AddEntriesToAclResponse:
        """
        @summary Adds IP entries to an access control list (ACL).
        
        @description    Each ACL can contain IP addresses or CIDR blocks. Take note of the following limits on ACLs:
        The maximum number of IP entries that can be added to an ACL with each Alibaba Cloud account at a time: 20
        The maximum number of IP entries that each ACL can contain: 1,000
        **AddEntriesToAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclEntries](https://help.aliyun.com/document_detail/213616.html) operation to query the status of the task.
        If the ACL is in the **Adding** state, the IP entries are being added.
        If the ACL is in the **Available** state, the IP entries are added.
        
        @param request: AddEntriesToAclRequest
        @return: AddEntriesToAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_entries_to_acl_with_options(request, runtime)

    async def add_entries_to_acl_async(
        self,
        request: alb_20200616_models.AddEntriesToAclRequest,
    ) -> alb_20200616_models.AddEntriesToAclResponse:
        """
        @summary Adds IP entries to an access control list (ACL).
        
        @description    Each ACL can contain IP addresses or CIDR blocks. Take note of the following limits on ACLs:
        The maximum number of IP entries that can be added to an ACL with each Alibaba Cloud account at a time: 20
        The maximum number of IP entries that each ACL can contain: 1,000
        **AddEntriesToAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclEntries](https://help.aliyun.com/document_detail/213616.html) operation to query the status of the task.
        If the ACL is in the **Adding** state, the IP entries are being added.
        If the ACL is in the **Available** state, the IP entries are added.
        
        @param request: AddEntriesToAclRequest
        @return: AddEntriesToAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_entries_to_acl_with_options_async(request, runtime)

    def add_servers_to_server_group_with_options(
        self,
        request: alb_20200616_models.AddServersToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AddServersToServerGroupResponse:
        """
        @summary Adds backend servers to a server group.
        
        @description *AddServersToServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Adding** state, it indicates that the backend server is being added to a server group.
        If a backend server is in the **Available** state, it indicates that the server is running.
        
        @param request: AddServersToServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddServersToServerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            query['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddServersToServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AddServersToServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_servers_to_server_group_with_options_async(
        self,
        request: alb_20200616_models.AddServersToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AddServersToServerGroupResponse:
        """
        @summary Adds backend servers to a server group.
        
        @description *AddServersToServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Adding** state, it indicates that the backend server is being added to a server group.
        If a backend server is in the **Available** state, it indicates that the server is running.
        
        @param request: AddServersToServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddServersToServerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            query['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddServersToServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AddServersToServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_servers_to_server_group(
        self,
        request: alb_20200616_models.AddServersToServerGroupRequest,
    ) -> alb_20200616_models.AddServersToServerGroupResponse:
        """
        @summary Adds backend servers to a server group.
        
        @description *AddServersToServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Adding** state, it indicates that the backend server is being added to a server group.
        If a backend server is in the **Available** state, it indicates that the server is running.
        
        @param request: AddServersToServerGroupRequest
        @return: AddServersToServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_servers_to_server_group_with_options(request, runtime)

    async def add_servers_to_server_group_async(
        self,
        request: alb_20200616_models.AddServersToServerGroupRequest,
    ) -> alb_20200616_models.AddServersToServerGroupResponse:
        """
        @summary Adds backend servers to a server group.
        
        @description *AddServersToServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Adding** state, it indicates that the backend server is being added to a server group.
        If a backend server is in the **Available** state, it indicates that the server is running.
        
        @param request: AddServersToServerGroupRequest
        @return: AddServersToServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_servers_to_server_group_with_options_async(request, runtime)

    def apply_health_check_template_to_server_group_with_options(
        self,
        request: alb_20200616_models.ApplyHealthCheckTemplateToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse:
        """
        @summary Applies a health check template to a server group.
        
        @param request: ApplyHealthCheckTemplateToServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyHealthCheckTemplateToServerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyHealthCheckTemplateToServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_health_check_template_to_server_group_with_options_async(
        self,
        request: alb_20200616_models.ApplyHealthCheckTemplateToServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse:
        """
        @summary Applies a health check template to a server group.
        
        @param request: ApplyHealthCheckTemplateToServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyHealthCheckTemplateToServerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyHealthCheckTemplateToServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_health_check_template_to_server_group(
        self,
        request: alb_20200616_models.ApplyHealthCheckTemplateToServerGroupRequest,
    ) -> alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse:
        """
        @summary Applies a health check template to a server group.
        
        @param request: ApplyHealthCheckTemplateToServerGroupRequest
        @return: ApplyHealthCheckTemplateToServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_health_check_template_to_server_group_with_options(request, runtime)

    async def apply_health_check_template_to_server_group_async(
        self,
        request: alb_20200616_models.ApplyHealthCheckTemplateToServerGroupRequest,
    ) -> alb_20200616_models.ApplyHealthCheckTemplateToServerGroupResponse:
        """
        @summary Applies a health check template to a server group.
        
        @param request: ApplyHealthCheckTemplateToServerGroupRequest
        @return: ApplyHealthCheckTemplateToServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_health_check_template_to_server_group_with_options_async(request, runtime)

    def associate_acls_with_listener_with_options(
        self,
        request: alb_20200616_models.AssociateAclsWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AssociateAclsWithListenerResponse:
        """
        @summary Associates access control lists (ACLs) with a listener.
        
        @description *DeleteDhcpOptionsSet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclRelations](https://help.aliyun.com/document_detail/213618.html) operation to query the status of the task.
        If an ACL is in the **Associating** state, the ACL is being associated with a listener.
        If an ACL is in the **Associated** state, the ACL is associated with a listener.
        
        @param request: AssociateAclsWithListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateAclsWithListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateAclsWithListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AssociateAclsWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_acls_with_listener_with_options_async(
        self,
        request: alb_20200616_models.AssociateAclsWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AssociateAclsWithListenerResponse:
        """
        @summary Associates access control lists (ACLs) with a listener.
        
        @description *DeleteDhcpOptionsSet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclRelations](https://help.aliyun.com/document_detail/213618.html) operation to query the status of the task.
        If an ACL is in the **Associating** state, the ACL is being associated with a listener.
        If an ACL is in the **Associated** state, the ACL is associated with a listener.
        
        @param request: AssociateAclsWithListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateAclsWithListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateAclsWithListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AssociateAclsWithListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_acls_with_listener(
        self,
        request: alb_20200616_models.AssociateAclsWithListenerRequest,
    ) -> alb_20200616_models.AssociateAclsWithListenerResponse:
        """
        @summary Associates access control lists (ACLs) with a listener.
        
        @description *DeleteDhcpOptionsSet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclRelations](https://help.aliyun.com/document_detail/213618.html) operation to query the status of the task.
        If an ACL is in the **Associating** state, the ACL is being associated with a listener.
        If an ACL is in the **Associated** state, the ACL is associated with a listener.
        
        @param request: AssociateAclsWithListenerRequest
        @return: AssociateAclsWithListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_acls_with_listener_with_options(request, runtime)

    async def associate_acls_with_listener_async(
        self,
        request: alb_20200616_models.AssociateAclsWithListenerRequest,
    ) -> alb_20200616_models.AssociateAclsWithListenerResponse:
        """
        @summary Associates access control lists (ACLs) with a listener.
        
        @description *DeleteDhcpOptionsSet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclRelations](https://help.aliyun.com/document_detail/213618.html) operation to query the status of the task.
        If an ACL is in the **Associating** state, the ACL is being associated with a listener.
        If an ACL is in the **Associated** state, the ACL is associated with a listener.
        
        @param request: AssociateAclsWithListenerRequest
        @return: AssociateAclsWithListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_acls_with_listener_with_options_async(request, runtime)

    def associate_additional_certificates_with_listener_with_options(
        self,
        request: alb_20200616_models.AssociateAdditionalCertificatesWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse:
        """
        @summary Associates additional certificates with a listener.
        
        @description *AssociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) operation to query the status of the task:
        If the HTTPS or QUIC listener is in the **Associating** state, the additional certificates are being associated.
        If the HTTPS or QUIC listener is in the **Associated** state, the additional certificates are associated.
        
        @param request: AssociateAdditionalCertificatesWithListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateAdditionalCertificatesWithListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateAdditionalCertificatesWithListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_additional_certificates_with_listener_with_options_async(
        self,
        request: alb_20200616_models.AssociateAdditionalCertificatesWithListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse:
        """
        @summary Associates additional certificates with a listener.
        
        @description *AssociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) operation to query the status of the task:
        If the HTTPS or QUIC listener is in the **Associating** state, the additional certificates are being associated.
        If the HTTPS or QUIC listener is in the **Associated** state, the additional certificates are associated.
        
        @param request: AssociateAdditionalCertificatesWithListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateAdditionalCertificatesWithListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateAdditionalCertificatesWithListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_additional_certificates_with_listener(
        self,
        request: alb_20200616_models.AssociateAdditionalCertificatesWithListenerRequest,
    ) -> alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse:
        """
        @summary Associates additional certificates with a listener.
        
        @description *AssociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) operation to query the status of the task:
        If the HTTPS or QUIC listener is in the **Associating** state, the additional certificates are being associated.
        If the HTTPS or QUIC listener is in the **Associated** state, the additional certificates are associated.
        
        @param request: AssociateAdditionalCertificatesWithListenerRequest
        @return: AssociateAdditionalCertificatesWithListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_additional_certificates_with_listener_with_options(request, runtime)

    async def associate_additional_certificates_with_listener_async(
        self,
        request: alb_20200616_models.AssociateAdditionalCertificatesWithListenerRequest,
    ) -> alb_20200616_models.AssociateAdditionalCertificatesWithListenerResponse:
        """
        @summary Associates additional certificates with a listener.
        
        @description *AssociateAdditionalCertificatesWithListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) operation to query the status of the task:
        If the HTTPS or QUIC listener is in the **Associating** state, the additional certificates are being associated.
        If the HTTPS or QUIC listener is in the **Associated** state, the additional certificates are associated.
        
        @param request: AssociateAdditionalCertificatesWithListenerRequest
        @return: AssociateAdditionalCertificatesWithListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_additional_certificates_with_listener_with_options_async(request, runtime)

    def attach_common_bandwidth_package_to_load_balancer_with_options(
        self,
        request: alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        """
        @summary Associates an EIP bandwidth plan with an Application Load Balancer (ALB) instance.
        
        @description *AttachCommonBandwidthPackageToLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If the ALB instance is in the **Configuring** state, the EIP bandwidth plan is being associated with the ALB instance.
        If the ALB instance is in the **Active** state, the EIP bandwidth plan is associated with the ALB instance.
        
        @param request: AttachCommonBandwidthPackageToLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachCommonBandwidthPackageToLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachCommonBandwidthPackageToLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_common_bandwidth_package_to_load_balancer_with_options_async(
        self,
        request: alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        """
        @summary Associates an EIP bandwidth plan with an Application Load Balancer (ALB) instance.
        
        @description *AttachCommonBandwidthPackageToLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If the ALB instance is in the **Configuring** state, the EIP bandwidth plan is being associated with the ALB instance.
        If the ALB instance is in the **Active** state, the EIP bandwidth plan is associated with the ALB instance.
        
        @param request: AttachCommonBandwidthPackageToLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachCommonBandwidthPackageToLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachCommonBandwidthPackageToLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_common_bandwidth_package_to_load_balancer(
        self,
        request: alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
    ) -> alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        """
        @summary Associates an EIP bandwidth plan with an Application Load Balancer (ALB) instance.
        
        @description *AttachCommonBandwidthPackageToLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If the ALB instance is in the **Configuring** state, the EIP bandwidth plan is being associated with the ALB instance.
        If the ALB instance is in the **Active** state, the EIP bandwidth plan is associated with the ALB instance.
        
        @param request: AttachCommonBandwidthPackageToLoadBalancerRequest
        @return: AttachCommonBandwidthPackageToLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_common_bandwidth_package_to_load_balancer_with_options(request, runtime)

    async def attach_common_bandwidth_package_to_load_balancer_async(
        self,
        request: alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerRequest,
    ) -> alb_20200616_models.AttachCommonBandwidthPackageToLoadBalancerResponse:
        """
        @summary Associates an EIP bandwidth plan with an Application Load Balancer (ALB) instance.
        
        @description *AttachCommonBandwidthPackageToLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If the ALB instance is in the **Configuring** state, the EIP bandwidth plan is being associated with the ALB instance.
        If the ALB instance is in the **Active** state, the EIP bandwidth plan is associated with the ALB instance.
        
        @param request: AttachCommonBandwidthPackageToLoadBalancerRequest
        @return: AttachCommonBandwidthPackageToLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_common_bandwidth_package_to_load_balancer_with_options_async(request, runtime)

    def cancel_shift_load_balancer_zones_with_options(
        self,
        request: alb_20200616_models.CancelShiftLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CancelShiftLoadBalancerZonesResponse:
        """
        @summary Adds the elastic IP address (EIP) and virtual IP address (VIP) of a zone to a DNS record.
        
        @description This operation is supported only by Application Load Balancer (ALB) instances that use static IP addresses. Before you call this operation, you must call the StartShiftLoadBalancerZones operation to remove the zone from the ALB instance.
        
        @param request: CancelShiftLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelShiftLoadBalancerZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelShiftLoadBalancerZones',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CancelShiftLoadBalancerZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_shift_load_balancer_zones_with_options_async(
        self,
        request: alb_20200616_models.CancelShiftLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CancelShiftLoadBalancerZonesResponse:
        """
        @summary Adds the elastic IP address (EIP) and virtual IP address (VIP) of a zone to a DNS record.
        
        @description This operation is supported only by Application Load Balancer (ALB) instances that use static IP addresses. Before you call this operation, you must call the StartShiftLoadBalancerZones operation to remove the zone from the ALB instance.
        
        @param request: CancelShiftLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelShiftLoadBalancerZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelShiftLoadBalancerZones',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CancelShiftLoadBalancerZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_shift_load_balancer_zones(
        self,
        request: alb_20200616_models.CancelShiftLoadBalancerZonesRequest,
    ) -> alb_20200616_models.CancelShiftLoadBalancerZonesResponse:
        """
        @summary Adds the elastic IP address (EIP) and virtual IP address (VIP) of a zone to a DNS record.
        
        @description This operation is supported only by Application Load Balancer (ALB) instances that use static IP addresses. Before you call this operation, you must call the StartShiftLoadBalancerZones operation to remove the zone from the ALB instance.
        
        @param request: CancelShiftLoadBalancerZonesRequest
        @return: CancelShiftLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_shift_load_balancer_zones_with_options(request, runtime)

    async def cancel_shift_load_balancer_zones_async(
        self,
        request: alb_20200616_models.CancelShiftLoadBalancerZonesRequest,
    ) -> alb_20200616_models.CancelShiftLoadBalancerZonesResponse:
        """
        @summary Adds the elastic IP address (EIP) and virtual IP address (VIP) of a zone to a DNS record.
        
        @description This operation is supported only by Application Load Balancer (ALB) instances that use static IP addresses. Before you call this operation, you must call the StartShiftLoadBalancerZones operation to remove the zone from the ALB instance.
        
        @param request: CancelShiftLoadBalancerZonesRequest
        @return: CancelShiftLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_shift_load_balancer_zones_with_options_async(request, runtime)

    def create_ascripts_with_options(
        self,
        request: alb_20200616_models.CreateAScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateAScriptsResponse:
        """
        @summary Creates AScript rules.
        
        @description ### Prerequisites
        A standard or WAF-enabled Application Load Balancer (ALB) instance is created. For more information, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html).
        By default, the feature to create and manage AScript rules is unavailable. Log on to the [Quota Center console](https://quotas.console.aliyun.com/white-list-products/alb/quotas?spm=a2c4g.11186623.0.0.6e8834f6IFiF2I). On the **Privileges** page, enter the quota ID `slb_user_visible_gray_label/ascript` and apply for the quota.
        ### Usage notes
        **CreateAScripts** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAScripts](https://help.aliyun.com/document_detail/472574.html) operation to query the status of the task:
        If an AScript rule is in the **Creating** state, the AScript rule is being created.
        If an AScript rule is in the **Available** state, the AScript rule is created.
        In the following table, the value of **N** is **1**.
        
        @param request: CreateAScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAScriptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascripts):
            query['AScripts'] = request.ascripts
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAScripts',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateAScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ascripts_with_options_async(
        self,
        request: alb_20200616_models.CreateAScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateAScriptsResponse:
        """
        @summary Creates AScript rules.
        
        @description ### Prerequisites
        A standard or WAF-enabled Application Load Balancer (ALB) instance is created. For more information, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html).
        By default, the feature to create and manage AScript rules is unavailable. Log on to the [Quota Center console](https://quotas.console.aliyun.com/white-list-products/alb/quotas?spm=a2c4g.11186623.0.0.6e8834f6IFiF2I). On the **Privileges** page, enter the quota ID `slb_user_visible_gray_label/ascript` and apply for the quota.
        ### Usage notes
        **CreateAScripts** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAScripts](https://help.aliyun.com/document_detail/472574.html) operation to query the status of the task:
        If an AScript rule is in the **Creating** state, the AScript rule is being created.
        If an AScript rule is in the **Available** state, the AScript rule is created.
        In the following table, the value of **N** is **1**.
        
        @param request: CreateAScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAScriptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascripts):
            query['AScripts'] = request.ascripts
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAScripts',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateAScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ascripts(
        self,
        request: alb_20200616_models.CreateAScriptsRequest,
    ) -> alb_20200616_models.CreateAScriptsResponse:
        """
        @summary Creates AScript rules.
        
        @description ### Prerequisites
        A standard or WAF-enabled Application Load Balancer (ALB) instance is created. For more information, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html).
        By default, the feature to create and manage AScript rules is unavailable. Log on to the [Quota Center console](https://quotas.console.aliyun.com/white-list-products/alb/quotas?spm=a2c4g.11186623.0.0.6e8834f6IFiF2I). On the **Privileges** page, enter the quota ID `slb_user_visible_gray_label/ascript` and apply for the quota.
        ### Usage notes
        **CreateAScripts** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAScripts](https://help.aliyun.com/document_detail/472574.html) operation to query the status of the task:
        If an AScript rule is in the **Creating** state, the AScript rule is being created.
        If an AScript rule is in the **Available** state, the AScript rule is created.
        In the following table, the value of **N** is **1**.
        
        @param request: CreateAScriptsRequest
        @return: CreateAScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ascripts_with_options(request, runtime)

    async def create_ascripts_async(
        self,
        request: alb_20200616_models.CreateAScriptsRequest,
    ) -> alb_20200616_models.CreateAScriptsResponse:
        """
        @summary Creates AScript rules.
        
        @description ### Prerequisites
        A standard or WAF-enabled Application Load Balancer (ALB) instance is created. For more information, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html).
        By default, the feature to create and manage AScript rules is unavailable. Log on to the [Quota Center console](https://quotas.console.aliyun.com/white-list-products/alb/quotas?spm=a2c4g.11186623.0.0.6e8834f6IFiF2I). On the **Privileges** page, enter the quota ID `slb_user_visible_gray_label/ascript` and apply for the quota.
        ### Usage notes
        **CreateAScripts** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAScripts](https://help.aliyun.com/document_detail/472574.html) operation to query the status of the task:
        If an AScript rule is in the **Creating** state, the AScript rule is being created.
        If an AScript rule is in the **Available** state, the AScript rule is created.
        In the following table, the value of **N** is **1**.
        
        @param request: CreateAScriptsRequest
        @return: CreateAScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ascripts_with_options_async(request, runtime)

    def create_acl_with_options(
        self,
        request: alb_20200616_models.CreateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateAclResponse:
        """
        @summary Creates an access control list (ACL) in a region.
        
        @description ## Usage notes
        The *CreateAcl** operation is asynchronous. After you send a request, the system returns a request ID. However, the operation is still being performed in the system background. You can call the [ListAcls](https://help.aliyun.com/document_detail/213617.html) operation to query the status of an ACL:
        If an ACL is in the **Creating** state, the ACL is being created.
        If an ACL is in the **Available** state, the ACL is created.
        
        @param request: CreateAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_acl_with_options_async(
        self,
        request: alb_20200616_models.CreateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateAclResponse:
        """
        @summary Creates an access control list (ACL) in a region.
        
        @description ## Usage notes
        The *CreateAcl** operation is asynchronous. After you send a request, the system returns a request ID. However, the operation is still being performed in the system background. You can call the [ListAcls](https://help.aliyun.com/document_detail/213617.html) operation to query the status of an ACL:
        If an ACL is in the **Creating** state, the ACL is being created.
        If an ACL is in the **Available** state, the ACL is created.
        
        @param request: CreateAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_acl(
        self,
        request: alb_20200616_models.CreateAclRequest,
    ) -> alb_20200616_models.CreateAclResponse:
        """
        @summary Creates an access control list (ACL) in a region.
        
        @description ## Usage notes
        The *CreateAcl** operation is asynchronous. After you send a request, the system returns a request ID. However, the operation is still being performed in the system background. You can call the [ListAcls](https://help.aliyun.com/document_detail/213617.html) operation to query the status of an ACL:
        If an ACL is in the **Creating** state, the ACL is being created.
        If an ACL is in the **Available** state, the ACL is created.
        
        @param request: CreateAclRequest
        @return: CreateAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    async def create_acl_async(
        self,
        request: alb_20200616_models.CreateAclRequest,
    ) -> alb_20200616_models.CreateAclResponse:
        """
        @summary Creates an access control list (ACL) in a region.
        
        @description ## Usage notes
        The *CreateAcl** operation is asynchronous. After you send a request, the system returns a request ID. However, the operation is still being performed in the system background. You can call the [ListAcls](https://help.aliyun.com/document_detail/213617.html) operation to query the status of an ACL:
        If an ACL is in the **Creating** state, the ACL is being created.
        If an ACL is in the **Available** state, the ACL is created.
        
        @param request: CreateAclRequest
        @return: CreateAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_acl_with_options_async(request, runtime)

    def create_health_check_template_with_options(
        self,
        request: alb_20200616_models.CreateHealthCheckTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateHealthCheckTemplateResponse:
        """
        @summary Creates a health check template in a region.
        
        @param request: CreateHealthCheckTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHealthCheckTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_codes):
            query['HealthCheckCodes'] = request.health_check_codes
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not UtilClient.is_unset(request.health_check_http_version):
            query['HealthCheckHttpVersion'] = request.health_check_http_version
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not UtilClient.is_unset(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not UtilClient.is_unset(request.health_check_template_name):
            query['HealthCheckTemplateName'] = request.health_check_template_name
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHealthCheckTemplate',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateHealthCheckTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_health_check_template_with_options_async(
        self,
        request: alb_20200616_models.CreateHealthCheckTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateHealthCheckTemplateResponse:
        """
        @summary Creates a health check template in a region.
        
        @param request: CreateHealthCheckTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHealthCheckTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_codes):
            query['HealthCheckCodes'] = request.health_check_codes
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not UtilClient.is_unset(request.health_check_http_version):
            query['HealthCheckHttpVersion'] = request.health_check_http_version
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not UtilClient.is_unset(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not UtilClient.is_unset(request.health_check_template_name):
            query['HealthCheckTemplateName'] = request.health_check_template_name
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHealthCheckTemplate',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateHealthCheckTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_health_check_template(
        self,
        request: alb_20200616_models.CreateHealthCheckTemplateRequest,
    ) -> alb_20200616_models.CreateHealthCheckTemplateResponse:
        """
        @summary Creates a health check template in a region.
        
        @param request: CreateHealthCheckTemplateRequest
        @return: CreateHealthCheckTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_health_check_template_with_options(request, runtime)

    async def create_health_check_template_async(
        self,
        request: alb_20200616_models.CreateHealthCheckTemplateRequest,
    ) -> alb_20200616_models.CreateHealthCheckTemplateResponse:
        """
        @summary Creates a health check template in a region.
        
        @param request: CreateHealthCheckTemplateRequest
        @return: CreateHealthCheckTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_health_check_template_with_options_async(request, runtime)

    def create_listener_with_options(
        self,
        request: alb_20200616_models.CreateListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateListenerResponse:
        """
        @summary Creates an HTTP, HTTPS, or QUIC listener in a region.
        
        @description ## Usage notes
        *CreateListener** is an asynchronous operation. After you call this operation, the system returns a request ID. However, the operation is still being performed in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/214353.html) operation to query the status of the HTTP, HTTPS, or QUIC listener.
        If the HTTP, HTTPS, or QUIC listener is in the **Provisioning** state, it indicates that the listener is being created.
        If the HTTP, HTTPS, or QUIC listener is in the **Running** state, it indicates that the listener has been created successfully.
        
        @param request: CreateListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_certificates):
            query['CaCertificates'] = request.ca_certificates
        if not UtilClient.is_unset(request.ca_enabled):
            query['CaEnabled'] = request.ca_enabled
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_actions):
            query['DefaultActions'] = request.default_actions
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.gzip_enabled):
            query['GzipEnabled'] = request.gzip_enabled
        if not UtilClient.is_unset(request.http_2enabled):
            query['Http2Enabled'] = request.http_2enabled
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_description):
            query['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.quic_config):
            query['QuicConfig'] = request.quic_config
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_listener_with_options_async(
        self,
        request: alb_20200616_models.CreateListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateListenerResponse:
        """
        @summary Creates an HTTP, HTTPS, or QUIC listener in a region.
        
        @description ## Usage notes
        *CreateListener** is an asynchronous operation. After you call this operation, the system returns a request ID. However, the operation is still being performed in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/214353.html) operation to query the status of the HTTP, HTTPS, or QUIC listener.
        If the HTTP, HTTPS, or QUIC listener is in the **Provisioning** state, it indicates that the listener is being created.
        If the HTTP, HTTPS, or QUIC listener is in the **Running** state, it indicates that the listener has been created successfully.
        
        @param request: CreateListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_certificates):
            query['CaCertificates'] = request.ca_certificates
        if not UtilClient.is_unset(request.ca_enabled):
            query['CaEnabled'] = request.ca_enabled
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_actions):
            query['DefaultActions'] = request.default_actions
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.gzip_enabled):
            query['GzipEnabled'] = request.gzip_enabled
        if not UtilClient.is_unset(request.http_2enabled):
            query['Http2Enabled'] = request.http_2enabled
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_description):
            query['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.quic_config):
            query['QuicConfig'] = request.quic_config
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_listener(
        self,
        request: alb_20200616_models.CreateListenerRequest,
    ) -> alb_20200616_models.CreateListenerResponse:
        """
        @summary Creates an HTTP, HTTPS, or QUIC listener in a region.
        
        @description ## Usage notes
        *CreateListener** is an asynchronous operation. After you call this operation, the system returns a request ID. However, the operation is still being performed in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/214353.html) operation to query the status of the HTTP, HTTPS, or QUIC listener.
        If the HTTP, HTTPS, or QUIC listener is in the **Provisioning** state, it indicates that the listener is being created.
        If the HTTP, HTTPS, or QUIC listener is in the **Running** state, it indicates that the listener has been created successfully.
        
        @param request: CreateListenerRequest
        @return: CreateListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_listener_with_options(request, runtime)

    async def create_listener_async(
        self,
        request: alb_20200616_models.CreateListenerRequest,
    ) -> alb_20200616_models.CreateListenerResponse:
        """
        @summary Creates an HTTP, HTTPS, or QUIC listener in a region.
        
        @description ## Usage notes
        *CreateListener** is an asynchronous operation. After you call this operation, the system returns a request ID. However, the operation is still being performed in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/214353.html) operation to query the status of the HTTP, HTTPS, or QUIC listener.
        If the HTTP, HTTPS, or QUIC listener is in the **Provisioning** state, it indicates that the listener is being created.
        If the HTTP, HTTPS, or QUIC listener is in the **Running** state, it indicates that the listener has been created successfully.
        
        @param request: CreateListenerRequest
        @return: CreateListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_listener_with_options_async(request, runtime)

    def create_load_balancer_with_options(
        self,
        request: alb_20200616_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateLoadBalancerResponse:
        """
        @summary Creates an Application Load Balancer (ALB) instance in a region.
        
        @description *CreateLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of an ALB instance.
        If an ALB instance is in the **Provisioning** state, it indicates that the ALB instance is being created.
        If an ALB instance is in the **Active** state, it indicates that the ALB instance is created.
        
        @param request: CreateLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_allocated_mode):
            query['AddressAllocatedMode'] = request.address_allocated_mode
        if not UtilClient.is_unset(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deletion_protection_enabled):
            query['DeletionProtectionEnabled'] = request.deletion_protection_enabled
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_billing_config):
            query['LoadBalancerBillingConfig'] = request.load_balancer_billing_config
        if not UtilClient.is_unset(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.modification_protection_config):
            query['ModificationProtectionConfig'] = request.modification_protection_config
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_with_options_async(
        self,
        request: alb_20200616_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateLoadBalancerResponse:
        """
        @summary Creates an Application Load Balancer (ALB) instance in a region.
        
        @description *CreateLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of an ALB instance.
        If an ALB instance is in the **Provisioning** state, it indicates that the ALB instance is being created.
        If an ALB instance is in the **Active** state, it indicates that the ALB instance is created.
        
        @param request: CreateLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_allocated_mode):
            query['AddressAllocatedMode'] = request.address_allocated_mode
        if not UtilClient.is_unset(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deletion_protection_enabled):
            query['DeletionProtectionEnabled'] = request.deletion_protection_enabled
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_billing_config):
            query['LoadBalancerBillingConfig'] = request.load_balancer_billing_config
        if not UtilClient.is_unset(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.modification_protection_config):
            query['ModificationProtectionConfig'] = request.modification_protection_config
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer(
        self,
        request: alb_20200616_models.CreateLoadBalancerRequest,
    ) -> alb_20200616_models.CreateLoadBalancerResponse:
        """
        @summary Creates an Application Load Balancer (ALB) instance in a region.
        
        @description *CreateLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of an ALB instance.
        If an ALB instance is in the **Provisioning** state, it indicates that the ALB instance is being created.
        If an ALB instance is in the **Active** state, it indicates that the ALB instance is created.
        
        @param request: CreateLoadBalancerRequest
        @return: CreateLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_with_options(request, runtime)

    async def create_load_balancer_async(
        self,
        request: alb_20200616_models.CreateLoadBalancerRequest,
    ) -> alb_20200616_models.CreateLoadBalancerResponse:
        """
        @summary Creates an Application Load Balancer (ALB) instance in a region.
        
        @description *CreateLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of an ALB instance.
        If an ALB instance is in the **Provisioning** state, it indicates that the ALB instance is being created.
        If an ALB instance is in the **Active** state, it indicates that the ALB instance is created.
        
        @param request: CreateLoadBalancerRequest
        @return: CreateLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: alb_20200616_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateRuleResponse:
        """
        @summary Creates a forwarding rule for a listener.
        
        @description Take note of the following limits:
        When you configure the **Redirect** action, you can use the default value only for the **HttpCode** parameter. Do not use the default values for the other parameters.
        If you specify the **Rewrite** action together with other actions in a forwarding rule, make sure that the **ForwardGroup** action is specified.
        **CreateRule** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of a forwarding rule.
        If a forwarding rule is in the **Provisioning** state, the forwarding rule is being created.
        If a forwarding rule is in the **Available** state, the forwarding rule is created.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. The limits on conditions and actions are:
        Limits on conditions: 5 for a basic Application Load Balancer (ALB) instance, 10 for a standard ALB instance, and 10 for a WAF-enabled ALB instance.
        Limits on actions: 3 for a basic ALB instance, 5 for a standard ALB instance, and 5 for a WAF-enabled ALB instance.
        
        @param request: CreateRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rule_actions):
            query['RuleActions'] = request.rule_actions
        if not UtilClient.is_unset(request.rule_conditions):
            query['RuleConditions'] = request.rule_conditions
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: alb_20200616_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateRuleResponse:
        """
        @summary Creates a forwarding rule for a listener.
        
        @description Take note of the following limits:
        When you configure the **Redirect** action, you can use the default value only for the **HttpCode** parameter. Do not use the default values for the other parameters.
        If you specify the **Rewrite** action together with other actions in a forwarding rule, make sure that the **ForwardGroup** action is specified.
        **CreateRule** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of a forwarding rule.
        If a forwarding rule is in the **Provisioning** state, the forwarding rule is being created.
        If a forwarding rule is in the **Available** state, the forwarding rule is created.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. The limits on conditions and actions are:
        Limits on conditions: 5 for a basic Application Load Balancer (ALB) instance, 10 for a standard ALB instance, and 10 for a WAF-enabled ALB instance.
        Limits on actions: 3 for a basic ALB instance, 5 for a standard ALB instance, and 5 for a WAF-enabled ALB instance.
        
        @param request: CreateRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rule_actions):
            query['RuleActions'] = request.rule_actions
        if not UtilClient.is_unset(request.rule_conditions):
            query['RuleConditions'] = request.rule_conditions
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rule(
        self,
        request: alb_20200616_models.CreateRuleRequest,
    ) -> alb_20200616_models.CreateRuleResponse:
        """
        @summary Creates a forwarding rule for a listener.
        
        @description Take note of the following limits:
        When you configure the **Redirect** action, you can use the default value only for the **HttpCode** parameter. Do not use the default values for the other parameters.
        If you specify the **Rewrite** action together with other actions in a forwarding rule, make sure that the **ForwardGroup** action is specified.
        **CreateRule** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of a forwarding rule.
        If a forwarding rule is in the **Provisioning** state, the forwarding rule is being created.
        If a forwarding rule is in the **Available** state, the forwarding rule is created.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. The limits on conditions and actions are:
        Limits on conditions: 5 for a basic Application Load Balancer (ALB) instance, 10 for a standard ALB instance, and 10 for a WAF-enabled ALB instance.
        Limits on actions: 3 for a basic ALB instance, 5 for a standard ALB instance, and 5 for a WAF-enabled ALB instance.
        
        @param request: CreateRuleRequest
        @return: CreateRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: alb_20200616_models.CreateRuleRequest,
    ) -> alb_20200616_models.CreateRuleResponse:
        """
        @summary Creates a forwarding rule for a listener.
        
        @description Take note of the following limits:
        When you configure the **Redirect** action, you can use the default value only for the **HttpCode** parameter. Do not use the default values for the other parameters.
        If you specify the **Rewrite** action together with other actions in a forwarding rule, make sure that the **ForwardGroup** action is specified.
        **CreateRule** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of a forwarding rule.
        If a forwarding rule is in the **Provisioning** state, the forwarding rule is being created.
        If a forwarding rule is in the **Available** state, the forwarding rule is created.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. The limits on conditions and actions are:
        Limits on conditions: 5 for a basic Application Load Balancer (ALB) instance, 10 for a standard ALB instance, and 10 for a WAF-enabled ALB instance.
        Limits on actions: 3 for a basic ALB instance, 5 for a standard ALB instance, and 5 for a WAF-enabled ALB instance.
        
        @param request: CreateRuleRequest
        @return: CreateRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_rules_with_options(
        self,
        request: alb_20200616_models.CreateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateRulesResponse:
        """
        @summary Creates one or more forwarding rules at a time.
        
        @description When you call this operation, take note of the following limits:
        When you configure the **Redirect** action, you can use the default value for the **HttpCode** parameter but you cannot use the default values for all of the other parameters.
        If you specify the **Rewrite** action and other actions in a forwarding rule, make sure that one of the actions is **ForwardGroup**.
        **CreateRules** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of forwarding rules.
        If forwarding rules are in the **Provisioning** state, the forwarding rules are being created.
        If forwarding rules are in the **Available** state, the forwarding rules have been created.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. Take note of the following limits on the number of conditions and the number of actions in each forwarding rule:
        Limits on conditions: You can specify at most 5 conditions if you use a basic Application Load Balancer (ALB) instance, at most 10 conditions if you use a standard ALB instance, and at most 10 conditions if you use a WAF-enabled ALB instance.
        Limits on actions: You can specify at most 3 actions if you use a basic ALB instance, at most 5 actions if you use a standard ALB instance, and at most 10 actions if you use a WAF-enabled ALB instance.
        
        @param request: CreateRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRules',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rules_with_options_async(
        self,
        request: alb_20200616_models.CreateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateRulesResponse:
        """
        @summary Creates one or more forwarding rules at a time.
        
        @description When you call this operation, take note of the following limits:
        When you configure the **Redirect** action, you can use the default value for the **HttpCode** parameter but you cannot use the default values for all of the other parameters.
        If you specify the **Rewrite** action and other actions in a forwarding rule, make sure that one of the actions is **ForwardGroup**.
        **CreateRules** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of forwarding rules.
        If forwarding rules are in the **Provisioning** state, the forwarding rules are being created.
        If forwarding rules are in the **Available** state, the forwarding rules have been created.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. Take note of the following limits on the number of conditions and the number of actions in each forwarding rule:
        Limits on conditions: You can specify at most 5 conditions if you use a basic Application Load Balancer (ALB) instance, at most 10 conditions if you use a standard ALB instance, and at most 10 conditions if you use a WAF-enabled ALB instance.
        Limits on actions: You can specify at most 3 actions if you use a basic ALB instance, at most 5 actions if you use a standard ALB instance, and at most 10 actions if you use a WAF-enabled ALB instance.
        
        @param request: CreateRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRules',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rules(
        self,
        request: alb_20200616_models.CreateRulesRequest,
    ) -> alb_20200616_models.CreateRulesResponse:
        """
        @summary Creates one or more forwarding rules at a time.
        
        @description When you call this operation, take note of the following limits:
        When you configure the **Redirect** action, you can use the default value for the **HttpCode** parameter but you cannot use the default values for all of the other parameters.
        If you specify the **Rewrite** action and other actions in a forwarding rule, make sure that one of the actions is **ForwardGroup**.
        **CreateRules** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of forwarding rules.
        If forwarding rules are in the **Provisioning** state, the forwarding rules are being created.
        If forwarding rules are in the **Available** state, the forwarding rules have been created.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. Take note of the following limits on the number of conditions and the number of actions in each forwarding rule:
        Limits on conditions: You can specify at most 5 conditions if you use a basic Application Load Balancer (ALB) instance, at most 10 conditions if you use a standard ALB instance, and at most 10 conditions if you use a WAF-enabled ALB instance.
        Limits on actions: You can specify at most 3 actions if you use a basic ALB instance, at most 5 actions if you use a standard ALB instance, and at most 10 actions if you use a WAF-enabled ALB instance.
        
        @param request: CreateRulesRequest
        @return: CreateRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_rules_with_options(request, runtime)

    async def create_rules_async(
        self,
        request: alb_20200616_models.CreateRulesRequest,
    ) -> alb_20200616_models.CreateRulesResponse:
        """
        @summary Creates one or more forwarding rules at a time.
        
        @description When you call this operation, take note of the following limits:
        When you configure the **Redirect** action, you can use the default value for the **HttpCode** parameter but you cannot use the default values for all of the other parameters.
        If you specify the **Rewrite** action and other actions in a forwarding rule, make sure that one of the actions is **ForwardGroup**.
        **CreateRules** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of forwarding rules.
        If forwarding rules are in the **Provisioning** state, the forwarding rules are being created.
        If forwarding rules are in the **Available** state, the forwarding rules have been created.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. Take note of the following limits on the number of conditions and the number of actions in each forwarding rule:
        Limits on conditions: You can specify at most 5 conditions if you use a basic Application Load Balancer (ALB) instance, at most 10 conditions if you use a standard ALB instance, and at most 10 conditions if you use a WAF-enabled ALB instance.
        Limits on actions: You can specify at most 3 actions if you use a basic ALB instance, at most 5 actions if you use a standard ALB instance, and at most 10 actions if you use a WAF-enabled ALB instance.
        
        @param request: CreateRulesRequest
        @return: CreateRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_rules_with_options_async(request, runtime)

    def create_security_policy_with_options(
        self,
        request: alb_20200616_models.CreateSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateSecurityPolicyResponse:
        """
        @summary Creates a custom security policy in a region.
        
        @param request: CreateSecurityPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecurityPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_policy_name):
            query['SecurityPolicyName'] = request.security_policy_name
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecurityPolicy',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateSecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_policy_with_options_async(
        self,
        request: alb_20200616_models.CreateSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateSecurityPolicyResponse:
        """
        @summary Creates a custom security policy in a region.
        
        @param request: CreateSecurityPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecurityPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_policy_name):
            query['SecurityPolicyName'] = request.security_policy_name
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecurityPolicy',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateSecurityPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_policy(
        self,
        request: alb_20200616_models.CreateSecurityPolicyRequest,
    ) -> alb_20200616_models.CreateSecurityPolicyResponse:
        """
        @summary Creates a custom security policy in a region.
        
        @param request: CreateSecurityPolicyRequest
        @return: CreateSecurityPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_security_policy_with_options(request, runtime)

    async def create_security_policy_async(
        self,
        request: alb_20200616_models.CreateSecurityPolicyRequest,
    ) -> alb_20200616_models.CreateSecurityPolicyResponse:
        """
        @summary Creates a custom security policy in a region.
        
        @param request: CreateSecurityPolicyRequest
        @return: CreateSecurityPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_security_policy_with_options_async(request, runtime)

    def create_server_group_with_options(
        self,
        request: alb_20200616_models.CreateServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateServerGroupResponse:
        """
        @summary Creates a server group in a region.
        
        @description *CreateServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) to query the status of a server group.
        If a server group is in the **Creating** state, it indicates that the server group is being created.
        If a server group is in the **Available** state, it indicates that the server group is created.
        
        @param request: CreateServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_drain_config):
            query['ConnectionDrainConfig'] = request.connection_drain_config
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_config):
            query['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_group_name):
            query['ServerGroupName'] = request.server_group_name
        if not UtilClient.is_unset(request.server_group_type):
            query['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.slow_start_config):
            query['SlowStartConfig'] = request.slow_start_config
        if not UtilClient.is_unset(request.sticky_session_config):
            query['StickySessionConfig'] = request.sticky_session_config
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.uch_config):
            query['UchConfig'] = request.uch_config
        if not UtilClient.is_unset(request.upstream_keepalive_enabled):
            query['UpstreamKeepaliveEnabled'] = request.upstream_keepalive_enabled
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_server_group_with_options_async(
        self,
        request: alb_20200616_models.CreateServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.CreateServerGroupResponse:
        """
        @summary Creates a server group in a region.
        
        @description *CreateServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) to query the status of a server group.
        If a server group is in the **Creating** state, it indicates that the server group is being created.
        If a server group is in the **Available** state, it indicates that the server group is created.
        
        @param request: CreateServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_drain_config):
            query['ConnectionDrainConfig'] = request.connection_drain_config
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_config):
            query['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_group_name):
            query['ServerGroupName'] = request.server_group_name
        if not UtilClient.is_unset(request.server_group_type):
            query['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.slow_start_config):
            query['SlowStartConfig'] = request.slow_start_config
        if not UtilClient.is_unset(request.sticky_session_config):
            query['StickySessionConfig'] = request.sticky_session_config
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.uch_config):
            query['UchConfig'] = request.uch_config
        if not UtilClient.is_unset(request.upstream_keepalive_enabled):
            query['UpstreamKeepaliveEnabled'] = request.upstream_keepalive_enabled
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.CreateServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_server_group(
        self,
        request: alb_20200616_models.CreateServerGroupRequest,
    ) -> alb_20200616_models.CreateServerGroupResponse:
        """
        @summary Creates a server group in a region.
        
        @description *CreateServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) to query the status of a server group.
        If a server group is in the **Creating** state, it indicates that the server group is being created.
        If a server group is in the **Available** state, it indicates that the server group is created.
        
        @param request: CreateServerGroupRequest
        @return: CreateServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_server_group_with_options(request, runtime)

    async def create_server_group_async(
        self,
        request: alb_20200616_models.CreateServerGroupRequest,
    ) -> alb_20200616_models.CreateServerGroupResponse:
        """
        @summary Creates a server group in a region.
        
        @description *CreateServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) to query the status of a server group.
        If a server group is in the **Creating** state, it indicates that the server group is being created.
        If a server group is in the **Available** state, it indicates that the server group is created.
        
        @param request: CreateServerGroupRequest
        @return: CreateServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_server_group_with_options_async(request, runtime)

    def delete_ascripts_with_options(
        self,
        request: alb_20200616_models.DeleteAScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteAScriptsResponse:
        """
        @summary Deletes AScript rules.
        
        @description *DeleteAScripts** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAScripts](https://help.aliyun.com/document_detail/472574.html) operation to query the status of the task:
        If an AScript rule is in the **Deleting** state, the AScript rule is being deleted.
        If an AScript rule cannot be found, the AScript rule is deleted.
        
        @param request: DeleteAScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAScriptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascript_ids):
            query['AScriptIds'] = request.ascript_ids
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAScripts',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteAScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ascripts_with_options_async(
        self,
        request: alb_20200616_models.DeleteAScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteAScriptsResponse:
        """
        @summary Deletes AScript rules.
        
        @description *DeleteAScripts** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAScripts](https://help.aliyun.com/document_detail/472574.html) operation to query the status of the task:
        If an AScript rule is in the **Deleting** state, the AScript rule is being deleted.
        If an AScript rule cannot be found, the AScript rule is deleted.
        
        @param request: DeleteAScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAScriptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascript_ids):
            query['AScriptIds'] = request.ascript_ids
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAScripts',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteAScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ascripts(
        self,
        request: alb_20200616_models.DeleteAScriptsRequest,
    ) -> alb_20200616_models.DeleteAScriptsResponse:
        """
        @summary Deletes AScript rules.
        
        @description *DeleteAScripts** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAScripts](https://help.aliyun.com/document_detail/472574.html) operation to query the status of the task:
        If an AScript rule is in the **Deleting** state, the AScript rule is being deleted.
        If an AScript rule cannot be found, the AScript rule is deleted.
        
        @param request: DeleteAScriptsRequest
        @return: DeleteAScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ascripts_with_options(request, runtime)

    async def delete_ascripts_async(
        self,
        request: alb_20200616_models.DeleteAScriptsRequest,
    ) -> alb_20200616_models.DeleteAScriptsResponse:
        """
        @summary Deletes AScript rules.
        
        @description *DeleteAScripts** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAScripts](https://help.aliyun.com/document_detail/472574.html) operation to query the status of the task:
        If an AScript rule is in the **Deleting** state, the AScript rule is being deleted.
        If an AScript rule cannot be found, the AScript rule is deleted.
        
        @param request: DeleteAScriptsRequest
        @return: DeleteAScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ascripts_with_options_async(request, runtime)

    def delete_acl_with_options(
        self,
        request: alb_20200616_models.DeleteAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteAclResponse:
        """
        @summary Deletes an access control list (ACL).
        
        @description *DeleteAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAcls](https://help.aliyun.com/document_detail/213617.html) operation to query the status of the task.
        If the ACL is in the **Deleting** state, the ACL is being deleted.
        If the ACL cannot be found, the ACL is deleted.
        
        @param request: DeleteAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_acl_with_options_async(
        self,
        request: alb_20200616_models.DeleteAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteAclResponse:
        """
        @summary Deletes an access control list (ACL).
        
        @description *DeleteAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAcls](https://help.aliyun.com/document_detail/213617.html) operation to query the status of the task.
        If the ACL is in the **Deleting** state, the ACL is being deleted.
        If the ACL cannot be found, the ACL is deleted.
        
        @param request: DeleteAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_acl(
        self,
        request: alb_20200616_models.DeleteAclRequest,
    ) -> alb_20200616_models.DeleteAclResponse:
        """
        @summary Deletes an access control list (ACL).
        
        @description *DeleteAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAcls](https://help.aliyun.com/document_detail/213617.html) operation to query the status of the task.
        If the ACL is in the **Deleting** state, the ACL is being deleted.
        If the ACL cannot be found, the ACL is deleted.
        
        @param request: DeleteAclRequest
        @return: DeleteAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    async def delete_acl_async(
        self,
        request: alb_20200616_models.DeleteAclRequest,
    ) -> alb_20200616_models.DeleteAclResponse:
        """
        @summary Deletes an access control list (ACL).
        
        @description *DeleteAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAcls](https://help.aliyun.com/document_detail/213617.html) operation to query the status of the task.
        If the ACL is in the **Deleting** state, the ACL is being deleted.
        If the ACL cannot be found, the ACL is deleted.
        
        @param request: DeleteAclRequest
        @return: DeleteAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_acl_with_options_async(request, runtime)

    def delete_health_check_templates_with_options(
        self,
        request: alb_20200616_models.DeleteHealthCheckTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteHealthCheckTemplatesResponse:
        """
        @summary Deletes health check templates.
        
        @param request: DeleteHealthCheckTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHealthCheckTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_template_ids):
            query['HealthCheckTemplateIds'] = request.health_check_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHealthCheckTemplates',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteHealthCheckTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_health_check_templates_with_options_async(
        self,
        request: alb_20200616_models.DeleteHealthCheckTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteHealthCheckTemplatesResponse:
        """
        @summary Deletes health check templates.
        
        @param request: DeleteHealthCheckTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHealthCheckTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_template_ids):
            query['HealthCheckTemplateIds'] = request.health_check_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHealthCheckTemplates',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteHealthCheckTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_health_check_templates(
        self,
        request: alb_20200616_models.DeleteHealthCheckTemplatesRequest,
    ) -> alb_20200616_models.DeleteHealthCheckTemplatesResponse:
        """
        @summary Deletes health check templates.
        
        @param request: DeleteHealthCheckTemplatesRequest
        @return: DeleteHealthCheckTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_health_check_templates_with_options(request, runtime)

    async def delete_health_check_templates_async(
        self,
        request: alb_20200616_models.DeleteHealthCheckTemplatesRequest,
    ) -> alb_20200616_models.DeleteHealthCheckTemplatesResponse:
        """
        @summary Deletes health check templates.
        
        @param request: DeleteHealthCheckTemplatesRequest
        @return: DeleteHealthCheckTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_health_check_templates_with_options_async(request, runtime)

    def delete_listener_with_options(
        self,
        request: alb_20200616_models.DeleteListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteListenerResponse:
        """
        @summary Deletes a listener.
        
        @description *DeleteListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) to query the status of the task.
        If the listener is in the **Deleting** state, the listener is being deleted.
        If the listener cannot be found, the listener is deleted.
        
        @param request: DeleteListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_listener_with_options_async(
        self,
        request: alb_20200616_models.DeleteListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteListenerResponse:
        """
        @summary Deletes a listener.
        
        @description *DeleteListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) to query the status of the task.
        If the listener is in the **Deleting** state, the listener is being deleted.
        If the listener cannot be found, the listener is deleted.
        
        @param request: DeleteListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_listener(
        self,
        request: alb_20200616_models.DeleteListenerRequest,
    ) -> alb_20200616_models.DeleteListenerResponse:
        """
        @summary Deletes a listener.
        
        @description *DeleteListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) to query the status of the task.
        If the listener is in the **Deleting** state, the listener is being deleted.
        If the listener cannot be found, the listener is deleted.
        
        @param request: DeleteListenerRequest
        @return: DeleteListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_listener_with_options(request, runtime)

    async def delete_listener_async(
        self,
        request: alb_20200616_models.DeleteListenerRequest,
    ) -> alb_20200616_models.DeleteListenerResponse:
        """
        @summary Deletes a listener.
        
        @description *DeleteListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) to query the status of the task.
        If the listener is in the **Deleting** state, the listener is being deleted.
        If the listener cannot be found, the listener is deleted.
        
        @param request: DeleteListenerRequest
        @return: DeleteListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_listener_with_options_async(request, runtime)

    def delete_load_balancer_with_options(
        self,
        request: alb_20200616_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteLoadBalancerResponse:
        """
        @summary Deletes an Application Load Balancer (ALB) instance.
        
        @description *DeleteLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If an ALB instance is in the **Deleting** state, the ALB instance is being deleted.
        If an ALB instance cannot be found, the ALB instance is deleted.
        
        @param request: DeleteLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_load_balancer_with_options_async(
        self,
        request: alb_20200616_models.DeleteLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteLoadBalancerResponse:
        """
        @summary Deletes an Application Load Balancer (ALB) instance.
        
        @description *DeleteLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If an ALB instance is in the **Deleting** state, the ALB instance is being deleted.
        If an ALB instance cannot be found, the ALB instance is deleted.
        
        @param request: DeleteLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_load_balancer(
        self,
        request: alb_20200616_models.DeleteLoadBalancerRequest,
    ) -> alb_20200616_models.DeleteLoadBalancerResponse:
        """
        @summary Deletes an Application Load Balancer (ALB) instance.
        
        @description *DeleteLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If an ALB instance is in the **Deleting** state, the ALB instance is being deleted.
        If an ALB instance cannot be found, the ALB instance is deleted.
        
        @param request: DeleteLoadBalancerRequest
        @return: DeleteLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_with_options(request, runtime)

    async def delete_load_balancer_async(
        self,
        request: alb_20200616_models.DeleteLoadBalancerRequest,
    ) -> alb_20200616_models.DeleteLoadBalancerResponse:
        """
        @summary Deletes an Application Load Balancer (ALB) instance.
        
        @description *DeleteLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If an ALB instance is in the **Deleting** state, the ALB instance is being deleted.
        If an ALB instance cannot be found, the ALB instance is deleted.
        
        @param request: DeleteLoadBalancerRequest
        @return: DeleteLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_load_balancer_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: alb_20200616_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteRuleResponse:
        """
        @summary Deletes a forwarding rule.
        
        @description *DeleteRule** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of a forwarding rule:
        If the forwarding rule is in the **Deleting** state, the forwarding rule is being deleted.
        If the forwarding rule cannot be found, the forwarding rule is deleted.
        
        @param request: DeleteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: alb_20200616_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteRuleResponse:
        """
        @summary Deletes a forwarding rule.
        
        @description *DeleteRule** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of a forwarding rule:
        If the forwarding rule is in the **Deleting** state, the forwarding rule is being deleted.
        If the forwarding rule cannot be found, the forwarding rule is deleted.
        
        @param request: DeleteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule(
        self,
        request: alb_20200616_models.DeleteRuleRequest,
    ) -> alb_20200616_models.DeleteRuleResponse:
        """
        @summary Deletes a forwarding rule.
        
        @description *DeleteRule** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of a forwarding rule:
        If the forwarding rule is in the **Deleting** state, the forwarding rule is being deleted.
        If the forwarding rule cannot be found, the forwarding rule is deleted.
        
        @param request: DeleteRuleRequest
        @return: DeleteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: alb_20200616_models.DeleteRuleRequest,
    ) -> alb_20200616_models.DeleteRuleResponse:
        """
        @summary Deletes a forwarding rule.
        
        @description *DeleteRule** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of a forwarding rule:
        If the forwarding rule is in the **Deleting** state, the forwarding rule is being deleted.
        If the forwarding rule cannot be found, the forwarding rule is deleted.
        
        @param request: DeleteRuleRequest
        @return: DeleteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_rules_with_options(
        self,
        request: alb_20200616_models.DeleteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteRulesResponse:
        """
        @summary Deletes one or more forwarding rules from a listener at a time.
        
        @description *DeleteRules** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of forwarding rules.
        If the forwarding rules are in the **Deleting** state, the forwarding rules are being deleted.
        If the forwarding rules cannot be found, the forwarding rules are deleted.
        
        @param request: DeleteRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRules',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rules_with_options_async(
        self,
        request: alb_20200616_models.DeleteRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteRulesResponse:
        """
        @summary Deletes one or more forwarding rules from a listener at a time.
        
        @description *DeleteRules** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of forwarding rules.
        If the forwarding rules are in the **Deleting** state, the forwarding rules are being deleted.
        If the forwarding rules cannot be found, the forwarding rules are deleted.
        
        @param request: DeleteRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRules',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rules(
        self,
        request: alb_20200616_models.DeleteRulesRequest,
    ) -> alb_20200616_models.DeleteRulesResponse:
        """
        @summary Deletes one or more forwarding rules from a listener at a time.
        
        @description *DeleteRules** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of forwarding rules.
        If the forwarding rules are in the **Deleting** state, the forwarding rules are being deleted.
        If the forwarding rules cannot be found, the forwarding rules are deleted.
        
        @param request: DeleteRulesRequest
        @return: DeleteRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rules_with_options(request, runtime)

    async def delete_rules_async(
        self,
        request: alb_20200616_models.DeleteRulesRequest,
    ) -> alb_20200616_models.DeleteRulesResponse:
        """
        @summary Deletes one or more forwarding rules from a listener at a time.
        
        @description *DeleteRules** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of forwarding rules.
        If the forwarding rules are in the **Deleting** state, the forwarding rules are being deleted.
        If the forwarding rules cannot be found, the forwarding rules are deleted.
        
        @param request: DeleteRulesRequest
        @return: DeleteRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_rules_with_options_async(request, runtime)

    def delete_security_policy_with_options(
        self,
        request: alb_20200616_models.DeleteSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteSecurityPolicyResponse:
        """
        @summary Deletes a custom security policy.
        
        @param request: DeleteSecurityPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecurityPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityPolicy',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteSecurityPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_policy_with_options_async(
        self,
        request: alb_20200616_models.DeleteSecurityPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteSecurityPolicyResponse:
        """
        @summary Deletes a custom security policy.
        
        @param request: DeleteSecurityPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecurityPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityPolicy',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteSecurityPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_policy(
        self,
        request: alb_20200616_models.DeleteSecurityPolicyRequest,
    ) -> alb_20200616_models.DeleteSecurityPolicyResponse:
        """
        @summary Deletes a custom security policy.
        
        @param request: DeleteSecurityPolicyRequest
        @return: DeleteSecurityPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_security_policy_with_options(request, runtime)

    async def delete_security_policy_async(
        self,
        request: alb_20200616_models.DeleteSecurityPolicyRequest,
    ) -> alb_20200616_models.DeleteSecurityPolicyResponse:
        """
        @summary Deletes a custom security policy.
        
        @param request: DeleteSecurityPolicyRequest
        @return: DeleteSecurityPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_policy_with_options_async(request, runtime)

    def delete_server_group_with_options(
        self,
        request: alb_20200616_models.DeleteServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteServerGroupResponse:
        """
        @summary Deletes a server group.
        
        @description *DeleteServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of the task.
        If a server group is in the **Deleting** state, it indicates that the server group is being deleted.
        If a specified server group cannot be found, it indicates that the server group has been deleted.
        
        @param request: DeleteServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_server_group_with_options_async(
        self,
        request: alb_20200616_models.DeleteServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DeleteServerGroupResponse:
        """
        @summary Deletes a server group.
        
        @description *DeleteServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of the task.
        If a server group is in the **Deleting** state, it indicates that the server group is being deleted.
        If a specified server group cannot be found, it indicates that the server group has been deleted.
        
        @param request: DeleteServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DeleteServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_server_group(
        self,
        request: alb_20200616_models.DeleteServerGroupRequest,
    ) -> alb_20200616_models.DeleteServerGroupResponse:
        """
        @summary Deletes a server group.
        
        @description *DeleteServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of the task.
        If a server group is in the **Deleting** state, it indicates that the server group is being deleted.
        If a specified server group cannot be found, it indicates that the server group has been deleted.
        
        @param request: DeleteServerGroupRequest
        @return: DeleteServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_server_group_with_options(request, runtime)

    async def delete_server_group_async(
        self,
        request: alb_20200616_models.DeleteServerGroupRequest,
    ) -> alb_20200616_models.DeleteServerGroupResponse:
        """
        @summary Deletes a server group.
        
        @description *DeleteServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of the task.
        If a server group is in the **Deleting** state, it indicates that the server group is being deleted.
        If a specified server group cannot be found, it indicates that the server group has been deleted.
        
        @param request: DeleteServerGroupRequest
        @return: DeleteServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_server_group_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: alb_20200616_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: alb_20200616_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: alb_20200616_models.DescribeRegionsRequest,
    ) -> alb_20200616_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: alb_20200616_models.DescribeRegionsRequest,
    ) -> alb_20200616_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: alb_20200616_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DescribeZonesResponse:
        """
        @summary Queries zones in a region.
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: alb_20200616_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DescribeZonesResponse:
        """
        @summary Queries zones in a region.
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: alb_20200616_models.DescribeZonesRequest,
    ) -> alb_20200616_models.DescribeZonesResponse:
        """
        @summary Queries zones in a region.
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: alb_20200616_models.DescribeZonesRequest,
    ) -> alb_20200616_models.DescribeZonesResponse:
        """
        @summary Queries zones in a region.
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_common_bandwidth_package_from_load_balancer_with_options(
        self,
        request: alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        """
        @summary Disassociates an elastic IP address (EIP) bandwidth plan from an Application Load Balancer (ALB) instance.
        
        @description *DetachCommonBandwidthPackageFromLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214359.html) operation to query the status of the task.
        If an ALB instance is in the **Configuring** state, the EIP bandwidth plan is being disassociated from the ALB instance.
        If an ALB instance is in the **Active** state, the EIP bandwidth plan is disassociated from the ALB instance.
        
        @param request: DetachCommonBandwidthPackageFromLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachCommonBandwidthPackageFromLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachCommonBandwidthPackageFromLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_common_bandwidth_package_from_load_balancer_with_options_async(
        self,
        request: alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        """
        @summary Disassociates an elastic IP address (EIP) bandwidth plan from an Application Load Balancer (ALB) instance.
        
        @description *DetachCommonBandwidthPackageFromLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214359.html) operation to query the status of the task.
        If an ALB instance is in the **Configuring** state, the EIP bandwidth plan is being disassociated from the ALB instance.
        If an ALB instance is in the **Active** state, the EIP bandwidth plan is disassociated from the ALB instance.
        
        @param request: DetachCommonBandwidthPackageFromLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachCommonBandwidthPackageFromLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachCommonBandwidthPackageFromLoadBalancer',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_common_bandwidth_package_from_load_balancer(
        self,
        request: alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
    ) -> alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        """
        @summary Disassociates an elastic IP address (EIP) bandwidth plan from an Application Load Balancer (ALB) instance.
        
        @description *DetachCommonBandwidthPackageFromLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214359.html) operation to query the status of the task.
        If an ALB instance is in the **Configuring** state, the EIP bandwidth plan is being disassociated from the ALB instance.
        If an ALB instance is in the **Active** state, the EIP bandwidth plan is disassociated from the ALB instance.
        
        @param request: DetachCommonBandwidthPackageFromLoadBalancerRequest
        @return: DetachCommonBandwidthPackageFromLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_common_bandwidth_package_from_load_balancer_with_options(request, runtime)

    async def detach_common_bandwidth_package_from_load_balancer_async(
        self,
        request: alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerRequest,
    ) -> alb_20200616_models.DetachCommonBandwidthPackageFromLoadBalancerResponse:
        """
        @summary Disassociates an elastic IP address (EIP) bandwidth plan from an Application Load Balancer (ALB) instance.
        
        @description *DetachCommonBandwidthPackageFromLoadBalancer** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214359.html) operation to query the status of the task.
        If an ALB instance is in the **Configuring** state, the EIP bandwidth plan is being disassociated from the ALB instance.
        If an ALB instance is in the **Active** state, the EIP bandwidth plan is disassociated from the ALB instance.
        
        @param request: DetachCommonBandwidthPackageFromLoadBalancerRequest
        @return: DetachCommonBandwidthPackageFromLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_common_bandwidth_package_from_load_balancer_with_options_async(request, runtime)

    def disable_deletion_protection_with_options(
        self,
        request: alb_20200616_models.DisableDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableDeletionProtectionResponse:
        """
        @summary Disables deletion protection for an Application Load Balancer (ALB) instance.
        
        @param request: DisableDeletionProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDeletionProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDeletionProtection',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_deletion_protection_with_options_async(
        self,
        request: alb_20200616_models.DisableDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableDeletionProtectionResponse:
        """
        @summary Disables deletion protection for an Application Load Balancer (ALB) instance.
        
        @param request: DisableDeletionProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDeletionProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDeletionProtection',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_deletion_protection(
        self,
        request: alb_20200616_models.DisableDeletionProtectionRequest,
    ) -> alb_20200616_models.DisableDeletionProtectionResponse:
        """
        @summary Disables deletion protection for an Application Load Balancer (ALB) instance.
        
        @param request: DisableDeletionProtectionRequest
        @return: DisableDeletionProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_deletion_protection_with_options(request, runtime)

    async def disable_deletion_protection_async(
        self,
        request: alb_20200616_models.DisableDeletionProtectionRequest,
    ) -> alb_20200616_models.DisableDeletionProtectionResponse:
        """
        @summary Disables deletion protection for an Application Load Balancer (ALB) instance.
        
        @param request: DisableDeletionProtectionRequest
        @return: DisableDeletionProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_deletion_protection_with_options_async(request, runtime)

    def disable_load_balancer_access_log_with_options(
        self,
        request: alb_20200616_models.DisableLoadBalancerAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableLoadBalancerAccessLogResponse:
        """
        @summary Disables the access log feature for a Server Load Balancer (SLB) instance.
        
        @param request: DisableLoadBalancerAccessLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableLoadBalancerAccessLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLoadBalancerAccessLog',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableLoadBalancerAccessLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_load_balancer_access_log_with_options_async(
        self,
        request: alb_20200616_models.DisableLoadBalancerAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableLoadBalancerAccessLogResponse:
        """
        @summary Disables the access log feature for a Server Load Balancer (SLB) instance.
        
        @param request: DisableLoadBalancerAccessLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableLoadBalancerAccessLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLoadBalancerAccessLog',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableLoadBalancerAccessLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_load_balancer_access_log(
        self,
        request: alb_20200616_models.DisableLoadBalancerAccessLogRequest,
    ) -> alb_20200616_models.DisableLoadBalancerAccessLogResponse:
        """
        @summary Disables the access log feature for a Server Load Balancer (SLB) instance.
        
        @param request: DisableLoadBalancerAccessLogRequest
        @return: DisableLoadBalancerAccessLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_load_balancer_access_log_with_options(request, runtime)

    async def disable_load_balancer_access_log_async(
        self,
        request: alb_20200616_models.DisableLoadBalancerAccessLogRequest,
    ) -> alb_20200616_models.DisableLoadBalancerAccessLogResponse:
        """
        @summary Disables the access log feature for a Server Load Balancer (SLB) instance.
        
        @param request: DisableLoadBalancerAccessLogRequest
        @return: DisableLoadBalancerAccessLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_load_balancer_access_log_with_options_async(request, runtime)

    def disable_load_balancer_ipv_6internet_with_options(
        self,
        request: alb_20200616_models.DisableLoadBalancerIpv6InternetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableLoadBalancerIpv6InternetResponse:
        """
        @summary Changes the type of the IPv6 address that is used by a dual-stack Application Load Balancer (ALB) instance from public to private.
        
        @description ### Prerequisites
        An ALB instance is created and IPv4/IPv6 dual stack is enabled for the instance. You can call the [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html) operation and set *AddressIpVersion** to **DualStack** to create a dual-stack ALB instance.
        > If you set *AddressIpVersion** to **DualStack**:
        If you set **AddressType** to **Internet**, the ALB instance uses a public IPv4 IP address and a private IPv6 address.
        If you set **AddressType** to **Intranet**, the ALB instance uses a private IPv4 IP address and a private IPv6 address.
        ### Description
        After the DisableLoadBalancerIpv6Internet operation is called, the value of **Ipv6AddressType** is changed to **Intranet** and the type of the IPv6 address of the ALB instance is changed from public to private. If you upgrade the instance or the instance scales elastic network interfaces (ENIs) along with workloads, private IPv6 addresses are automatically enabled for the instance and the new ENIs. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the value of **Ipv6AddressType**.
        **DisableLoadBalancerIpv6Internet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of the task.
        If the ALB instance is in the **Configuring** state, the network type of the IPv6 address that is used by the ALB instance is being changed.
        If the ALB instance is in the **Active** state, the network type of the IPv6 address that is used by the ALB instance is changed.
        
        @param request: DisableLoadBalancerIpv6InternetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableLoadBalancerIpv6InternetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLoadBalancerIpv6Internet',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableLoadBalancerIpv6InternetResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_load_balancer_ipv_6internet_with_options_async(
        self,
        request: alb_20200616_models.DisableLoadBalancerIpv6InternetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DisableLoadBalancerIpv6InternetResponse:
        """
        @summary Changes the type of the IPv6 address that is used by a dual-stack Application Load Balancer (ALB) instance from public to private.
        
        @description ### Prerequisites
        An ALB instance is created and IPv4/IPv6 dual stack is enabled for the instance. You can call the [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html) operation and set *AddressIpVersion** to **DualStack** to create a dual-stack ALB instance.
        > If you set *AddressIpVersion** to **DualStack**:
        If you set **AddressType** to **Internet**, the ALB instance uses a public IPv4 IP address and a private IPv6 address.
        If you set **AddressType** to **Intranet**, the ALB instance uses a private IPv4 IP address and a private IPv6 address.
        ### Description
        After the DisableLoadBalancerIpv6Internet operation is called, the value of **Ipv6AddressType** is changed to **Intranet** and the type of the IPv6 address of the ALB instance is changed from public to private. If you upgrade the instance or the instance scales elastic network interfaces (ENIs) along with workloads, private IPv6 addresses are automatically enabled for the instance and the new ENIs. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the value of **Ipv6AddressType**.
        **DisableLoadBalancerIpv6Internet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of the task.
        If the ALB instance is in the **Configuring** state, the network type of the IPv6 address that is used by the ALB instance is being changed.
        If the ALB instance is in the **Active** state, the network type of the IPv6 address that is used by the ALB instance is changed.
        
        @param request: DisableLoadBalancerIpv6InternetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableLoadBalancerIpv6InternetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLoadBalancerIpv6Internet',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DisableLoadBalancerIpv6InternetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_load_balancer_ipv_6internet(
        self,
        request: alb_20200616_models.DisableLoadBalancerIpv6InternetRequest,
    ) -> alb_20200616_models.DisableLoadBalancerIpv6InternetResponse:
        """
        @summary Changes the type of the IPv6 address that is used by a dual-stack Application Load Balancer (ALB) instance from public to private.
        
        @description ### Prerequisites
        An ALB instance is created and IPv4/IPv6 dual stack is enabled for the instance. You can call the [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html) operation and set *AddressIpVersion** to **DualStack** to create a dual-stack ALB instance.
        > If you set *AddressIpVersion** to **DualStack**:
        If you set **AddressType** to **Internet**, the ALB instance uses a public IPv4 IP address and a private IPv6 address.
        If you set **AddressType** to **Intranet**, the ALB instance uses a private IPv4 IP address and a private IPv6 address.
        ### Description
        After the DisableLoadBalancerIpv6Internet operation is called, the value of **Ipv6AddressType** is changed to **Intranet** and the type of the IPv6 address of the ALB instance is changed from public to private. If you upgrade the instance or the instance scales elastic network interfaces (ENIs) along with workloads, private IPv6 addresses are automatically enabled for the instance and the new ENIs. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the value of **Ipv6AddressType**.
        **DisableLoadBalancerIpv6Internet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of the task.
        If the ALB instance is in the **Configuring** state, the network type of the IPv6 address that is used by the ALB instance is being changed.
        If the ALB instance is in the **Active** state, the network type of the IPv6 address that is used by the ALB instance is changed.
        
        @param request: DisableLoadBalancerIpv6InternetRequest
        @return: DisableLoadBalancerIpv6InternetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_load_balancer_ipv_6internet_with_options(request, runtime)

    async def disable_load_balancer_ipv_6internet_async(
        self,
        request: alb_20200616_models.DisableLoadBalancerIpv6InternetRequest,
    ) -> alb_20200616_models.DisableLoadBalancerIpv6InternetResponse:
        """
        @summary Changes the type of the IPv6 address that is used by a dual-stack Application Load Balancer (ALB) instance from public to private.
        
        @description ### Prerequisites
        An ALB instance is created and IPv4/IPv6 dual stack is enabled for the instance. You can call the [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html) operation and set *AddressIpVersion** to **DualStack** to create a dual-stack ALB instance.
        > If you set *AddressIpVersion** to **DualStack**:
        If you set **AddressType** to **Internet**, the ALB instance uses a public IPv4 IP address and a private IPv6 address.
        If you set **AddressType** to **Intranet**, the ALB instance uses a private IPv4 IP address and a private IPv6 address.
        ### Description
        After the DisableLoadBalancerIpv6Internet operation is called, the value of **Ipv6AddressType** is changed to **Intranet** and the type of the IPv6 address of the ALB instance is changed from public to private. If you upgrade the instance or the instance scales elastic network interfaces (ENIs) along with workloads, private IPv6 addresses are automatically enabled for the instance and the new ENIs. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the value of **Ipv6AddressType**.
        **DisableLoadBalancerIpv6Internet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of the task.
        If the ALB instance is in the **Configuring** state, the network type of the IPv6 address that is used by the ALB instance is being changed.
        If the ALB instance is in the **Active** state, the network type of the IPv6 address that is used by the ALB instance is changed.
        
        @param request: DisableLoadBalancerIpv6InternetRequest
        @return: DisableLoadBalancerIpv6InternetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_load_balancer_ipv_6internet_with_options_async(request, runtime)

    def dissociate_acls_from_listener_with_options(
        self,
        request: alb_20200616_models.DissociateAclsFromListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DissociateAclsFromListenerResponse:
        """
        @summary Disassociates access control lists (ACLs) from a listener.
        
        @description *DeleteDhcpOptionsSet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclRelations](https://help.aliyun.com/document_detail/213618.html) operation to query the status of the task.
        If an ACL is in the **Dissociating** state, the ACL is being disassociated from the listener.
        If an ACL is in the **Dissociated** state, the ACL is disassociated from the listener.
        
        @param request: DissociateAclsFromListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateAclsFromListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateAclsFromListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DissociateAclsFromListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_acls_from_listener_with_options_async(
        self,
        request: alb_20200616_models.DissociateAclsFromListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DissociateAclsFromListenerResponse:
        """
        @summary Disassociates access control lists (ACLs) from a listener.
        
        @description *DeleteDhcpOptionsSet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclRelations](https://help.aliyun.com/document_detail/213618.html) operation to query the status of the task.
        If an ACL is in the **Dissociating** state, the ACL is being disassociated from the listener.
        If an ACL is in the **Dissociated** state, the ACL is disassociated from the listener.
        
        @param request: DissociateAclsFromListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateAclsFromListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateAclsFromListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DissociateAclsFromListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_acls_from_listener(
        self,
        request: alb_20200616_models.DissociateAclsFromListenerRequest,
    ) -> alb_20200616_models.DissociateAclsFromListenerResponse:
        """
        @summary Disassociates access control lists (ACLs) from a listener.
        
        @description *DeleteDhcpOptionsSet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclRelations](https://help.aliyun.com/document_detail/213618.html) operation to query the status of the task.
        If an ACL is in the **Dissociating** state, the ACL is being disassociated from the listener.
        If an ACL is in the **Dissociated** state, the ACL is disassociated from the listener.
        
        @param request: DissociateAclsFromListenerRequest
        @return: DissociateAclsFromListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dissociate_acls_from_listener_with_options(request, runtime)

    async def dissociate_acls_from_listener_async(
        self,
        request: alb_20200616_models.DissociateAclsFromListenerRequest,
    ) -> alb_20200616_models.DissociateAclsFromListenerResponse:
        """
        @summary Disassociates access control lists (ACLs) from a listener.
        
        @description *DeleteDhcpOptionsSet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclRelations](https://help.aliyun.com/document_detail/213618.html) operation to query the status of the task.
        If an ACL is in the **Dissociating** state, the ACL is being disassociated from the listener.
        If an ACL is in the **Dissociated** state, the ACL is disassociated from the listener.
        
        @param request: DissociateAclsFromListenerRequest
        @return: DissociateAclsFromListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_acls_from_listener_with_options_async(request, runtime)

    def dissociate_additional_certificates_from_listener_with_options(
        self,
        request: alb_20200616_models.DissociateAdditionalCertificatesFromListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse:
        """
        @summary Disassociates additional certificates from a listener.
        
        @description *DissociateAdditionalCertificatesFromListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListListenerCertificates](https://help.aliyun.com/document_detail/214354.html) operation to query the status of the task. - If an additional certificate is in the **Dissociating** state, the additional certificate is being disassociated. - If an additional certificate is in the **Dissociated** state, the additional certificate is disassociated.
        
        @param request: DissociateAdditionalCertificatesFromListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateAdditionalCertificatesFromListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateAdditionalCertificatesFromListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_additional_certificates_from_listener_with_options_async(
        self,
        request: alb_20200616_models.DissociateAdditionalCertificatesFromListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse:
        """
        @summary Disassociates additional certificates from a listener.
        
        @description *DissociateAdditionalCertificatesFromListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListListenerCertificates](https://help.aliyun.com/document_detail/214354.html) operation to query the status of the task. - If an additional certificate is in the **Dissociating** state, the additional certificate is being disassociated. - If an additional certificate is in the **Dissociated** state, the additional certificate is disassociated.
        
        @param request: DissociateAdditionalCertificatesFromListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateAdditionalCertificatesFromListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateAdditionalCertificatesFromListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_additional_certificates_from_listener(
        self,
        request: alb_20200616_models.DissociateAdditionalCertificatesFromListenerRequest,
    ) -> alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse:
        """
        @summary Disassociates additional certificates from a listener.
        
        @description *DissociateAdditionalCertificatesFromListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListListenerCertificates](https://help.aliyun.com/document_detail/214354.html) operation to query the status of the task. - If an additional certificate is in the **Dissociating** state, the additional certificate is being disassociated. - If an additional certificate is in the **Dissociated** state, the additional certificate is disassociated.
        
        @param request: DissociateAdditionalCertificatesFromListenerRequest
        @return: DissociateAdditionalCertificatesFromListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dissociate_additional_certificates_from_listener_with_options(request, runtime)

    async def dissociate_additional_certificates_from_listener_async(
        self,
        request: alb_20200616_models.DissociateAdditionalCertificatesFromListenerRequest,
    ) -> alb_20200616_models.DissociateAdditionalCertificatesFromListenerResponse:
        """
        @summary Disassociates additional certificates from a listener.
        
        @description *DissociateAdditionalCertificatesFromListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListListenerCertificates](https://help.aliyun.com/document_detail/214354.html) operation to query the status of the task. - If an additional certificate is in the **Dissociating** state, the additional certificate is being disassociated. - If an additional certificate is in the **Dissociated** state, the additional certificate is disassociated.
        
        @param request: DissociateAdditionalCertificatesFromListenerRequest
        @return: DissociateAdditionalCertificatesFromListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_additional_certificates_from_listener_with_options_async(request, runtime)

    def enable_deletion_protection_with_options(
        self,
        request: alb_20200616_models.EnableDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableDeletionProtectionResponse:
        """
        @summary Enables deletion protection for a resource.
        
        @param request: EnableDeletionProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDeletionProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDeletionProtection',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_deletion_protection_with_options_async(
        self,
        request: alb_20200616_models.EnableDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableDeletionProtectionResponse:
        """
        @summary Enables deletion protection for a resource.
        
        @param request: EnableDeletionProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDeletionProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDeletionProtection',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_deletion_protection(
        self,
        request: alb_20200616_models.EnableDeletionProtectionRequest,
    ) -> alb_20200616_models.EnableDeletionProtectionResponse:
        """
        @summary Enables deletion protection for a resource.
        
        @param request: EnableDeletionProtectionRequest
        @return: EnableDeletionProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_deletion_protection_with_options(request, runtime)

    async def enable_deletion_protection_async(
        self,
        request: alb_20200616_models.EnableDeletionProtectionRequest,
    ) -> alb_20200616_models.EnableDeletionProtectionResponse:
        """
        @summary Enables deletion protection for a resource.
        
        @param request: EnableDeletionProtectionRequest
        @return: EnableDeletionProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_deletion_protection_with_options_async(request, runtime)

    def enable_load_balancer_access_log_with_options(
        self,
        request: alb_20200616_models.EnableLoadBalancerAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableLoadBalancerAccessLogResponse:
        """
        @summary Enables the access log feature for an Application Load Balancer (ALB) instance.
        
        @param request: EnableLoadBalancerAccessLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableLoadBalancerAccessLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.log_project):
            query['LogProject'] = request.log_project
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLoadBalancerAccessLog',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableLoadBalancerAccessLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_load_balancer_access_log_with_options_async(
        self,
        request: alb_20200616_models.EnableLoadBalancerAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableLoadBalancerAccessLogResponse:
        """
        @summary Enables the access log feature for an Application Load Balancer (ALB) instance.
        
        @param request: EnableLoadBalancerAccessLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableLoadBalancerAccessLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.log_project):
            query['LogProject'] = request.log_project
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLoadBalancerAccessLog',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableLoadBalancerAccessLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_load_balancer_access_log(
        self,
        request: alb_20200616_models.EnableLoadBalancerAccessLogRequest,
    ) -> alb_20200616_models.EnableLoadBalancerAccessLogResponse:
        """
        @summary Enables the access log feature for an Application Load Balancer (ALB) instance.
        
        @param request: EnableLoadBalancerAccessLogRequest
        @return: EnableLoadBalancerAccessLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_load_balancer_access_log_with_options(request, runtime)

    async def enable_load_balancer_access_log_async(
        self,
        request: alb_20200616_models.EnableLoadBalancerAccessLogRequest,
    ) -> alb_20200616_models.EnableLoadBalancerAccessLogResponse:
        """
        @summary Enables the access log feature for an Application Load Balancer (ALB) instance.
        
        @param request: EnableLoadBalancerAccessLogRequest
        @return: EnableLoadBalancerAccessLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_load_balancer_access_log_with_options_async(request, runtime)

    def enable_load_balancer_ipv_6internet_with_options(
        self,
        request: alb_20200616_models.EnableLoadBalancerIpv6InternetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableLoadBalancerIpv6InternetResponse:
        """
        @summary Changes the type of the IPv6 address that is used by a dual-stack Application Load Balancer (ALB) instance from private to public.
        
        @description ### Prerequisites
        An ALB instance is created and IPv4/IPv6 dual stack is enabled for the instance. You can call the [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html) operation and set *AddressIpVersion** to **DualStack** to create a dual-stack ALB instance.
        > If you set *AddressIpVersion** to **DualStack**:
        If you set **AddressType** to **Internet**, the ALB instance uses a public IPv4 IP address and a private IPv6 address.
        If you set **AddressType** to **Intranet**, the ALB instance uses a private IPv4 IP address and a private IPv6 address.
        ### Description
        After the EnableLoadBalancerIpv6Internet operation is called, the value of **Ipv6AddressType** is changed to **Internet** and the type of the IPv6 address of the ALB instance is changed from private to public. If you upgrade the instance or the instance scales elastic network interfaces (ENIs) along with workloads, public IPv6 addresses are automatically enabled for the instance and the new ENIs. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the value of **Ipv6AddressType**.
        **EnableLoadBalancerIpv6Internet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of the task.
        If the ALB instance is in the **Configuring** state, the network type of the IPv6 address that is used by the ALB instance is being changed.
        If the ALB instance is in the **Active** state, the network type of the IPv6 address that is used by the ALB instance is changed.
        
        @param request: EnableLoadBalancerIpv6InternetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableLoadBalancerIpv6InternetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLoadBalancerIpv6Internet',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableLoadBalancerIpv6InternetResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_load_balancer_ipv_6internet_with_options_async(
        self,
        request: alb_20200616_models.EnableLoadBalancerIpv6InternetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.EnableLoadBalancerIpv6InternetResponse:
        """
        @summary Changes the type of the IPv6 address that is used by a dual-stack Application Load Balancer (ALB) instance from private to public.
        
        @description ### Prerequisites
        An ALB instance is created and IPv4/IPv6 dual stack is enabled for the instance. You can call the [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html) operation and set *AddressIpVersion** to **DualStack** to create a dual-stack ALB instance.
        > If you set *AddressIpVersion** to **DualStack**:
        If you set **AddressType** to **Internet**, the ALB instance uses a public IPv4 IP address and a private IPv6 address.
        If you set **AddressType** to **Intranet**, the ALB instance uses a private IPv4 IP address and a private IPv6 address.
        ### Description
        After the EnableLoadBalancerIpv6Internet operation is called, the value of **Ipv6AddressType** is changed to **Internet** and the type of the IPv6 address of the ALB instance is changed from private to public. If you upgrade the instance or the instance scales elastic network interfaces (ENIs) along with workloads, public IPv6 addresses are automatically enabled for the instance and the new ENIs. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the value of **Ipv6AddressType**.
        **EnableLoadBalancerIpv6Internet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of the task.
        If the ALB instance is in the **Configuring** state, the network type of the IPv6 address that is used by the ALB instance is being changed.
        If the ALB instance is in the **Active** state, the network type of the IPv6 address that is used by the ALB instance is changed.
        
        @param request: EnableLoadBalancerIpv6InternetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableLoadBalancerIpv6InternetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLoadBalancerIpv6Internet',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.EnableLoadBalancerIpv6InternetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_load_balancer_ipv_6internet(
        self,
        request: alb_20200616_models.EnableLoadBalancerIpv6InternetRequest,
    ) -> alb_20200616_models.EnableLoadBalancerIpv6InternetResponse:
        """
        @summary Changes the type of the IPv6 address that is used by a dual-stack Application Load Balancer (ALB) instance from private to public.
        
        @description ### Prerequisites
        An ALB instance is created and IPv4/IPv6 dual stack is enabled for the instance. You can call the [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html) operation and set *AddressIpVersion** to **DualStack** to create a dual-stack ALB instance.
        > If you set *AddressIpVersion** to **DualStack**:
        If you set **AddressType** to **Internet**, the ALB instance uses a public IPv4 IP address and a private IPv6 address.
        If you set **AddressType** to **Intranet**, the ALB instance uses a private IPv4 IP address and a private IPv6 address.
        ### Description
        After the EnableLoadBalancerIpv6Internet operation is called, the value of **Ipv6AddressType** is changed to **Internet** and the type of the IPv6 address of the ALB instance is changed from private to public. If you upgrade the instance or the instance scales elastic network interfaces (ENIs) along with workloads, public IPv6 addresses are automatically enabled for the instance and the new ENIs. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the value of **Ipv6AddressType**.
        **EnableLoadBalancerIpv6Internet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of the task.
        If the ALB instance is in the **Configuring** state, the network type of the IPv6 address that is used by the ALB instance is being changed.
        If the ALB instance is in the **Active** state, the network type of the IPv6 address that is used by the ALB instance is changed.
        
        @param request: EnableLoadBalancerIpv6InternetRequest
        @return: EnableLoadBalancerIpv6InternetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_load_balancer_ipv_6internet_with_options(request, runtime)

    async def enable_load_balancer_ipv_6internet_async(
        self,
        request: alb_20200616_models.EnableLoadBalancerIpv6InternetRequest,
    ) -> alb_20200616_models.EnableLoadBalancerIpv6InternetResponse:
        """
        @summary Changes the type of the IPv6 address that is used by a dual-stack Application Load Balancer (ALB) instance from private to public.
        
        @description ### Prerequisites
        An ALB instance is created and IPv4/IPv6 dual stack is enabled for the instance. You can call the [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html) operation and set *AddressIpVersion** to **DualStack** to create a dual-stack ALB instance.
        > If you set *AddressIpVersion** to **DualStack**:
        If you set **AddressType** to **Internet**, the ALB instance uses a public IPv4 IP address and a private IPv6 address.
        If you set **AddressType** to **Intranet**, the ALB instance uses a private IPv4 IP address and a private IPv6 address.
        ### Description
        After the EnableLoadBalancerIpv6Internet operation is called, the value of **Ipv6AddressType** is changed to **Internet** and the type of the IPv6 address of the ALB instance is changed from private to public. If you upgrade the instance or the instance scales elastic network interfaces (ENIs) along with workloads, public IPv6 addresses are automatically enabled for the instance and the new ENIs. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the value of **Ipv6AddressType**.
        **EnableLoadBalancerIpv6Internet** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of the task.
        If the ALB instance is in the **Configuring** state, the network type of the IPv6 address that is used by the ALB instance is being changed.
        If the ALB instance is in the **Active** state, the network type of the IPv6 address that is used by the ALB instance is changed.
        
        @param request: EnableLoadBalancerIpv6InternetRequest
        @return: EnableLoadBalancerIpv6InternetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_load_balancer_ipv_6internet_with_options_async(request, runtime)

    def get_health_check_template_attribute_with_options(
        self,
        request: alb_20200616_models.GetHealthCheckTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetHealthCheckTemplateAttributeResponse:
        """
        @summary Queries the details about a health check template.
        
        @param request: GetHealthCheckTemplateAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHealthCheckTemplateAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHealthCheckTemplateAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetHealthCheckTemplateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_health_check_template_attribute_with_options_async(
        self,
        request: alb_20200616_models.GetHealthCheckTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetHealthCheckTemplateAttributeResponse:
        """
        @summary Queries the details about a health check template.
        
        @param request: GetHealthCheckTemplateAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHealthCheckTemplateAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHealthCheckTemplateAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetHealthCheckTemplateAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_health_check_template_attribute(
        self,
        request: alb_20200616_models.GetHealthCheckTemplateAttributeRequest,
    ) -> alb_20200616_models.GetHealthCheckTemplateAttributeResponse:
        """
        @summary Queries the details about a health check template.
        
        @param request: GetHealthCheckTemplateAttributeRequest
        @return: GetHealthCheckTemplateAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_health_check_template_attribute_with_options(request, runtime)

    async def get_health_check_template_attribute_async(
        self,
        request: alb_20200616_models.GetHealthCheckTemplateAttributeRequest,
    ) -> alb_20200616_models.GetHealthCheckTemplateAttributeResponse:
        """
        @summary Queries the details about a health check template.
        
        @param request: GetHealthCheckTemplateAttributeRequest
        @return: GetHealthCheckTemplateAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_health_check_template_attribute_with_options_async(request, runtime)

    def get_listener_attribute_with_options(
        self,
        request: alb_20200616_models.GetListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetListenerAttributeResponse:
        """
        @summary Queries the details about a listener.
        
        @param request: GetListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListenerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_listener_attribute_with_options_async(
        self,
        request: alb_20200616_models.GetListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetListenerAttributeResponse:
        """
        @summary Queries the details about a listener.
        
        @param request: GetListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListenerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_listener_attribute(
        self,
        request: alb_20200616_models.GetListenerAttributeRequest,
    ) -> alb_20200616_models.GetListenerAttributeResponse:
        """
        @summary Queries the details about a listener.
        
        @param request: GetListenerAttributeRequest
        @return: GetListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_listener_attribute_with_options(request, runtime)

    async def get_listener_attribute_async(
        self,
        request: alb_20200616_models.GetListenerAttributeRequest,
    ) -> alb_20200616_models.GetListenerAttributeResponse:
        """
        @summary Queries the details about a listener.
        
        @param request: GetListenerAttributeRequest
        @return: GetListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_listener_attribute_with_options_async(request, runtime)

    def get_listener_health_status_with_options(
        self,
        request: alb_20200616_models.GetListenerHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetListenerHealthStatusResponse:
        """
        @summary Queries the health check status of a listener and its forwarding rules.
        
        @param request: GetListenerHealthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListenerHealthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_rule):
            query['IncludeRule'] = request.include_rule
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListenerHealthStatus',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetListenerHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_listener_health_status_with_options_async(
        self,
        request: alb_20200616_models.GetListenerHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetListenerHealthStatusResponse:
        """
        @summary Queries the health check status of a listener and its forwarding rules.
        
        @param request: GetListenerHealthStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListenerHealthStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_rule):
            query['IncludeRule'] = request.include_rule
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetListenerHealthStatus',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetListenerHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_listener_health_status(
        self,
        request: alb_20200616_models.GetListenerHealthStatusRequest,
    ) -> alb_20200616_models.GetListenerHealthStatusResponse:
        """
        @summary Queries the health check status of a listener and its forwarding rules.
        
        @param request: GetListenerHealthStatusRequest
        @return: GetListenerHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_listener_health_status_with_options(request, runtime)

    async def get_listener_health_status_async(
        self,
        request: alb_20200616_models.GetListenerHealthStatusRequest,
    ) -> alb_20200616_models.GetListenerHealthStatusResponse:
        """
        @summary Queries the health check status of a listener and its forwarding rules.
        
        @param request: GetListenerHealthStatusRequest
        @return: GetListenerHealthStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_listener_health_status_with_options_async(request, runtime)

    def get_load_balancer_attribute_with_options(
        self,
        request: alb_20200616_models.GetLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetLoadBalancerAttributeResponse:
        """
        @summary Queries the details of an Application Load Balancer (ALB) instance.
        
        @param request: GetLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoadBalancerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_load_balancer_attribute_with_options_async(
        self,
        request: alb_20200616_models.GetLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.GetLoadBalancerAttributeResponse:
        """
        @summary Queries the details of an Application Load Balancer (ALB) instance.
        
        @param request: GetLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoadBalancerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.GetLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_load_balancer_attribute(
        self,
        request: alb_20200616_models.GetLoadBalancerAttributeRequest,
    ) -> alb_20200616_models.GetLoadBalancerAttributeResponse:
        """
        @summary Queries the details of an Application Load Balancer (ALB) instance.
        
        @param request: GetLoadBalancerAttributeRequest
        @return: GetLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_load_balancer_attribute_with_options(request, runtime)

    async def get_load_balancer_attribute_async(
        self,
        request: alb_20200616_models.GetLoadBalancerAttributeRequest,
    ) -> alb_20200616_models.GetLoadBalancerAttributeResponse:
        """
        @summary Queries the details of an Application Load Balancer (ALB) instance.
        
        @param request: GetLoadBalancerAttributeRequest
        @return: GetLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_load_balancer_attribute_with_options_async(request, runtime)

    def list_ascripts_with_options(
        self,
        request: alb_20200616_models.ListAScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAScriptsResponse:
        """
        @summary Queries AScript rules.
        
        @param request: ListAScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAScriptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascript_ids):
            query['AScriptIds'] = request.ascript_ids
        if not UtilClient.is_unset(request.ascript_names):
            query['AScriptNames'] = request.ascript_names
        if not UtilClient.is_unset(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAScripts',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ascripts_with_options_async(
        self,
        request: alb_20200616_models.ListAScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAScriptsResponse:
        """
        @summary Queries AScript rules.
        
        @param request: ListAScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAScriptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascript_ids):
            query['AScriptIds'] = request.ascript_ids
        if not UtilClient.is_unset(request.ascript_names):
            query['AScriptNames'] = request.ascript_names
        if not UtilClient.is_unset(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAScripts',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ascripts(
        self,
        request: alb_20200616_models.ListAScriptsRequest,
    ) -> alb_20200616_models.ListAScriptsResponse:
        """
        @summary Queries AScript rules.
        
        @param request: ListAScriptsRequest
        @return: ListAScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ascripts_with_options(request, runtime)

    async def list_ascripts_async(
        self,
        request: alb_20200616_models.ListAScriptsRequest,
    ) -> alb_20200616_models.ListAScriptsResponse:
        """
        @summary Queries AScript rules.
        
        @param request: ListAScriptsRequest
        @return: ListAScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ascripts_with_options_async(request, runtime)

    def list_acl_entries_with_options(
        self,
        request: alb_20200616_models.ListAclEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclEntriesResponse:
        """
        @summary Queries the entries of an access control list (ACL).
        
        @param request: ListAclEntriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAclEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAclEntries',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acl_entries_with_options_async(
        self,
        request: alb_20200616_models.ListAclEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclEntriesResponse:
        """
        @summary Queries the entries of an access control list (ACL).
        
        @param request: ListAclEntriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAclEntriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAclEntries',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acl_entries(
        self,
        request: alb_20200616_models.ListAclEntriesRequest,
    ) -> alb_20200616_models.ListAclEntriesResponse:
        """
        @summary Queries the entries of an access control list (ACL).
        
        @param request: ListAclEntriesRequest
        @return: ListAclEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_acl_entries_with_options(request, runtime)

    async def list_acl_entries_async(
        self,
        request: alb_20200616_models.ListAclEntriesRequest,
    ) -> alb_20200616_models.ListAclEntriesResponse:
        """
        @summary Queries the entries of an access control list (ACL).
        
        @param request: ListAclEntriesRequest
        @return: ListAclEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_acl_entries_with_options_async(request, runtime)

    def list_acl_relations_with_options(
        self,
        request: alb_20200616_models.ListAclRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclRelationsResponse:
        """
        @summary Queries the listeners that are associated with access control lists (ACLs).
        
        @param request: ListAclRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAclRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAclRelations',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acl_relations_with_options_async(
        self,
        request: alb_20200616_models.ListAclRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclRelationsResponse:
        """
        @summary Queries the listeners that are associated with access control lists (ACLs).
        
        @param request: ListAclRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAclRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAclRelations',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acl_relations(
        self,
        request: alb_20200616_models.ListAclRelationsRequest,
    ) -> alb_20200616_models.ListAclRelationsResponse:
        """
        @summary Queries the listeners that are associated with access control lists (ACLs).
        
        @param request: ListAclRelationsRequest
        @return: ListAclRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_acl_relations_with_options(request, runtime)

    async def list_acl_relations_async(
        self,
        request: alb_20200616_models.ListAclRelationsRequest,
    ) -> alb_20200616_models.ListAclRelationsResponse:
        """
        @summary Queries the listeners that are associated with access control lists (ACLs).
        
        @param request: ListAclRelationsRequest
        @return: ListAclRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_acl_relations_with_options_async(request, runtime)

    def list_acls_with_options(
        self,
        request: alb_20200616_models.ListAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclsResponse:
        """
        @summary Queries the access control lists (ACLs) in a region.
        
        @param request: ListAclsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAclsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.acl_names):
            query['AclNames'] = request.acl_names
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAcls',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acls_with_options_async(
        self,
        request: alb_20200616_models.ListAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAclsResponse:
        """
        @summary Queries the access control lists (ACLs) in a region.
        
        @param request: ListAclsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAclsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not UtilClient.is_unset(request.acl_names):
            query['AclNames'] = request.acl_names
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAcls',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAclsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acls(
        self,
        request: alb_20200616_models.ListAclsRequest,
    ) -> alb_20200616_models.ListAclsResponse:
        """
        @summary Queries the access control lists (ACLs) in a region.
        
        @param request: ListAclsRequest
        @return: ListAclsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_acls_with_options(request, runtime)

    async def list_acls_async(
        self,
        request: alb_20200616_models.ListAclsRequest,
    ) -> alb_20200616_models.ListAclsResponse:
        """
        @summary Queries the access control lists (ACLs) in a region.
        
        @param request: ListAclsRequest
        @return: ListAclsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_acls_with_options_async(request, runtime)

    def list_asyn_jobs_with_options(
        self,
        request: alb_20200616_models.ListAsynJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAsynJobsResponse:
        """
        @summary Queries asynchronous tasks in a region.
        
        @param request: ListAsynJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsynJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsynJobs',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAsynJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_asyn_jobs_with_options_async(
        self,
        request: alb_20200616_models.ListAsynJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListAsynJobsResponse:
        """
        @summary Queries asynchronous tasks in a region.
        
        @param request: ListAsynJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsynJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsynJobs',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListAsynJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_asyn_jobs(
        self,
        request: alb_20200616_models.ListAsynJobsRequest,
    ) -> alb_20200616_models.ListAsynJobsResponse:
        """
        @summary Queries asynchronous tasks in a region.
        
        @param request: ListAsynJobsRequest
        @return: ListAsynJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_asyn_jobs_with_options(request, runtime)

    async def list_asyn_jobs_async(
        self,
        request: alb_20200616_models.ListAsynJobsRequest,
    ) -> alb_20200616_models.ListAsynJobsResponse:
        """
        @summary Queries asynchronous tasks in a region.
        
        @param request: ListAsynJobsRequest
        @return: ListAsynJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_asyn_jobs_with_options_async(request, runtime)

    def list_health_check_templates_with_options(
        self,
        request: alb_20200616_models.ListHealthCheckTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListHealthCheckTemplatesResponse:
        """
        @summary Queries health check templates in a region.
        
        @param request: ListHealthCheckTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHealthCheckTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_check_template_ids):
            query['HealthCheckTemplateIds'] = request.health_check_template_ids
        if not UtilClient.is_unset(request.health_check_template_names):
            query['HealthCheckTemplateNames'] = request.health_check_template_names
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHealthCheckTemplates',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListHealthCheckTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_health_check_templates_with_options_async(
        self,
        request: alb_20200616_models.ListHealthCheckTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListHealthCheckTemplatesResponse:
        """
        @summary Queries health check templates in a region.
        
        @param request: ListHealthCheckTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHealthCheckTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_check_template_ids):
            query['HealthCheckTemplateIds'] = request.health_check_template_ids
        if not UtilClient.is_unset(request.health_check_template_names):
            query['HealthCheckTemplateNames'] = request.health_check_template_names
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHealthCheckTemplates',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListHealthCheckTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_health_check_templates(
        self,
        request: alb_20200616_models.ListHealthCheckTemplatesRequest,
    ) -> alb_20200616_models.ListHealthCheckTemplatesResponse:
        """
        @summary Queries health check templates in a region.
        
        @param request: ListHealthCheckTemplatesRequest
        @return: ListHealthCheckTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_health_check_templates_with_options(request, runtime)

    async def list_health_check_templates_async(
        self,
        request: alb_20200616_models.ListHealthCheckTemplatesRequest,
    ) -> alb_20200616_models.ListHealthCheckTemplatesResponse:
        """
        @summary Queries health check templates in a region.
        
        @param request: ListHealthCheckTemplatesRequest
        @return: ListHealthCheckTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_health_check_templates_with_options_async(request, runtime)

    def list_listener_certificates_with_options(
        self,
        request: alb_20200616_models.ListListenerCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListListenerCertificatesResponse:
        """
        @summary Queries the certificates that are associated with a listener, including additional certificates and the default certificate.
        
        @param request: ListListenerCertificatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListListenerCertificatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_ids):
            query['CertificateIds'] = request.certificate_ids
        if not UtilClient.is_unset(request.certificate_type):
            query['CertificateType'] = request.certificate_type
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListenerCertificates',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListListenerCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listener_certificates_with_options_async(
        self,
        request: alb_20200616_models.ListListenerCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListListenerCertificatesResponse:
        """
        @summary Queries the certificates that are associated with a listener, including additional certificates and the default certificate.
        
        @param request: ListListenerCertificatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListListenerCertificatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_ids):
            query['CertificateIds'] = request.certificate_ids
        if not UtilClient.is_unset(request.certificate_type):
            query['CertificateType'] = request.certificate_type
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListenerCertificates',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListListenerCertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listener_certificates(
        self,
        request: alb_20200616_models.ListListenerCertificatesRequest,
    ) -> alb_20200616_models.ListListenerCertificatesResponse:
        """
        @summary Queries the certificates that are associated with a listener, including additional certificates and the default certificate.
        
        @param request: ListListenerCertificatesRequest
        @return: ListListenerCertificatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_listener_certificates_with_options(request, runtime)

    async def list_listener_certificates_async(
        self,
        request: alb_20200616_models.ListListenerCertificatesRequest,
    ) -> alb_20200616_models.ListListenerCertificatesResponse:
        """
        @summary Queries the certificates that are associated with a listener, including additional certificates and the default certificate.
        
        @param request: ListListenerCertificatesRequest
        @return: ListListenerCertificatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_listener_certificates_with_options_async(request, runtime)

    def list_listeners_with_options(
        self,
        request: alb_20200616_models.ListListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListListenersResponse:
        """
        @summary Queries the listeners in a region.
        
        @param request: ListListenersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListListenersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListeners',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListListenersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listeners_with_options_async(
        self,
        request: alb_20200616_models.ListListenersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListListenersResponse:
        """
        @summary Queries the listeners in a region.
        
        @param request: ListListenersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListListenersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListListeners',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListListenersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listeners(
        self,
        request: alb_20200616_models.ListListenersRequest,
    ) -> alb_20200616_models.ListListenersResponse:
        """
        @summary Queries the listeners in a region.
        
        @param request: ListListenersRequest
        @return: ListListenersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_with_options(request, runtime)

    async def list_listeners_async(
        self,
        request: alb_20200616_models.ListListenersRequest,
    ) -> alb_20200616_models.ListListenersResponse:
        """
        @summary Queries the listeners in a region.
        
        @param request: ListListenersRequest
        @return: ListListenersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_listeners_with_options_async(request, runtime)

    def list_load_balancers_with_options(
        self,
        request: alb_20200616_models.ListLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListLoadBalancersResponse:
        """
        @summary Queries Application Load Balancer (ALB) instances in a region based on filter conditions.
        
        @param request: ListLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.dnsname):
            query['DNSName'] = request.dnsname
        if not UtilClient.is_unset(request.ipv_6address_type):
            query['Ipv6AddressType'] = request.ipv_6address_type
        if not UtilClient.is_unset(request.load_balancer_bussiness_status):
            query['LoadBalancerBussinessStatus'] = request.load_balancer_bussiness_status
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.load_balancer_names):
            query['LoadBalancerNames'] = request.load_balancer_names
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_ids):
            query['VpcIds'] = request.vpc_ids
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLoadBalancers',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_load_balancers_with_options_async(
        self,
        request: alb_20200616_models.ListLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListLoadBalancersResponse:
        """
        @summary Queries Application Load Balancer (ALB) instances in a region based on filter conditions.
        
        @param request: ListLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_ip_version):
            query['AddressIpVersion'] = request.address_ip_version
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.dnsname):
            query['DNSName'] = request.dnsname
        if not UtilClient.is_unset(request.ipv_6address_type):
            query['Ipv6AddressType'] = request.ipv_6address_type
        if not UtilClient.is_unset(request.load_balancer_bussiness_status):
            query['LoadBalancerBussinessStatus'] = request.load_balancer_bussiness_status
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.load_balancer_names):
            query['LoadBalancerNames'] = request.load_balancer_names
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_ids):
            query['VpcIds'] = request.vpc_ids
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLoadBalancers',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_load_balancers(
        self,
        request: alb_20200616_models.ListLoadBalancersRequest,
    ) -> alb_20200616_models.ListLoadBalancersResponse:
        """
        @summary Queries Application Load Balancer (ALB) instances in a region based on filter conditions.
        
        @param request: ListLoadBalancersRequest
        @return: ListLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_load_balancers_with_options(request, runtime)

    async def list_load_balancers_async(
        self,
        request: alb_20200616_models.ListLoadBalancersRequest,
    ) -> alb_20200616_models.ListLoadBalancersResponse:
        """
        @summary Queries Application Load Balancer (ALB) instances in a region based on filter conditions.
        
        @param request: ListLoadBalancersRequest
        @return: ListLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_load_balancers_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: alb_20200616_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListRulesResponse:
        """
        @summary Queries the forwarding rules in a region.
        
        @param request: ListRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: alb_20200616_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListRulesResponse:
        """
        @summary Queries the forwarding rules in a region.
        
        @param request: ListRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.listener_ids):
            query['ListenerIds'] = request.listener_ids
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules(
        self,
        request: alb_20200616_models.ListRulesRequest,
    ) -> alb_20200616_models.ListRulesResponse:
        """
        @summary Queries the forwarding rules in a region.
        
        @param request: ListRulesRequest
        @return: ListRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: alb_20200616_models.ListRulesRequest,
    ) -> alb_20200616_models.ListRulesResponse:
        """
        @summary Queries the forwarding rules in a region.
        
        @param request: ListRulesRequest
        @return: ListRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_security_policies_with_options(
        self,
        request: alb_20200616_models.ListSecurityPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSecurityPoliciesResponse:
        """
        @summary Queries custom security policies in a region.
        
        @param request: ListSecurityPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecurityPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_policy_ids):
            query['SecurityPolicyIds'] = request.security_policy_ids
        if not UtilClient.is_unset(request.security_policy_names):
            query['SecurityPolicyNames'] = request.security_policy_names
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityPolicies',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSecurityPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_policies_with_options_async(
        self,
        request: alb_20200616_models.ListSecurityPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSecurityPoliciesResponse:
        """
        @summary Queries custom security policies in a region.
        
        @param request: ListSecurityPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecurityPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_policy_ids):
            query['SecurityPolicyIds'] = request.security_policy_ids
        if not UtilClient.is_unset(request.security_policy_names):
            query['SecurityPolicyNames'] = request.security_policy_names
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityPolicies',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSecurityPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_policies(
        self,
        request: alb_20200616_models.ListSecurityPoliciesRequest,
    ) -> alb_20200616_models.ListSecurityPoliciesResponse:
        """
        @summary Queries custom security policies in a region.
        
        @param request: ListSecurityPoliciesRequest
        @return: ListSecurityPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_security_policies_with_options(request, runtime)

    async def list_security_policies_async(
        self,
        request: alb_20200616_models.ListSecurityPoliciesRequest,
    ) -> alb_20200616_models.ListSecurityPoliciesResponse:
        """
        @summary Queries custom security policies in a region.
        
        @param request: ListSecurityPoliciesRequest
        @return: ListSecurityPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_security_policies_with_options_async(request, runtime)

    def list_security_policy_relations_with_options(
        self,
        request: alb_20200616_models.ListSecurityPolicyRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSecurityPolicyRelationsResponse:
        """
        @summary Queries the listeners that are associated with security policies.
        
        @param request: ListSecurityPolicyRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecurityPolicyRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_policy_ids):
            query['SecurityPolicyIds'] = request.security_policy_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityPolicyRelations',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSecurityPolicyRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_policy_relations_with_options_async(
        self,
        request: alb_20200616_models.ListSecurityPolicyRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSecurityPolicyRelationsResponse:
        """
        @summary Queries the listeners that are associated with security policies.
        
        @param request: ListSecurityPolicyRelationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSecurityPolicyRelationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_policy_ids):
            query['SecurityPolicyIds'] = request.security_policy_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecurityPolicyRelations',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSecurityPolicyRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_policy_relations(
        self,
        request: alb_20200616_models.ListSecurityPolicyRelationsRequest,
    ) -> alb_20200616_models.ListSecurityPolicyRelationsResponse:
        """
        @summary Queries the listeners that are associated with security policies.
        
        @param request: ListSecurityPolicyRelationsRequest
        @return: ListSecurityPolicyRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_security_policy_relations_with_options(request, runtime)

    async def list_security_policy_relations_async(
        self,
        request: alb_20200616_models.ListSecurityPolicyRelationsRequest,
    ) -> alb_20200616_models.ListSecurityPolicyRelationsResponse:
        """
        @summary Queries the listeners that are associated with security policies.
        
        @param request: ListSecurityPolicyRelationsRequest
        @return: ListSecurityPolicyRelationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_security_policy_relations_with_options_async(request, runtime)

    def list_server_group_servers_with_options(
        self,
        request: alb_20200616_models.ListServerGroupServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListServerGroupServersResponse:
        """
        @summary Queries servers in a server group.
        
        @param request: ListServerGroupServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerGroupServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_ids):
            query['ServerIds'] = request.server_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerGroupServers',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListServerGroupServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_group_servers_with_options_async(
        self,
        request: alb_20200616_models.ListServerGroupServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListServerGroupServersResponse:
        """
        @summary Queries servers in a server group.
        
        @param request: ListServerGroupServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerGroupServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_ids):
            query['ServerIds'] = request.server_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerGroupServers',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListServerGroupServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_group_servers(
        self,
        request: alb_20200616_models.ListServerGroupServersRequest,
    ) -> alb_20200616_models.ListServerGroupServersResponse:
        """
        @summary Queries servers in a server group.
        
        @param request: ListServerGroupServersRequest
        @return: ListServerGroupServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_server_group_servers_with_options(request, runtime)

    async def list_server_group_servers_async(
        self,
        request: alb_20200616_models.ListServerGroupServersRequest,
    ) -> alb_20200616_models.ListServerGroupServersResponse:
        """
        @summary Queries servers in a server group.
        
        @param request: ListServerGroupServersRequest
        @return: ListServerGroupServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_server_group_servers_with_options_async(request, runtime)

    def list_server_groups_with_options(
        self,
        request: alb_20200616_models.ListServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListServerGroupsResponse:
        """
        @summary Queries server groups in a region.
        
        @param request: ListServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.server_group_ids):
            query['ServerGroupIds'] = request.server_group_ids
        if not UtilClient.is_unset(request.server_group_names):
            query['ServerGroupNames'] = request.server_group_names
        if not UtilClient.is_unset(request.server_group_type):
            query['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerGroups',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_groups_with_options_async(
        self,
        request: alb_20200616_models.ListServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListServerGroupsResponse:
        """
        @summary Queries server groups in a region.
        
        @param request: ListServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.server_group_ids):
            query['ServerGroupIds'] = request.server_group_ids
        if not UtilClient.is_unset(request.server_group_names):
            query['ServerGroupNames'] = request.server_group_names
        if not UtilClient.is_unset(request.server_group_type):
            query['ServerGroupType'] = request.server_group_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerGroups',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_groups(
        self,
        request: alb_20200616_models.ListServerGroupsRequest,
    ) -> alb_20200616_models.ListServerGroupsResponse:
        """
        @summary Queries server groups in a region.
        
        @param request: ListServerGroupsRequest
        @return: ListServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_server_groups_with_options(request, runtime)

    async def list_server_groups_async(
        self,
        request: alb_20200616_models.ListServerGroupsRequest,
    ) -> alb_20200616_models.ListServerGroupsResponse:
        """
        @summary Queries server groups in a region.
        
        @param request: ListServerGroupsRequest
        @return: ListServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_server_groups_with_options_async(request, runtime)

    def list_system_security_policies_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSystemSecurityPoliciesResponse:
        """
        @summary Queries system security policies in a region.
        
        @param request: ListSystemSecurityPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSystemSecurityPoliciesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSystemSecurityPolicies',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSystemSecurityPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_system_security_policies_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListSystemSecurityPoliciesResponse:
        """
        @summary Queries system security policies in a region.
        
        @param request: ListSystemSecurityPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSystemSecurityPoliciesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSystemSecurityPolicies',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListSystemSecurityPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_system_security_policies(self) -> alb_20200616_models.ListSystemSecurityPoliciesResponse:
        """
        @summary Queries system security policies in a region.
        
        @return: ListSystemSecurityPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_system_security_policies_with_options(runtime)

    async def list_system_security_policies_async(self) -> alb_20200616_models.ListSystemSecurityPoliciesResponse:
        """
        @summary Queries system security policies in a region.
        
        @return: ListSystemSecurityPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_system_security_policies_with_options_async(runtime)

    def list_tag_keys_with_options(
        self,
        request: alb_20200616_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagKeysResponse:
        """
        @summary Queries tag keys.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: alb_20200616_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagKeysResponse:
        """
        @summary Queries tag keys.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: alb_20200616_models.ListTagKeysRequest,
    ) -> alb_20200616_models.ListTagKeysResponse:
        """
        @summary Queries tag keys.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: alb_20200616_models.ListTagKeysRequest,
    ) -> alb_20200616_models.ListTagKeysResponse:
        """
        @summary Queries tag keys.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: alb_20200616_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of resources.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
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
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: alb_20200616_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of resources.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
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
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: alb_20200616_models.ListTagResourcesRequest,
    ) -> alb_20200616_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: alb_20200616_models.ListTagResourcesRequest,
    ) -> alb_20200616_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: alb_20200616_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagValuesResponse:
        """
        @summary Queries tag values.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            action='ListTagValues',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: alb_20200616_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ListTagValuesResponse:
        """
        @summary Queries tag values.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            action='ListTagValues',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: alb_20200616_models.ListTagValuesRequest,
    ) -> alb_20200616_models.ListTagValuesResponse:
        """
        @summary Queries tag values.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: alb_20200616_models.ListTagValuesRequest,
    ) -> alb_20200616_models.ListTagValuesResponse:
        """
        @summary Queries tag values.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: alb_20200616_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.MoveResourceGroupResponse:
        """
        @summary Moves a resource to another resource group.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: alb_20200616_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.MoveResourceGroupResponse:
        """
        @summary Moves a resource to another resource group.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: alb_20200616_models.MoveResourceGroupRequest,
    ) -> alb_20200616_models.MoveResourceGroupResponse:
        """
        @summary Moves a resource to another resource group.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: alb_20200616_models.MoveResourceGroupRequest,
    ) -> alb_20200616_models.MoveResourceGroupResponse:
        """
        @summary Moves a resource to another resource group.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def remove_entries_from_acl_with_options(
        self,
        request: alb_20200616_models.RemoveEntriesFromAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.RemoveEntriesFromAclResponse:
        """
        @summary Removes entries from an access control list (ACL).
        
        @description *RemoveEntriesFromAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclEntries](https://help.aliyun.com/document_detail/213616.html) operation to query the status of the task.
        If an ACL is in the **Removing** state, the entries are being removed.
        If an ACL cannot be found, the entries are removed.
        
        @param request: RemoveEntriesFromAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveEntriesFromAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.entries):
            query['Entries'] = request.entries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveEntriesFromAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.RemoveEntriesFromAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_entries_from_acl_with_options_async(
        self,
        request: alb_20200616_models.RemoveEntriesFromAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.RemoveEntriesFromAclResponse:
        """
        @summary Removes entries from an access control list (ACL).
        
        @description *RemoveEntriesFromAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclEntries](https://help.aliyun.com/document_detail/213616.html) operation to query the status of the task.
        If an ACL is in the **Removing** state, the entries are being removed.
        If an ACL cannot be found, the entries are removed.
        
        @param request: RemoveEntriesFromAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveEntriesFromAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.entries):
            query['Entries'] = request.entries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveEntriesFromAcl',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.RemoveEntriesFromAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_entries_from_acl(
        self,
        request: alb_20200616_models.RemoveEntriesFromAclRequest,
    ) -> alb_20200616_models.RemoveEntriesFromAclResponse:
        """
        @summary Removes entries from an access control list (ACL).
        
        @description *RemoveEntriesFromAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclEntries](https://help.aliyun.com/document_detail/213616.html) operation to query the status of the task.
        If an ACL is in the **Removing** state, the entries are being removed.
        If an ACL cannot be found, the entries are removed.
        
        @param request: RemoveEntriesFromAclRequest
        @return: RemoveEntriesFromAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_entries_from_acl_with_options(request, runtime)

    async def remove_entries_from_acl_async(
        self,
        request: alb_20200616_models.RemoveEntriesFromAclRequest,
    ) -> alb_20200616_models.RemoveEntriesFromAclResponse:
        """
        @summary Removes entries from an access control list (ACL).
        
        @description *RemoveEntriesFromAcl** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAclEntries](https://help.aliyun.com/document_detail/213616.html) operation to query the status of the task.
        If an ACL is in the **Removing** state, the entries are being removed.
        If an ACL cannot be found, the entries are removed.
        
        @param request: RemoveEntriesFromAclRequest
        @return: RemoveEntriesFromAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_entries_from_acl_with_options_async(request, runtime)

    def remove_servers_from_server_group_with_options(
        self,
        request: alb_20200616_models.RemoveServersFromServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.RemoveServersFromServerGroupResponse:
        """
        @summary Removes backend servers from a server group.
        
        @description *RemoveServersFromServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Removing** state, the server is being removed from the server group.
        If a backend server cannot be found, the server is no longer in the server group.
        
        @param request: RemoveServersFromServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveServersFromServerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            query['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveServersFromServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.RemoveServersFromServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_servers_from_server_group_with_options_async(
        self,
        request: alb_20200616_models.RemoveServersFromServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.RemoveServersFromServerGroupResponse:
        """
        @summary Removes backend servers from a server group.
        
        @description *RemoveServersFromServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Removing** state, the server is being removed from the server group.
        If a backend server cannot be found, the server is no longer in the server group.
        
        @param request: RemoveServersFromServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveServersFromServerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            query['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveServersFromServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.RemoveServersFromServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_servers_from_server_group(
        self,
        request: alb_20200616_models.RemoveServersFromServerGroupRequest,
    ) -> alb_20200616_models.RemoveServersFromServerGroupResponse:
        """
        @summary Removes backend servers from a server group.
        
        @description *RemoveServersFromServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Removing** state, the server is being removed from the server group.
        If a backend server cannot be found, the server is no longer in the server group.
        
        @param request: RemoveServersFromServerGroupRequest
        @return: RemoveServersFromServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_servers_from_server_group_with_options(request, runtime)

    async def remove_servers_from_server_group_async(
        self,
        request: alb_20200616_models.RemoveServersFromServerGroupRequest,
    ) -> alb_20200616_models.RemoveServersFromServerGroupResponse:
        """
        @summary Removes backend servers from a server group.
        
        @description *RemoveServersFromServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Removing** state, the server is being removed from the server group.
        If a backend server cannot be found, the server is no longer in the server group.
        
        @param request: RemoveServersFromServerGroupRequest
        @return: RemoveServersFromServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_servers_from_server_group_with_options_async(request, runtime)

    def replace_servers_in_server_group_with_options(
        self,
        request: alb_20200616_models.ReplaceServersInServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ReplaceServersInServerGroupResponse:
        """
        @summary Replaces backend servers in a server group.
        
        @description *ReplaceServersInServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Replacing** state, it indicates that the server is being removed from the server group and a new server is added to the server group.
        If a backend server is in the \\*\\*Available\\*\\* state, it indicates that the server is running.
        
        @param request: ReplaceServersInServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReplaceServersInServerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.added_servers):
            query['AddedServers'] = request.added_servers
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.removed_servers):
            query['RemovedServers'] = request.removed_servers
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceServersInServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ReplaceServersInServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_servers_in_server_group_with_options_async(
        self,
        request: alb_20200616_models.ReplaceServersInServerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.ReplaceServersInServerGroupResponse:
        """
        @summary Replaces backend servers in a server group.
        
        @description *ReplaceServersInServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Replacing** state, it indicates that the server is being removed from the server group and a new server is added to the server group.
        If a backend server is in the \\*\\*Available\\*\\* state, it indicates that the server is running.
        
        @param request: ReplaceServersInServerGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReplaceServersInServerGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.added_servers):
            query['AddedServers'] = request.added_servers
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.removed_servers):
            query['RemovedServers'] = request.removed_servers
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceServersInServerGroup',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.ReplaceServersInServerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_servers_in_server_group(
        self,
        request: alb_20200616_models.ReplaceServersInServerGroupRequest,
    ) -> alb_20200616_models.ReplaceServersInServerGroupResponse:
        """
        @summary Replaces backend servers in a server group.
        
        @description *ReplaceServersInServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Replacing** state, it indicates that the server is being removed from the server group and a new server is added to the server group.
        If a backend server is in the \\*\\*Available\\*\\* state, it indicates that the server is running.
        
        @param request: ReplaceServersInServerGroupRequest
        @return: ReplaceServersInServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.replace_servers_in_server_group_with_options(request, runtime)

    async def replace_servers_in_server_group_async(
        self,
        request: alb_20200616_models.ReplaceServersInServerGroupRequest,
    ) -> alb_20200616_models.ReplaceServersInServerGroupResponse:
        """
        @summary Replaces backend servers in a server group.
        
        @description *ReplaceServersInServerGroup** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Replacing** state, it indicates that the server is being removed from the server group and a new server is added to the server group.
        If a backend server is in the \\*\\*Available\\*\\* state, it indicates that the server is running.
        
        @param request: ReplaceServersInServerGroupRequest
        @return: ReplaceServersInServerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.replace_servers_in_server_group_with_options_async(request, runtime)

    def start_listener_with_options(
        self,
        request: alb_20200616_models.StartListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StartListenerResponse:
        """
        @summary Enables a listener.
        
        @description *StartListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) to query the status of the task.
        If a listener is in the **Configuring** state, the listener is being enabled.
        If a listener is in the **Running** state, the listener is enabled.
        
        @param request: StartListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.StartListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_listener_with_options_async(
        self,
        request: alb_20200616_models.StartListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StartListenerResponse:
        """
        @summary Enables a listener.
        
        @description *StartListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) to query the status of the task.
        If a listener is in the **Configuring** state, the listener is being enabled.
        If a listener is in the **Running** state, the listener is enabled.
        
        @param request: StartListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.StartListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_listener(
        self,
        request: alb_20200616_models.StartListenerRequest,
    ) -> alb_20200616_models.StartListenerResponse:
        """
        @summary Enables a listener.
        
        @description *StartListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) to query the status of the task.
        If a listener is in the **Configuring** state, the listener is being enabled.
        If a listener is in the **Running** state, the listener is enabled.
        
        @param request: StartListenerRequest
        @return: StartListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_listener_with_options(request, runtime)

    async def start_listener_async(
        self,
        request: alb_20200616_models.StartListenerRequest,
    ) -> alb_20200616_models.StartListenerResponse:
        """
        @summary Enables a listener.
        
        @description *StartListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) to query the status of the task.
        If a listener is in the **Configuring** state, the listener is being enabled.
        If a listener is in the **Running** state, the listener is enabled.
        
        @param request: StartListenerRequest
        @return: StartListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_listener_with_options_async(request, runtime)

    def start_shift_load_balancer_zones_with_options(
        self,
        request: alb_20200616_models.StartShiftLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StartShiftLoadBalancerZonesResponse:
        """
        @summary Removes an elastic IP address (EIP) or a virtual IP address (VIP) of a zone from a DNS record.
        
        @description This operation is supported by Application Load Balancer (ALB) instances that use static IP addresses. The zone cannot be removed if the ALB instance has only one available zone.
        
        @param request: StartShiftLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartShiftLoadBalancerZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartShiftLoadBalancerZones',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.StartShiftLoadBalancerZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_shift_load_balancer_zones_with_options_async(
        self,
        request: alb_20200616_models.StartShiftLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StartShiftLoadBalancerZonesResponse:
        """
        @summary Removes an elastic IP address (EIP) or a virtual IP address (VIP) of a zone from a DNS record.
        
        @description This operation is supported by Application Load Balancer (ALB) instances that use static IP addresses. The zone cannot be removed if the ALB instance has only one available zone.
        
        @param request: StartShiftLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartShiftLoadBalancerZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartShiftLoadBalancerZones',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.StartShiftLoadBalancerZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_shift_load_balancer_zones(
        self,
        request: alb_20200616_models.StartShiftLoadBalancerZonesRequest,
    ) -> alb_20200616_models.StartShiftLoadBalancerZonesResponse:
        """
        @summary Removes an elastic IP address (EIP) or a virtual IP address (VIP) of a zone from a DNS record.
        
        @description This operation is supported by Application Load Balancer (ALB) instances that use static IP addresses. The zone cannot be removed if the ALB instance has only one available zone.
        
        @param request: StartShiftLoadBalancerZonesRequest
        @return: StartShiftLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_shift_load_balancer_zones_with_options(request, runtime)

    async def start_shift_load_balancer_zones_async(
        self,
        request: alb_20200616_models.StartShiftLoadBalancerZonesRequest,
    ) -> alb_20200616_models.StartShiftLoadBalancerZonesResponse:
        """
        @summary Removes an elastic IP address (EIP) or a virtual IP address (VIP) of a zone from a DNS record.
        
        @description This operation is supported by Application Load Balancer (ALB) instances that use static IP addresses. The zone cannot be removed if the ALB instance has only one available zone.
        
        @param request: StartShiftLoadBalancerZonesRequest
        @return: StartShiftLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_shift_load_balancer_zones_with_options_async(request, runtime)

    def stop_listener_with_options(
        self,
        request: alb_20200616_models.StopListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StopListenerResponse:
        """
        @summary Disables a listener.
        
        @description *StopListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) operation to query the status of the task:
        If a listener is in the **Configuring** state, the listener is being disabled.
        If a listener is in the **Stopped** state, the listener is disabled.
        
        @param request: StopListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.StopListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_listener_with_options_async(
        self,
        request: alb_20200616_models.StopListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.StopListenerResponse:
        """
        @summary Disables a listener.
        
        @description *StopListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) operation to query the status of the task:
        If a listener is in the **Configuring** state, the listener is being disabled.
        If a listener is in the **Stopped** state, the listener is disabled.
        
        @param request: StopListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopListener',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.StopListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_listener(
        self,
        request: alb_20200616_models.StopListenerRequest,
    ) -> alb_20200616_models.StopListenerResponse:
        """
        @summary Disables a listener.
        
        @description *StopListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) operation to query the status of the task:
        If a listener is in the **Configuring** state, the listener is being disabled.
        If a listener is in the **Stopped** state, the listener is disabled.
        
        @param request: StopListenerRequest
        @return: StopListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_listener_with_options(request, runtime)

    async def stop_listener_async(
        self,
        request: alb_20200616_models.StopListenerRequest,
    ) -> alb_20200616_models.StopListenerResponse:
        """
        @summary Disables a listener.
        
        @description *StopListener** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) operation to query the status of the task:
        If a listener is in the **Configuring** state, the listener is being disabled.
        If a listener is in the **Stopped** state, the listener is disabled.
        
        @param request: StopListenerRequest
        @return: StopListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_listener_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: alb_20200616_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
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
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: alb_20200616_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
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
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: alb_20200616_models.TagResourcesRequest,
    ) -> alb_20200616_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: alb_20200616_models.TagResourcesRequest,
    ) -> alb_20200616_models.TagResourcesResponse:
        """
        @summary Adds tags to resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: alb_20200616_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UnTagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UnTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: alb_20200616_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UnTagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UnTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: alb_20200616_models.UnTagResourcesRequest,
    ) -> alb_20200616_models.UnTagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: alb_20200616_models.UnTagResourcesRequest,
    ) -> alb_20200616_models.UnTagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def update_ascripts_with_options(
        self,
        request: alb_20200616_models.UpdateAScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateAScriptsResponse:
        """
        @summary Updates AScript rules.
        
        @description    **UpdateAScripts** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAScripts](https://help.aliyun.com/document_detail/472574.html) operation to query the status of the task.
        If an AScript rule is in the **Configuring** state, the AScript rule is being updated.
        If an AScript rule is in the **Available** state, the AScript rule is updated.
        In the following table, the maximum value of **N** is **4**.
        
        @param request: UpdateAScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAScriptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascripts):
            query['AScripts'] = request.ascripts
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAScripts',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateAScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ascripts_with_options_async(
        self,
        request: alb_20200616_models.UpdateAScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateAScriptsResponse:
        """
        @summary Updates AScript rules.
        
        @description    **UpdateAScripts** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAScripts](https://help.aliyun.com/document_detail/472574.html) operation to query the status of the task.
        If an AScript rule is in the **Configuring** state, the AScript rule is being updated.
        If an AScript rule is in the **Available** state, the AScript rule is updated.
        In the following table, the maximum value of **N** is **4**.
        
        @param request: UpdateAScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAScriptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascripts):
            query['AScripts'] = request.ascripts
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAScripts',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateAScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ascripts(
        self,
        request: alb_20200616_models.UpdateAScriptsRequest,
    ) -> alb_20200616_models.UpdateAScriptsResponse:
        """
        @summary Updates AScript rules.
        
        @description    **UpdateAScripts** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAScripts](https://help.aliyun.com/document_detail/472574.html) operation to query the status of the task.
        If an AScript rule is in the **Configuring** state, the AScript rule is being updated.
        If an AScript rule is in the **Available** state, the AScript rule is updated.
        In the following table, the maximum value of **N** is **4**.
        
        @param request: UpdateAScriptsRequest
        @return: UpdateAScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ascripts_with_options(request, runtime)

    async def update_ascripts_async(
        self,
        request: alb_20200616_models.UpdateAScriptsRequest,
    ) -> alb_20200616_models.UpdateAScriptsResponse:
        """
        @summary Updates AScript rules.
        
        @description    **UpdateAScripts** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListAScripts](https://help.aliyun.com/document_detail/472574.html) operation to query the status of the task.
        If an AScript rule is in the **Configuring** state, the AScript rule is being updated.
        If an AScript rule is in the **Available** state, the AScript rule is updated.
        In the following table, the maximum value of **N** is **4**.
        
        @param request: UpdateAScriptsRequest
        @return: UpdateAScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ascripts_with_options_async(request, runtime)

    def update_acl_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateAclAttributeResponse:
        """
        @summary Updates the attributes of an access control list (ACL), such as the name.
        
        @param request: UpdateAclAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAclAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAclAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateAclAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_acl_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateAclAttributeResponse:
        """
        @summary Updates the attributes of an access control list (ACL), such as the name.
        
        @param request: UpdateAclAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAclAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAclAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateAclAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_acl_attribute(
        self,
        request: alb_20200616_models.UpdateAclAttributeRequest,
    ) -> alb_20200616_models.UpdateAclAttributeResponse:
        """
        @summary Updates the attributes of an access control list (ACL), such as the name.
        
        @param request: UpdateAclAttributeRequest
        @return: UpdateAclAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_acl_attribute_with_options(request, runtime)

    async def update_acl_attribute_async(
        self,
        request: alb_20200616_models.UpdateAclAttributeRequest,
    ) -> alb_20200616_models.UpdateAclAttributeResponse:
        """
        @summary Updates the attributes of an access control list (ACL), such as the name.
        
        @param request: UpdateAclAttributeRequest
        @return: UpdateAclAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_acl_attribute_with_options_async(request, runtime)

    def update_health_check_template_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateHealthCheckTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse:
        """
        @summary Modifies the attributes, such as the name and protocol, of a health check template.
        
        @param request: UpdateHealthCheckTemplateAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHealthCheckTemplateAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_codes):
            query['HealthCheckCodes'] = request.health_check_codes
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not UtilClient.is_unset(request.health_check_http_version):
            query['HealthCheckHttpVersion'] = request.health_check_http_version
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not UtilClient.is_unset(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not UtilClient.is_unset(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        if not UtilClient.is_unset(request.health_check_template_name):
            query['HealthCheckTemplateName'] = request.health_check_template_name
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHealthCheckTemplateAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_health_check_template_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateHealthCheckTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse:
        """
        @summary Modifies the attributes, such as the name and protocol, of a health check template.
        
        @param request: UpdateHealthCheckTemplateAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHealthCheckTemplateAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_codes):
            query['HealthCheckCodes'] = request.health_check_codes
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not UtilClient.is_unset(request.health_check_http_version):
            query['HealthCheckHttpVersion'] = request.health_check_http_version
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not UtilClient.is_unset(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not UtilClient.is_unset(request.health_check_template_id):
            query['HealthCheckTemplateId'] = request.health_check_template_id
        if not UtilClient.is_unset(request.health_check_template_name):
            query['HealthCheckTemplateName'] = request.health_check_template_name
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHealthCheckTemplateAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_health_check_template_attribute(
        self,
        request: alb_20200616_models.UpdateHealthCheckTemplateAttributeRequest,
    ) -> alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse:
        """
        @summary Modifies the attributes, such as the name and protocol, of a health check template.
        
        @param request: UpdateHealthCheckTemplateAttributeRequest
        @return: UpdateHealthCheckTemplateAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_health_check_template_attribute_with_options(request, runtime)

    async def update_health_check_template_attribute_async(
        self,
        request: alb_20200616_models.UpdateHealthCheckTemplateAttributeRequest,
    ) -> alb_20200616_models.UpdateHealthCheckTemplateAttributeResponse:
        """
        @summary Modifies the attributes, such as the name and protocol, of a health check template.
        
        @param request: UpdateHealthCheckTemplateAttributeRequest
        @return: UpdateHealthCheckTemplateAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_health_check_template_attribute_with_options_async(request, runtime)

    def update_listener_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateListenerAttributeResponse:
        """
        @summary Updates the attributes of a listener, such as the name and the default action.
        
        @description *UpdateListenerAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) operation to query the status of the task.
        If a listener is in the **Configuring** state, the configuration of the listener is being modified.
        If a listener is in the **Running** state, the configuration of the listener is modified.
        
        @param request: UpdateListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_certificates):
            query['CaCertificates'] = request.ca_certificates
        if not UtilClient.is_unset(request.ca_enabled):
            query['CaEnabled'] = request.ca_enabled
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_actions):
            query['DefaultActions'] = request.default_actions
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.gzip_enabled):
            query['GzipEnabled'] = request.gzip_enabled
        if not UtilClient.is_unset(request.http_2enabled):
            query['Http2Enabled'] = request.http_2enabled
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_description):
            query['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.quic_config):
            query['QuicConfig'] = request.quic_config
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateListenerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_listener_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateListenerAttributeResponse:
        """
        @summary Updates the attributes of a listener, such as the name and the default action.
        
        @description *UpdateListenerAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) operation to query the status of the task.
        If a listener is in the **Configuring** state, the configuration of the listener is being modified.
        If a listener is in the **Running** state, the configuration of the listener is modified.
        
        @param request: UpdateListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_certificates):
            query['CaCertificates'] = request.ca_certificates
        if not UtilClient.is_unset(request.ca_enabled):
            query['CaEnabled'] = request.ca_enabled
        if not UtilClient.is_unset(request.certificates):
            query['Certificates'] = request.certificates
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.default_actions):
            query['DefaultActions'] = request.default_actions
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.gzip_enabled):
            query['GzipEnabled'] = request.gzip_enabled
        if not UtilClient.is_unset(request.http_2enabled):
            query['Http2Enabled'] = request.http_2enabled
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_description):
            query['ListenerDescription'] = request.listener_description
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not UtilClient.is_unset(request.quic_config):
            query['QuicConfig'] = request.quic_config
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateListenerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_listener_attribute(
        self,
        request: alb_20200616_models.UpdateListenerAttributeRequest,
    ) -> alb_20200616_models.UpdateListenerAttributeResponse:
        """
        @summary Updates the attributes of a listener, such as the name and the default action.
        
        @description *UpdateListenerAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) operation to query the status of the task.
        If a listener is in the **Configuring** state, the configuration of the listener is being modified.
        If a listener is in the **Running** state, the configuration of the listener is modified.
        
        @param request: UpdateListenerAttributeRequest
        @return: UpdateListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_listener_attribute_with_options(request, runtime)

    async def update_listener_attribute_async(
        self,
        request: alb_20200616_models.UpdateListenerAttributeRequest,
    ) -> alb_20200616_models.UpdateListenerAttributeResponse:
        """
        @summary Updates the attributes of a listener, such as the name and the default action.
        
        @description *UpdateListenerAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) operation to query the status of the task.
        If a listener is in the **Configuring** state, the configuration of the listener is being modified.
        If a listener is in the **Running** state, the configuration of the listener is modified.
        
        @param request: UpdateListenerAttributeRequest
        @return: UpdateListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_listener_attribute_with_options_async(request, runtime)

    def update_listener_log_config_with_options(
        self,
        request: alb_20200616_models.UpdateListenerLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateListenerLogConfigResponse:
        """
        @summary Updates the log configuration of a listener, such as the access log configuration.
        
        @description *UpdateListenerLogConfig** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) to query the status of the task:
        If a listener is in the **Configuring** state, the log configuration of the listener is being modified.
        If a listener is in the **Running** state, the log configuration of the listener is modified.
        > You can update the log configuration of a listener only after you enable the access log feature.
        
        @param request: UpdateListenerLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateListenerLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_log_record_customized_headers_enabled):
            query['AccessLogRecordCustomizedHeadersEnabled'] = request.access_log_record_customized_headers_enabled
        if not UtilClient.is_unset(request.access_log_tracing_config):
            query['AccessLogTracingConfig'] = request.access_log_tracing_config
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateListenerLogConfig',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateListenerLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_listener_log_config_with_options_async(
        self,
        request: alb_20200616_models.UpdateListenerLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateListenerLogConfigResponse:
        """
        @summary Updates the log configuration of a listener, such as the access log configuration.
        
        @description *UpdateListenerLogConfig** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) to query the status of the task:
        If a listener is in the **Configuring** state, the log configuration of the listener is being modified.
        If a listener is in the **Running** state, the log configuration of the listener is modified.
        > You can update the log configuration of a listener only after you enable the access log feature.
        
        @param request: UpdateListenerLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateListenerLogConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_log_record_customized_headers_enabled):
            query['AccessLogRecordCustomizedHeadersEnabled'] = request.access_log_record_customized_headers_enabled
        if not UtilClient.is_unset(request.access_log_tracing_config):
            query['AccessLogTracingConfig'] = request.access_log_tracing_config
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateListenerLogConfig',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateListenerLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_listener_log_config(
        self,
        request: alb_20200616_models.UpdateListenerLogConfigRequest,
    ) -> alb_20200616_models.UpdateListenerLogConfigResponse:
        """
        @summary Updates the log configuration of a listener, such as the access log configuration.
        
        @description *UpdateListenerLogConfig** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) to query the status of the task:
        If a listener is in the **Configuring** state, the log configuration of the listener is being modified.
        If a listener is in the **Running** state, the log configuration of the listener is modified.
        > You can update the log configuration of a listener only after you enable the access log feature.
        
        @param request: UpdateListenerLogConfigRequest
        @return: UpdateListenerLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_listener_log_config_with_options(request, runtime)

    async def update_listener_log_config_async(
        self,
        request: alb_20200616_models.UpdateListenerLogConfigRequest,
    ) -> alb_20200616_models.UpdateListenerLogConfigResponse:
        """
        @summary Updates the log configuration of a listener, such as the access log configuration.
        
        @description *UpdateListenerLogConfig** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetListenerAttribute](https://help.aliyun.com/document_detail/2254865.html) to query the status of the task:
        If a listener is in the **Configuring** state, the log configuration of the listener is being modified.
        If a listener is in the **Running** state, the log configuration of the listener is modified.
        > You can update the log configuration of a listener only after you enable the access log feature.
        
        @param request: UpdateListenerLogConfigRequest
        @return: UpdateListenerLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_listener_log_config_with_options_async(request, runtime)

    def update_load_balancer_address_type_config_with_options(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAddressTypeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerAddressTypeConfigResponse:
        """
        @summary Modifies the network type of an Application Load Balancer (ALB) instance.
        
        @description ## Prerequisites
        An ALB instance is created. For more information about how to create an ALB instance, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html).
        If you want to change the network type from internal-facing to Internet-facing, you must first create an elastic IP address (EIP). For more information, see [AllocateEipAddress](https://help.aliyun.com/document_detail/120192.html).
        ## Usage notes
        *UpdateLoadBalancerAddressTypeConfig** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of the task.
        If an ALB instance is in the **Configuring** state, the network type is being changed.
        If an ALB instance is in the **Active** state, the network type has been changed.
        
        @param request: UpdateLoadBalancerAddressTypeConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerAddressTypeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAddressTypeConfig',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerAddressTypeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_address_type_config_with_options_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAddressTypeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerAddressTypeConfigResponse:
        """
        @summary Modifies the network type of an Application Load Balancer (ALB) instance.
        
        @description ## Prerequisites
        An ALB instance is created. For more information about how to create an ALB instance, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html).
        If you want to change the network type from internal-facing to Internet-facing, you must first create an elastic IP address (EIP). For more information, see [AllocateEipAddress](https://help.aliyun.com/document_detail/120192.html).
        ## Usage notes
        *UpdateLoadBalancerAddressTypeConfig** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of the task.
        If an ALB instance is in the **Configuring** state, the network type is being changed.
        If an ALB instance is in the **Active** state, the network type has been changed.
        
        @param request: UpdateLoadBalancerAddressTypeConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerAddressTypeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAddressTypeConfig',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerAddressTypeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_address_type_config(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAddressTypeConfigRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerAddressTypeConfigResponse:
        """
        @summary Modifies the network type of an Application Load Balancer (ALB) instance.
        
        @description ## Prerequisites
        An ALB instance is created. For more information about how to create an ALB instance, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html).
        If you want to change the network type from internal-facing to Internet-facing, you must first create an elastic IP address (EIP). For more information, see [AllocateEipAddress](https://help.aliyun.com/document_detail/120192.html).
        ## Usage notes
        *UpdateLoadBalancerAddressTypeConfig** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of the task.
        If an ALB instance is in the **Configuring** state, the network type is being changed.
        If an ALB instance is in the **Active** state, the network type has been changed.
        
        @param request: UpdateLoadBalancerAddressTypeConfigRequest
        @return: UpdateLoadBalancerAddressTypeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_address_type_config_with_options(request, runtime)

    async def update_load_balancer_address_type_config_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAddressTypeConfigRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerAddressTypeConfigResponse:
        """
        @summary Modifies the network type of an Application Load Balancer (ALB) instance.
        
        @description ## Prerequisites
        An ALB instance is created. For more information about how to create an ALB instance, see [CreateLoadBalancer](https://help.aliyun.com/document_detail/214358.html).
        If you want to change the network type from internal-facing to Internet-facing, you must first create an elastic IP address (EIP). For more information, see [AllocateEipAddress](https://help.aliyun.com/document_detail/120192.html).
        ## Usage notes
        *UpdateLoadBalancerAddressTypeConfig** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) operation to query the status of the task.
        If an ALB instance is in the **Configuring** state, the network type is being changed.
        If an ALB instance is in the **Active** state, the network type has been changed.
        
        @param request: UpdateLoadBalancerAddressTypeConfigRequest
        @return: UpdateLoadBalancerAddressTypeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_address_type_config_with_options_async(request, runtime)

    def update_load_balancer_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerAttributeResponse:
        """
        @summary Modifies the attributes of an Application Load Balancer (ALB) instance, such as the name and the configuration read-only mode.
        
        @description *UpdateLoadBalancerAttribute** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If the ALB instance is in the **Configuring** state, the ALB instance is being modified.
        If the ALB instance is in the **Active** state, the ALB instance is modified.
        
        @param request: UpdateLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.modification_protection_config):
            query['ModificationProtectionConfig'] = request.modification_protection_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerAttributeResponse:
        """
        @summary Modifies the attributes of an Application Load Balancer (ALB) instance, such as the name and the configuration read-only mode.
        
        @description *UpdateLoadBalancerAttribute** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If the ALB instance is in the **Configuring** state, the ALB instance is being modified.
        If the ALB instance is in the **Active** state, the ALB instance is modified.
        
        @param request: UpdateLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.modification_protection_config):
            query['ModificationProtectionConfig'] = request.modification_protection_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_attribute(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAttributeRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerAttributeResponse:
        """
        @summary Modifies the attributes of an Application Load Balancer (ALB) instance, such as the name and the configuration read-only mode.
        
        @description *UpdateLoadBalancerAttribute** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If the ALB instance is in the **Configuring** state, the ALB instance is being modified.
        If the ALB instance is in the **Active** state, the ALB instance is modified.
        
        @param request: UpdateLoadBalancerAttributeRequest
        @return: UpdateLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_attribute_with_options(request, runtime)

    async def update_load_balancer_attribute_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerAttributeRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerAttributeResponse:
        """
        @summary Modifies the attributes of an Application Load Balancer (ALB) instance, such as the name and the configuration read-only mode.
        
        @description *UpdateLoadBalancerAttribute** is an asynchronous operation. After you send a request, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If the ALB instance is in the **Configuring** state, the ALB instance is being modified.
        If the ALB instance is in the **Active** state, the ALB instance is modified.
        
        @param request: UpdateLoadBalancerAttributeRequest
        @return: UpdateLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_attribute_with_options_async(request, runtime)

    def update_load_balancer_edition_with_options(
        self,
        request: alb_20200616_models.UpdateLoadBalancerEditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerEditionResponse:
        """
        @summary Changes the edition of an Application Load Balancer (ALB) instance.
        
        @description ##
        You can upgrade a basic ALB instance to a standard ALB instance or a WAF-enabled ALB instance but you cannot downgrade a standard ALB instance or a WAF-enabled ALB instance to a basic ALB instance. For more information, see [Upgrade an ALB instance](https://help.aliyun.com/document_detail/214654.html).
        **UpdateLoadBalancerEdition** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If the ALB instance is in the **Configuring** state, the edition of the ALB instance is being modified.
        If the ALB instance is in the **Active** state, the edition of the ALB instance has been modified.
        
        @param request: UpdateLoadBalancerEditionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerEditionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerEdition',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerEditionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_edition_with_options_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerEditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerEditionResponse:
        """
        @summary Changes the edition of an Application Load Balancer (ALB) instance.
        
        @description ##
        You can upgrade a basic ALB instance to a standard ALB instance or a WAF-enabled ALB instance but you cannot downgrade a standard ALB instance or a WAF-enabled ALB instance to a basic ALB instance. For more information, see [Upgrade an ALB instance](https://help.aliyun.com/document_detail/214654.html).
        **UpdateLoadBalancerEdition** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If the ALB instance is in the **Configuring** state, the edition of the ALB instance is being modified.
        If the ALB instance is in the **Active** state, the edition of the ALB instance has been modified.
        
        @param request: UpdateLoadBalancerEditionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerEditionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_edition):
            query['LoadBalancerEdition'] = request.load_balancer_edition
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerEdition',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerEditionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_edition(
        self,
        request: alb_20200616_models.UpdateLoadBalancerEditionRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerEditionResponse:
        """
        @summary Changes the edition of an Application Load Balancer (ALB) instance.
        
        @description ##
        You can upgrade a basic ALB instance to a standard ALB instance or a WAF-enabled ALB instance but you cannot downgrade a standard ALB instance or a WAF-enabled ALB instance to a basic ALB instance. For more information, see [Upgrade an ALB instance](https://help.aliyun.com/document_detail/214654.html).
        **UpdateLoadBalancerEdition** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If the ALB instance is in the **Configuring** state, the edition of the ALB instance is being modified.
        If the ALB instance is in the **Active** state, the edition of the ALB instance has been modified.
        
        @param request: UpdateLoadBalancerEditionRequest
        @return: UpdateLoadBalancerEditionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_edition_with_options(request, runtime)

    async def update_load_balancer_edition_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerEditionRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerEditionResponse:
        """
        @summary Changes the edition of an Application Load Balancer (ALB) instance.
        
        @description ##
        You can upgrade a basic ALB instance to a standard ALB instance or a WAF-enabled ALB instance but you cannot downgrade a standard ALB instance or a WAF-enabled ALB instance to a basic ALB instance. For more information, see [Upgrade an ALB instance](https://help.aliyun.com/document_detail/214654.html).
        **UpdateLoadBalancerEdition** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If the ALB instance is in the **Configuring** state, the edition of the ALB instance is being modified.
        If the ALB instance is in the **Active** state, the edition of the ALB instance has been modified.
        
        @param request: UpdateLoadBalancerEditionRequest
        @return: UpdateLoadBalancerEditionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_edition_with_options_async(request, runtime)

    def update_load_balancer_zones_with_options(
        self,
        request: alb_20200616_models.UpdateLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerZonesResponse:
        """
        @summary Modifies the zones of an Application Load Balancer (ALB) instance.
        
        @description *UpdateLoadBalancerZones** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If an ALB instance is in the **Configuring** state, the zones are being modified.
        If an ALB instance is in the **Active** state, the zones are modified.
        > You may be charged after you call UpdateLoadBalancerZones.
        
        @param request: UpdateLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerZones',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_load_balancer_zones_with_options_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateLoadBalancerZonesResponse:
        """
        @summary Modifies the zones of an Application Load Balancer (ALB) instance.
        
        @description *UpdateLoadBalancerZones** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If an ALB instance is in the **Configuring** state, the zones are being modified.
        If an ALB instance is in the **Active** state, the zones are modified.
        > You may be charged after you call UpdateLoadBalancerZones.
        
        @param request: UpdateLoadBalancerZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoadBalancerZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.zone_mappings):
            query['ZoneMappings'] = request.zone_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLoadBalancerZones',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateLoadBalancerZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_load_balancer_zones(
        self,
        request: alb_20200616_models.UpdateLoadBalancerZonesRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerZonesResponse:
        """
        @summary Modifies the zones of an Application Load Balancer (ALB) instance.
        
        @description *UpdateLoadBalancerZones** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If an ALB instance is in the **Configuring** state, the zones are being modified.
        If an ALB instance is in the **Active** state, the zones are modified.
        > You may be charged after you call UpdateLoadBalancerZones.
        
        @param request: UpdateLoadBalancerZonesRequest
        @return: UpdateLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_load_balancer_zones_with_options(request, runtime)

    async def update_load_balancer_zones_async(
        self,
        request: alb_20200616_models.UpdateLoadBalancerZonesRequest,
    ) -> alb_20200616_models.UpdateLoadBalancerZonesResponse:
        """
        @summary Modifies the zones of an Application Load Balancer (ALB) instance.
        
        @description *UpdateLoadBalancerZones** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [GetLoadBalancerAttribute](https://help.aliyun.com/document_detail/214362.html) to query the status of the task.
        If an ALB instance is in the **Configuring** state, the zones are being modified.
        If an ALB instance is in the **Active** state, the zones are modified.
        > You may be charged after you call UpdateLoadBalancerZones.
        
        @param request: UpdateLoadBalancerZonesRequest
        @return: UpdateLoadBalancerZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_load_balancer_zones_with_options_async(request, runtime)

    def update_rule_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateRuleAttributeResponse:
        """
        @summary Updates a forwarding rule, such as the match condition, action, and name.
        
        @description    **UpdateRuleAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of a forwarding rule:
        If a forwarding rule is in the **Configuring** state, the forwarding rule is being updated.
        If a forwarding rule is in the **Available** state, the forwarding rule is updated.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. Take note of the following limits on the number of conditions and the number of actions in each forwarding rule:
        Number of conditions: You can specify at most 5 for a basic Application Load Balancer (ALB) instance, at most 10 for a standard ALB instance, and at most 10 for a WAF-enabled ALB instance.
        Number of actions: You can specify at most 3 for a basic ALB instance, at most 5 for a standard ALB instance, and at most 5 for a WAF-enabled ALB instance.
        
        @param request: UpdateRuleAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRuleAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rule_actions):
            query['RuleActions'] = request.rule_actions
        if not UtilClient.is_unset(request.rule_conditions):
            query['RuleConditions'] = request.rule_conditions
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRuleAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateRuleAttributeResponse:
        """
        @summary Updates a forwarding rule, such as the match condition, action, and name.
        
        @description    **UpdateRuleAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of a forwarding rule:
        If a forwarding rule is in the **Configuring** state, the forwarding rule is being updated.
        If a forwarding rule is in the **Available** state, the forwarding rule is updated.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. Take note of the following limits on the number of conditions and the number of actions in each forwarding rule:
        Number of conditions: You can specify at most 5 for a basic Application Load Balancer (ALB) instance, at most 10 for a standard ALB instance, and at most 10 for a WAF-enabled ALB instance.
        Number of actions: You can specify at most 3 for a basic ALB instance, at most 5 for a standard ALB instance, and at most 5 for a WAF-enabled ALB instance.
        
        @param request: UpdateRuleAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRuleAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rule_actions):
            query['RuleActions'] = request.rule_actions
        if not UtilClient.is_unset(request.rule_conditions):
            query['RuleConditions'] = request.rule_conditions
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRuleAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateRuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule_attribute(
        self,
        request: alb_20200616_models.UpdateRuleAttributeRequest,
    ) -> alb_20200616_models.UpdateRuleAttributeResponse:
        """
        @summary Updates a forwarding rule, such as the match condition, action, and name.
        
        @description    **UpdateRuleAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of a forwarding rule:
        If a forwarding rule is in the **Configuring** state, the forwarding rule is being updated.
        If a forwarding rule is in the **Available** state, the forwarding rule is updated.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. Take note of the following limits on the number of conditions and the number of actions in each forwarding rule:
        Number of conditions: You can specify at most 5 for a basic Application Load Balancer (ALB) instance, at most 10 for a standard ALB instance, and at most 10 for a WAF-enabled ALB instance.
        Number of actions: You can specify at most 3 for a basic ALB instance, at most 5 for a standard ALB instance, and at most 5 for a WAF-enabled ALB instance.
        
        @param request: UpdateRuleAttributeRequest
        @return: UpdateRuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rule_attribute_with_options(request, runtime)

    async def update_rule_attribute_async(
        self,
        request: alb_20200616_models.UpdateRuleAttributeRequest,
    ) -> alb_20200616_models.UpdateRuleAttributeResponse:
        """
        @summary Updates a forwarding rule, such as the match condition, action, and name.
        
        @description    **UpdateRuleAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of a forwarding rule:
        If a forwarding rule is in the **Configuring** state, the forwarding rule is being updated.
        If a forwarding rule is in the **Available** state, the forwarding rule is updated.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. Take note of the following limits on the number of conditions and the number of actions in each forwarding rule:
        Number of conditions: You can specify at most 5 for a basic Application Load Balancer (ALB) instance, at most 10 for a standard ALB instance, and at most 10 for a WAF-enabled ALB instance.
        Number of actions: You can specify at most 3 for a basic ALB instance, at most 5 for a standard ALB instance, and at most 5 for a WAF-enabled ALB instance.
        
        @param request: UpdateRuleAttributeRequest
        @return: UpdateRuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_attribute_with_options_async(request, runtime)

    def update_rules_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateRulesAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateRulesAttributeResponse:
        """
        @summary Modifies the attributes of forwarding rules.
        
        @description *UpdateRulesAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of the task.
        If a forwarding rule is in the **Configuring** state, the forwarding rule is being updated.
        If a forwarding rule is in the **Available** state, the forwarding rule is updated.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. Take note of the following limits on the maximum number of conditions and the maximum number of actions in each forwarding rule:
        Limits on conditions: 5 for a basic Application Load Balancer (ALB) instance, 10 for a standard ALB instance, and 10 for a WAF-enabled ALB instance.
        Limits on actions: 3 for a basic ALB instance, 5 for a standard ALB instance, and 5 for a WAF-enabled ALB instance.
        
        @param request: UpdateRulesAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRulesAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRulesAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateRulesAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rules_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateRulesAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateRulesAttributeResponse:
        """
        @summary Modifies the attributes of forwarding rules.
        
        @description *UpdateRulesAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of the task.
        If a forwarding rule is in the **Configuring** state, the forwarding rule is being updated.
        If a forwarding rule is in the **Available** state, the forwarding rule is updated.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. Take note of the following limits on the maximum number of conditions and the maximum number of actions in each forwarding rule:
        Limits on conditions: 5 for a basic Application Load Balancer (ALB) instance, 10 for a standard ALB instance, and 10 for a WAF-enabled ALB instance.
        Limits on actions: 3 for a basic ALB instance, 5 for a standard ALB instance, and 5 for a WAF-enabled ALB instance.
        
        @param request: UpdateRulesAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRulesAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.rules):
            query['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRulesAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateRulesAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rules_attribute(
        self,
        request: alb_20200616_models.UpdateRulesAttributeRequest,
    ) -> alb_20200616_models.UpdateRulesAttributeResponse:
        """
        @summary Modifies the attributes of forwarding rules.
        
        @description *UpdateRulesAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of the task.
        If a forwarding rule is in the **Configuring** state, the forwarding rule is being updated.
        If a forwarding rule is in the **Available** state, the forwarding rule is updated.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. Take note of the following limits on the maximum number of conditions and the maximum number of actions in each forwarding rule:
        Limits on conditions: 5 for a basic Application Load Balancer (ALB) instance, 10 for a standard ALB instance, and 10 for a WAF-enabled ALB instance.
        Limits on actions: 3 for a basic ALB instance, 5 for a standard ALB instance, and 5 for a WAF-enabled ALB instance.
        
        @param request: UpdateRulesAttributeRequest
        @return: UpdateRulesAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rules_attribute_with_options(request, runtime)

    async def update_rules_attribute_async(
        self,
        request: alb_20200616_models.UpdateRulesAttributeRequest,
    ) -> alb_20200616_models.UpdateRulesAttributeResponse:
        """
        @summary Modifies the attributes of forwarding rules.
        
        @description *UpdateRulesAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListRules](https://help.aliyun.com/document_detail/214379.html) operation to query the status of the task.
        If a forwarding rule is in the **Configuring** state, the forwarding rule is being updated.
        If a forwarding rule is in the **Available** state, the forwarding rule is updated.
        You can set **RuleConditions** and **RuleActions** to add conditions and actions to a forwarding rule. Take note of the following limits on the maximum number of conditions and the maximum number of actions in each forwarding rule:
        Limits on conditions: 5 for a basic Application Load Balancer (ALB) instance, 10 for a standard ALB instance, and 10 for a WAF-enabled ALB instance.
        Limits on actions: 3 for a basic ALB instance, 5 for a standard ALB instance, and 5 for a WAF-enabled ALB instance.
        
        @param request: UpdateRulesAttributeRequest
        @return: UpdateRulesAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_rules_attribute_with_options_async(request, runtime)

    def update_security_policy_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateSecurityPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateSecurityPolicyAttributeResponse:
        """
        @summary Updates the attributes of a security policy, such as the TLS protocol version and the supported cipher suites.
        
        @description ##
        *UpdateSecurityPolicyAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [ListSecurityPolicies](https://help.aliyun.com/document_detail/213609.html) to query the status of the task.
        If a security policy is in the **Configuring** state, the security policy is being updated.
        If a security policy is in the **Available** state, the security policy is updated.
        
        @param request: UpdateSecurityPolicyAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecurityPolicyAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.security_policy_name):
            query['SecurityPolicyName'] = request.security_policy_name
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecurityPolicyAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateSecurityPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_security_policy_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateSecurityPolicyAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateSecurityPolicyAttributeResponse:
        """
        @summary Updates the attributes of a security policy, such as the TLS protocol version and the supported cipher suites.
        
        @description ##
        *UpdateSecurityPolicyAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [ListSecurityPolicies](https://help.aliyun.com/document_detail/213609.html) to query the status of the task.
        If a security policy is in the **Configuring** state, the security policy is being updated.
        If a security policy is in the **Available** state, the security policy is updated.
        
        @param request: UpdateSecurityPolicyAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSecurityPolicyAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not UtilClient.is_unset(request.security_policy_name):
            query['SecurityPolicyName'] = request.security_policy_name
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSecurityPolicyAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateSecurityPolicyAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_security_policy_attribute(
        self,
        request: alb_20200616_models.UpdateSecurityPolicyAttributeRequest,
    ) -> alb_20200616_models.UpdateSecurityPolicyAttributeResponse:
        """
        @summary Updates the attributes of a security policy, such as the TLS protocol version and the supported cipher suites.
        
        @description ##
        *UpdateSecurityPolicyAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [ListSecurityPolicies](https://help.aliyun.com/document_detail/213609.html) to query the status of the task.
        If a security policy is in the **Configuring** state, the security policy is being updated.
        If a security policy is in the **Available** state, the security policy is updated.
        
        @param request: UpdateSecurityPolicyAttributeRequest
        @return: UpdateSecurityPolicyAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_security_policy_attribute_with_options(request, runtime)

    async def update_security_policy_attribute_async(
        self,
        request: alb_20200616_models.UpdateSecurityPolicyAttributeRequest,
    ) -> alb_20200616_models.UpdateSecurityPolicyAttributeResponse:
        """
        @summary Updates the attributes of a security policy, such as the TLS protocol version and the supported cipher suites.
        
        @description ##
        *UpdateSecurityPolicyAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call [ListSecurityPolicies](https://help.aliyun.com/document_detail/213609.html) to query the status of the task.
        If a security policy is in the **Configuring** state, the security policy is being updated.
        If a security policy is in the **Available** state, the security policy is updated.
        
        @param request: UpdateSecurityPolicyAttributeRequest
        @return: UpdateSecurityPolicyAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_security_policy_attribute_with_options_async(request, runtime)

    def update_server_group_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateServerGroupAttributeResponse:
        """
        @summary Modifies the configurations of a server group, such as health checks, session persistence, server group names, routing algorithms, and protocols.
        
        @description ## Description
        *UpdateServerGroupAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group:
        If a server group is in the **Configuring** state, the configuration of the server group is being modified.
        If a server group is in the **Available** state, the configuration of the server group is modified.
        
        @param request: UpdateServerGroupAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServerGroupAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_drain_config):
            query['ConnectionDrainConfig'] = request.connection_drain_config
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_config):
            query['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_group_name):
            query['ServerGroupName'] = request.server_group_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.slow_start_config):
            query['SlowStartConfig'] = request.slow_start_config
        if not UtilClient.is_unset(request.sticky_session_config):
            query['StickySessionConfig'] = request.sticky_session_config
        if not UtilClient.is_unset(request.uch_config):
            query['UchConfig'] = request.uch_config
        if not UtilClient.is_unset(request.upstream_keepalive_enabled):
            query['UpstreamKeepaliveEnabled'] = request.upstream_keepalive_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_server_group_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateServerGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateServerGroupAttributeResponse:
        """
        @summary Modifies the configurations of a server group, such as health checks, session persistence, server group names, routing algorithms, and protocols.
        
        @description ## Description
        *UpdateServerGroupAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group:
        If a server group is in the **Configuring** state, the configuration of the server group is being modified.
        If a server group is in the **Available** state, the configuration of the server group is modified.
        
        @param request: UpdateServerGroupAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServerGroupAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.connection_drain_config):
            query['ConnectionDrainConfig'] = request.connection_drain_config
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.health_check_config):
            query['HealthCheckConfig'] = request.health_check_config
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.server_group_name):
            query['ServerGroupName'] = request.server_group_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.slow_start_config):
            query['SlowStartConfig'] = request.slow_start_config
        if not UtilClient.is_unset(request.sticky_session_config):
            query['StickySessionConfig'] = request.sticky_session_config
        if not UtilClient.is_unset(request.uch_config):
            query['UchConfig'] = request.uch_config
        if not UtilClient.is_unset(request.upstream_keepalive_enabled):
            query['UpstreamKeepaliveEnabled'] = request.upstream_keepalive_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateServerGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_server_group_attribute(
        self,
        request: alb_20200616_models.UpdateServerGroupAttributeRequest,
    ) -> alb_20200616_models.UpdateServerGroupAttributeResponse:
        """
        @summary Modifies the configurations of a server group, such as health checks, session persistence, server group names, routing algorithms, and protocols.
        
        @description ## Description
        *UpdateServerGroupAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group:
        If a server group is in the **Configuring** state, the configuration of the server group is being modified.
        If a server group is in the **Available** state, the configuration of the server group is modified.
        
        @param request: UpdateServerGroupAttributeRequest
        @return: UpdateServerGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_server_group_attribute_with_options(request, runtime)

    async def update_server_group_attribute_async(
        self,
        request: alb_20200616_models.UpdateServerGroupAttributeRequest,
    ) -> alb_20200616_models.UpdateServerGroupAttributeResponse:
        """
        @summary Modifies the configurations of a server group, such as health checks, session persistence, server group names, routing algorithms, and protocols.
        
        @description ## Description
        *UpdateServerGroupAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group:
        If a server group is in the **Configuring** state, the configuration of the server group is being modified.
        If a server group is in the **Available** state, the configuration of the server group is modified.
        
        @param request: UpdateServerGroupAttributeRequest
        @return: UpdateServerGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_server_group_attribute_with_options_async(request, runtime)

    def update_server_group_servers_attribute_with_options(
        self,
        request: alb_20200616_models.UpdateServerGroupServersAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateServerGroupServersAttributeResponse:
        """
        @summary Modifies the configurations, such as the backend server weight and description, of a server group.
        
        @description *UpdateServerGroupServersAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Configuring** state, it indicates that the backend server is being modified.
        If a backend server is in the **Available** state, it indicates that the backend server is running.
        
        @param request: UpdateServerGroupServersAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServerGroupServersAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            query['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupServersAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateServerGroupServersAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_server_group_servers_attribute_with_options_async(
        self,
        request: alb_20200616_models.UpdateServerGroupServersAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> alb_20200616_models.UpdateServerGroupServersAttributeResponse:
        """
        @summary Modifies the configurations, such as the backend server weight and description, of a server group.
        
        @description *UpdateServerGroupServersAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Configuring** state, it indicates that the backend server is being modified.
        If a backend server is in the **Available** state, it indicates that the backend server is running.
        
        @param request: UpdateServerGroupServersAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServerGroupServersAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.server_group_id):
            query['ServerGroupId'] = request.server_group_id
        if not UtilClient.is_unset(request.servers):
            query['Servers'] = request.servers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServerGroupServersAttribute',
            version='2020-06-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alb_20200616_models.UpdateServerGroupServersAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_server_group_servers_attribute(
        self,
        request: alb_20200616_models.UpdateServerGroupServersAttributeRequest,
    ) -> alb_20200616_models.UpdateServerGroupServersAttributeResponse:
        """
        @summary Modifies the configurations, such as the backend server weight and description, of a server group.
        
        @description *UpdateServerGroupServersAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Configuring** state, it indicates that the backend server is being modified.
        If a backend server is in the **Available** state, it indicates that the backend server is running.
        
        @param request: UpdateServerGroupServersAttributeRequest
        @return: UpdateServerGroupServersAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_server_group_servers_attribute_with_options(request, runtime)

    async def update_server_group_servers_attribute_async(
        self,
        request: alb_20200616_models.UpdateServerGroupServersAttributeRequest,
    ) -> alb_20200616_models.UpdateServerGroupServersAttributeResponse:
        """
        @summary Modifies the configurations, such as the backend server weight and description, of a server group.
        
        @description *UpdateServerGroupServersAttribute** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background.
        1.  You can call the [ListServerGroups](https://help.aliyun.com/document_detail/213627.html) operation to query the status of a server group.
        If a server group is in the **Configuring** state, it indicates that the server group is being modified.
        If a server group is in the **Available** state, it indicates that the server group is running.
        2.  You can call the [ListServerGroupServers](https://help.aliyun.com/document_detail/213628.html) operation to query the status of a backend server.
        If a backend server is in the **Configuring** state, it indicates that the backend server is being modified.
        If a backend server is in the **Available** state, it indicates that the backend server is running.
        
        @param request: UpdateServerGroupServersAttributeRequest
        @return: UpdateServerGroupServersAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_server_group_servers_attribute_with_options_async(request, runtime)
