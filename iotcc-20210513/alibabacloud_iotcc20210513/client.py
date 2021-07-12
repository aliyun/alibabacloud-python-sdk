# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iotcc20210513 import models as io_tcc20210513_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('iotcc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def delete_service_with_options(
        self,
        request: io_tcc20210513_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DeleteServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteServiceResponse(),
            self.do_rpcrequest('DeleteService', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        request: io_tcc20210513_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DeleteServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteServiceResponse(),
            await self.do_rpcrequest_async('DeleteService', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_service(
        self,
        request: io_tcc20210513_models.DeleteServiceRequest,
    ) -> io_tcc20210513_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    async def delete_service_async(
        self,
        request: io_tcc20210513_models.DeleteServiceRequest,
    ) -> io_tcc20210513_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_with_options_async(request, runtime)

    def delete_service_entry_with_options(
        self,
        request: io_tcc20210513_models.DeleteServiceEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DeleteServiceEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteServiceEntryResponse(),
            self.do_rpcrequest('DeleteServiceEntry', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_service_entry_with_options_async(
        self,
        request: io_tcc20210513_models.DeleteServiceEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DeleteServiceEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteServiceEntryResponse(),
            await self.do_rpcrequest_async('DeleteServiceEntry', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_service_entry(
        self,
        request: io_tcc20210513_models.DeleteServiceEntryRequest,
    ) -> io_tcc20210513_models.DeleteServiceEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_entry_with_options(request, runtime)

    async def delete_service_entry_async(
        self,
        request: io_tcc20210513_models.DeleteServiceEntryRequest,
    ) -> io_tcc20210513_models.DeleteServiceEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_entry_with_options_async(request, runtime)

    def update_service_entry_attribute_with_options(
        self,
        request: io_tcc20210513_models.UpdateServiceEntryAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.UpdateServiceEntryAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateServiceEntryAttributeResponse(),
            self.do_rpcrequest('UpdateServiceEntryAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_service_entry_attribute_with_options_async(
        self,
        request: io_tcc20210513_models.UpdateServiceEntryAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.UpdateServiceEntryAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateServiceEntryAttributeResponse(),
            await self.do_rpcrequest_async('UpdateServiceEntryAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_service_entry_attribute(
        self,
        request: io_tcc20210513_models.UpdateServiceEntryAttributeRequest,
    ) -> io_tcc20210513_models.UpdateServiceEntryAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_service_entry_attribute_with_options(request, runtime)

    async def update_service_entry_attribute_async(
        self,
        request: io_tcc20210513_models.UpdateServiceEntryAttributeRequest,
    ) -> io_tcc20210513_models.UpdateServiceEntryAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_service_entry_attribute_with_options_async(request, runtime)

    def update_service_attribute_with_options(
        self,
        request: io_tcc20210513_models.UpdateServiceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.UpdateServiceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateServiceAttributeResponse(),
            self.do_rpcrequest('UpdateServiceAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_service_attribute_with_options_async(
        self,
        request: io_tcc20210513_models.UpdateServiceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.UpdateServiceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateServiceAttributeResponse(),
            await self.do_rpcrequest_async('UpdateServiceAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_service_attribute(
        self,
        request: io_tcc20210513_models.UpdateServiceAttributeRequest,
    ) -> io_tcc20210513_models.UpdateServiceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_service_attribute_with_options(request, runtime)

    async def update_service_attribute_async(
        self,
        request: io_tcc20210513_models.UpdateServiceAttributeRequest,
    ) -> io_tcc20210513_models.UpdateServiceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_service_attribute_with_options_async(request, runtime)

    def list_authorization_rules_with_options(
        self,
        request: io_tcc20210513_models.ListAuthorizationRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.ListAuthorizationRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListAuthorizationRulesResponse(),
            self.do_rpcrequest('ListAuthorizationRules', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_authorization_rules_with_options_async(
        self,
        request: io_tcc20210513_models.ListAuthorizationRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.ListAuthorizationRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListAuthorizationRulesResponse(),
            await self.do_rpcrequest_async('ListAuthorizationRules', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_authorization_rules(
        self,
        request: io_tcc20210513_models.ListAuthorizationRulesRequest,
    ) -> io_tcc20210513_models.ListAuthorizationRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_authorization_rules_with_options(request, runtime)

    async def list_authorization_rules_async(
        self,
        request: io_tcc20210513_models.ListAuthorizationRulesRequest,
    ) -> io_tcc20210513_models.ListAuthorizationRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_authorization_rules_with_options_async(request, runtime)

    def list_service_with_options(
        self,
        request: io_tcc20210513_models.ListServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.ListServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListServiceResponse(),
            self.do_rpcrequest('ListService', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_service_with_options_async(
        self,
        request: io_tcc20210513_models.ListServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.ListServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListServiceResponse(),
            await self.do_rpcrequest_async('ListService', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service(
        self,
        request: io_tcc20210513_models.ListServiceRequest,
    ) -> io_tcc20210513_models.ListServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_service_with_options(request, runtime)

    async def list_service_async(
        self,
        request: io_tcc20210513_models.ListServiceRequest,
    ) -> io_tcc20210513_models.ListServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_service_with_options_async(request, runtime)

    def associate_vswitch_with_io_tcloud_connector_with_options(
        self,
        request: io_tcc20210513_models.AssociateVSwitchWithIoTCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.AssociateVSwitchWithIoTCloudConnectorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.AssociateVSwitchWithIoTCloudConnectorResponse(),
            self.do_rpcrequest('AssociateVSwitchWithIoTCloudConnector', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_vswitch_with_io_tcloud_connector_with_options_async(
        self,
        request: io_tcc20210513_models.AssociateVSwitchWithIoTCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.AssociateVSwitchWithIoTCloudConnectorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.AssociateVSwitchWithIoTCloudConnectorResponse(),
            await self.do_rpcrequest_async('AssociateVSwitchWithIoTCloudConnector', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_vswitch_with_io_tcloud_connector(
        self,
        request: io_tcc20210513_models.AssociateVSwitchWithIoTCloudConnectorRequest,
    ) -> io_tcc20210513_models.AssociateVSwitchWithIoTCloudConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_vswitch_with_io_tcloud_connector_with_options(request, runtime)

    async def associate_vswitch_with_io_tcloud_connector_async(
        self,
        request: io_tcc20210513_models.AssociateVSwitchWithIoTCloudConnectorRequest,
    ) -> io_tcc20210513_models.AssociateVSwitchWithIoTCloudConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_vswitch_with_io_tcloud_connector_with_options_async(request, runtime)

    def list_connection_pools_with_options(
        self,
        request: io_tcc20210513_models.ListConnectionPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.ListConnectionPoolsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListConnectionPoolsResponse(),
            self.do_rpcrequest('ListConnectionPools', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_connection_pools_with_options_async(
        self,
        request: io_tcc20210513_models.ListConnectionPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.ListConnectionPoolsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListConnectionPoolsResponse(),
            await self.do_rpcrequest_async('ListConnectionPools', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_connection_pools(
        self,
        request: io_tcc20210513_models.ListConnectionPoolsRequest,
    ) -> io_tcc20210513_models.ListConnectionPoolsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_connection_pools_with_options(request, runtime)

    async def list_connection_pools_async(
        self,
        request: io_tcc20210513_models.ListConnectionPoolsRequest,
    ) -> io_tcc20210513_models.ListConnectionPoolsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_connection_pools_with_options_async(request, runtime)

    def update_connection_pool_attribute_with_options(
        self,
        request: io_tcc20210513_models.UpdateConnectionPoolAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.UpdateConnectionPoolAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateConnectionPoolAttributeResponse(),
            self.do_rpcrequest('UpdateConnectionPoolAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_connection_pool_attribute_with_options_async(
        self,
        request: io_tcc20210513_models.UpdateConnectionPoolAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.UpdateConnectionPoolAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateConnectionPoolAttributeResponse(),
            await self.do_rpcrequest_async('UpdateConnectionPoolAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_connection_pool_attribute(
        self,
        request: io_tcc20210513_models.UpdateConnectionPoolAttributeRequest,
    ) -> io_tcc20210513_models.UpdateConnectionPoolAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_connection_pool_attribute_with_options(request, runtime)

    async def update_connection_pool_attribute_async(
        self,
        request: io_tcc20210513_models.UpdateConnectionPoolAttributeRequest,
    ) -> io_tcc20210513_models.UpdateConnectionPoolAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_connection_pool_attribute_with_options_async(request, runtime)

    def disable_io_tcloud_connector_access_log_with_options(
        self,
        request: io_tcc20210513_models.DisableIoTCloudConnectorAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DisableIoTCloudConnectorAccessLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DisableIoTCloudConnectorAccessLogResponse(),
            self.do_rpcrequest('DisableIoTCloudConnectorAccessLog', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_io_tcloud_connector_access_log_with_options_async(
        self,
        request: io_tcc20210513_models.DisableIoTCloudConnectorAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DisableIoTCloudConnectorAccessLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DisableIoTCloudConnectorAccessLogResponse(),
            await self.do_rpcrequest_async('DisableIoTCloudConnectorAccessLog', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_io_tcloud_connector_access_log(
        self,
        request: io_tcc20210513_models.DisableIoTCloudConnectorAccessLogRequest,
    ) -> io_tcc20210513_models.DisableIoTCloudConnectorAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_io_tcloud_connector_access_log_with_options(request, runtime)

    async def disable_io_tcloud_connector_access_log_async(
        self,
        request: io_tcc20210513_models.DisableIoTCloudConnectorAccessLogRequest,
    ) -> io_tcc20210513_models.DisableIoTCloudConnectorAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_io_tcloud_connector_access_log_with_options_async(request, runtime)

    def create_connection_pool_with_options(
        self,
        request: io_tcc20210513_models.CreateConnectionPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.CreateConnectionPoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateConnectionPoolResponse(),
            self.do_rpcrequest('CreateConnectionPool', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_connection_pool_with_options_async(
        self,
        request: io_tcc20210513_models.CreateConnectionPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.CreateConnectionPoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateConnectionPoolResponse(),
            await self.do_rpcrequest_async('CreateConnectionPool', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_connection_pool(
        self,
        request: io_tcc20210513_models.CreateConnectionPoolRequest,
    ) -> io_tcc20210513_models.CreateConnectionPoolResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_connection_pool_with_options(request, runtime)

    async def create_connection_pool_async(
        self,
        request: io_tcc20210513_models.CreateConnectionPoolRequest,
    ) -> io_tcc20210513_models.CreateConnectionPoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_connection_pool_with_options_async(request, runtime)

    def create_authorization_rule_with_options(
        self,
        request: io_tcc20210513_models.CreateAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.CreateAuthorizationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateAuthorizationRuleResponse(),
            self.do_rpcrequest('CreateAuthorizationRule', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_authorization_rule_with_options_async(
        self,
        request: io_tcc20210513_models.CreateAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.CreateAuthorizationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateAuthorizationRuleResponse(),
            await self.do_rpcrequest_async('CreateAuthorizationRule', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_authorization_rule(
        self,
        request: io_tcc20210513_models.CreateAuthorizationRuleRequest,
    ) -> io_tcc20210513_models.CreateAuthorizationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_authorization_rule_with_options(request, runtime)

    async def create_authorization_rule_async(
        self,
        request: io_tcc20210513_models.CreateAuthorizationRuleRequest,
    ) -> io_tcc20210513_models.CreateAuthorizationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_authorization_rule_with_options_async(request, runtime)

    def update_io_tcloud_connector_attribute_with_options(
        self,
        request: io_tcc20210513_models.UpdateIoTCloudConnectorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.UpdateIoTCloudConnectorAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateIoTCloudConnectorAttributeResponse(),
            self.do_rpcrequest('UpdateIoTCloudConnectorAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_io_tcloud_connector_attribute_with_options_async(
        self,
        request: io_tcc20210513_models.UpdateIoTCloudConnectorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.UpdateIoTCloudConnectorAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateIoTCloudConnectorAttributeResponse(),
            await self.do_rpcrequest_async('UpdateIoTCloudConnectorAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_io_tcloud_connector_attribute(
        self,
        request: io_tcc20210513_models.UpdateIoTCloudConnectorAttributeRequest,
    ) -> io_tcc20210513_models.UpdateIoTCloudConnectorAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_io_tcloud_connector_attribute_with_options(request, runtime)

    async def update_io_tcloud_connector_attribute_async(
        self,
        request: io_tcc20210513_models.UpdateIoTCloudConnectorAttributeRequest,
    ) -> io_tcc20210513_models.UpdateIoTCloudConnectorAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_io_tcloud_connector_attribute_with_options_async(request, runtime)

    def delete_io_tcloud_connector_with_options(
        self,
        request: io_tcc20210513_models.DeleteIoTCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DeleteIoTCloudConnectorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteIoTCloudConnectorResponse(),
            self.do_rpcrequest('DeleteIoTCloudConnector', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_io_tcloud_connector_with_options_async(
        self,
        request: io_tcc20210513_models.DeleteIoTCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DeleteIoTCloudConnectorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteIoTCloudConnectorResponse(),
            await self.do_rpcrequest_async('DeleteIoTCloudConnector', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_io_tcloud_connector(
        self,
        request: io_tcc20210513_models.DeleteIoTCloudConnectorRequest,
    ) -> io_tcc20210513_models.DeleteIoTCloudConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_io_tcloud_connector_with_options(request, runtime)

    async def delete_io_tcloud_connector_async(
        self,
        request: io_tcc20210513_models.DeleteIoTCloudConnectorRequest,
    ) -> io_tcc20210513_models.DeleteIoTCloudConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_io_tcloud_connector_with_options_async(request, runtime)

    def list_io_tcloud_connector_available_zones_with_options(
        self,
        request: io_tcc20210513_models.ListIoTCloudConnectorAvailableZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.ListIoTCloudConnectorAvailableZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListIoTCloudConnectorAvailableZonesResponse(),
            self.do_rpcrequest('ListIoTCloudConnectorAvailableZones', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_io_tcloud_connector_available_zones_with_options_async(
        self,
        request: io_tcc20210513_models.ListIoTCloudConnectorAvailableZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.ListIoTCloudConnectorAvailableZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListIoTCloudConnectorAvailableZonesResponse(),
            await self.do_rpcrequest_async('ListIoTCloudConnectorAvailableZones', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_io_tcloud_connector_available_zones(
        self,
        request: io_tcc20210513_models.ListIoTCloudConnectorAvailableZonesRequest,
    ) -> io_tcc20210513_models.ListIoTCloudConnectorAvailableZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_io_tcloud_connector_available_zones_with_options(request, runtime)

    async def list_io_tcloud_connector_available_zones_async(
        self,
        request: io_tcc20210513_models.ListIoTCloudConnectorAvailableZonesRequest,
    ) -> io_tcc20210513_models.ListIoTCloudConnectorAvailableZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_io_tcloud_connector_available_zones_with_options_async(request, runtime)

    def get_io_tcloud_connector_access_log_with_options(
        self,
        request: io_tcc20210513_models.GetIoTCloudConnectorAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.GetIoTCloudConnectorAccessLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.GetIoTCloudConnectorAccessLogResponse(),
            self.do_rpcrequest('GetIoTCloudConnectorAccessLog', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_io_tcloud_connector_access_log_with_options_async(
        self,
        request: io_tcc20210513_models.GetIoTCloudConnectorAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.GetIoTCloudConnectorAccessLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.GetIoTCloudConnectorAccessLogResponse(),
            await self.do_rpcrequest_async('GetIoTCloudConnectorAccessLog', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_io_tcloud_connector_access_log(
        self,
        request: io_tcc20210513_models.GetIoTCloudConnectorAccessLogRequest,
    ) -> io_tcc20210513_models.GetIoTCloudConnectorAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_io_tcloud_connector_access_log_with_options(request, runtime)

    async def get_io_tcloud_connector_access_log_async(
        self,
        request: io_tcc20210513_models.GetIoTCloudConnectorAccessLogRequest,
    ) -> io_tcc20210513_models.GetIoTCloudConnectorAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_io_tcloud_connector_access_log_with_options_async(request, runtime)

    def delete_authorization_rule_with_options(
        self,
        request: io_tcc20210513_models.DeleteAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DeleteAuthorizationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteAuthorizationRuleResponse(),
            self.do_rpcrequest('DeleteAuthorizationRule', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_authorization_rule_with_options_async(
        self,
        request: io_tcc20210513_models.DeleteAuthorizationRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DeleteAuthorizationRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteAuthorizationRuleResponse(),
            await self.do_rpcrequest_async('DeleteAuthorizationRule', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_authorization_rule(
        self,
        request: io_tcc20210513_models.DeleteAuthorizationRuleRequest,
    ) -> io_tcc20210513_models.DeleteAuthorizationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_authorization_rule_with_options(request, runtime)

    async def delete_authorization_rule_async(
        self,
        request: io_tcc20210513_models.DeleteAuthorizationRuleRequest,
    ) -> io_tcc20210513_models.DeleteAuthorizationRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_authorization_rule_with_options_async(request, runtime)

    def delete_connection_pool_with_options(
        self,
        request: io_tcc20210513_models.DeleteConnectionPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DeleteConnectionPoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteConnectionPoolResponse(),
            self.do_rpcrequest('DeleteConnectionPool', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_connection_pool_with_options_async(
        self,
        request: io_tcc20210513_models.DeleteConnectionPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DeleteConnectionPoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DeleteConnectionPoolResponse(),
            await self.do_rpcrequest_async('DeleteConnectionPool', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_connection_pool(
        self,
        request: io_tcc20210513_models.DeleteConnectionPoolRequest,
    ) -> io_tcc20210513_models.DeleteConnectionPoolResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_connection_pool_with_options(request, runtime)

    async def delete_connection_pool_async(
        self,
        request: io_tcc20210513_models.DeleteConnectionPoolRequest,
    ) -> io_tcc20210513_models.DeleteConnectionPoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_connection_pool_with_options_async(request, runtime)

    def dissociate_vswitch_from_io_tcloud_connector_with_options(
        self,
        request: io_tcc20210513_models.DissociateVSwitchFromIoTCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DissociateVSwitchFromIoTCloudConnectorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DissociateVSwitchFromIoTCloudConnectorResponse(),
            self.do_rpcrequest('DissociateVSwitchFromIoTCloudConnector', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dissociate_vswitch_from_io_tcloud_connector_with_options_async(
        self,
        request: io_tcc20210513_models.DissociateVSwitchFromIoTCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.DissociateVSwitchFromIoTCloudConnectorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.DissociateVSwitchFromIoTCloudConnectorResponse(),
            await self.do_rpcrequest_async('DissociateVSwitchFromIoTCloudConnector', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_vswitch_from_io_tcloud_connector(
        self,
        request: io_tcc20210513_models.DissociateVSwitchFromIoTCloudConnectorRequest,
    ) -> io_tcc20210513_models.DissociateVSwitchFromIoTCloudConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_vswitch_from_io_tcloud_connector_with_options(request, runtime)

    async def dissociate_vswitch_from_io_tcloud_connector_async(
        self,
        request: io_tcc20210513_models.DissociateVSwitchFromIoTCloudConnectorRequest,
    ) -> io_tcc20210513_models.DissociateVSwitchFromIoTCloudConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_vswitch_from_io_tcloud_connector_with_options_async(request, runtime)

    def enable_io_tcloud_connector_access_log_with_options(
        self,
        request: io_tcc20210513_models.EnableIoTCloudConnectorAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.EnableIoTCloudConnectorAccessLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.EnableIoTCloudConnectorAccessLogResponse(),
            self.do_rpcrequest('EnableIoTCloudConnectorAccessLog', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_io_tcloud_connector_access_log_with_options_async(
        self,
        request: io_tcc20210513_models.EnableIoTCloudConnectorAccessLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.EnableIoTCloudConnectorAccessLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.EnableIoTCloudConnectorAccessLogResponse(),
            await self.do_rpcrequest_async('EnableIoTCloudConnectorAccessLog', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_io_tcloud_connector_access_log(
        self,
        request: io_tcc20210513_models.EnableIoTCloudConnectorAccessLogRequest,
    ) -> io_tcc20210513_models.EnableIoTCloudConnectorAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_io_tcloud_connector_access_log_with_options(request, runtime)

    async def enable_io_tcloud_connector_access_log_async(
        self,
        request: io_tcc20210513_models.EnableIoTCloudConnectorAccessLogRequest,
    ) -> io_tcc20210513_models.EnableIoTCloudConnectorAccessLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_io_tcloud_connector_access_log_with_options_async(request, runtime)

    def list_service_entries_with_options(
        self,
        request: io_tcc20210513_models.ListServiceEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.ListServiceEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListServiceEntriesResponse(),
            self.do_rpcrequest('ListServiceEntries', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_service_entries_with_options_async(
        self,
        request: io_tcc20210513_models.ListServiceEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.ListServiceEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListServiceEntriesResponse(),
            await self.do_rpcrequest_async('ListServiceEntries', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service_entries(
        self,
        request: io_tcc20210513_models.ListServiceEntriesRequest,
    ) -> io_tcc20210513_models.ListServiceEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_service_entries_with_options(request, runtime)

    async def list_service_entries_async(
        self,
        request: io_tcc20210513_models.ListServiceEntriesRequest,
    ) -> io_tcc20210513_models.ListServiceEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_service_entries_with_options_async(request, runtime)

    def create_service_with_options(
        self,
        request: io_tcc20210513_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateServiceResponse(),
            self.do_rpcrequest('CreateService', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: io_tcc20210513_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateServiceResponse(),
            await self.do_rpcrequest_async('CreateService', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service(
        self,
        request: io_tcc20210513_models.CreateServiceRequest,
    ) -> io_tcc20210513_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    async def create_service_async(
        self,
        request: io_tcc20210513_models.CreateServiceRequest,
    ) -> io_tcc20210513_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_with_options_async(request, runtime)

    def list_io_tcloud_connectors_with_options(
        self,
        request: io_tcc20210513_models.ListIoTCloudConnectorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.ListIoTCloudConnectorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListIoTCloudConnectorsResponse(),
            self.do_rpcrequest('ListIoTCloudConnectors', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_io_tcloud_connectors_with_options_async(
        self,
        request: io_tcc20210513_models.ListIoTCloudConnectorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.ListIoTCloudConnectorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.ListIoTCloudConnectorsResponse(),
            await self.do_rpcrequest_async('ListIoTCloudConnectors', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_io_tcloud_connectors(
        self,
        request: io_tcc20210513_models.ListIoTCloudConnectorsRequest,
    ) -> io_tcc20210513_models.ListIoTCloudConnectorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_io_tcloud_connectors_with_options(request, runtime)

    async def list_io_tcloud_connectors_async(
        self,
        request: io_tcc20210513_models.ListIoTCloudConnectorsRequest,
    ) -> io_tcc20210513_models.ListIoTCloudConnectorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_io_tcloud_connectors_with_options_async(request, runtime)

    def create_io_tcloud_connector_with_options(
        self,
        request: io_tcc20210513_models.CreateIoTCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.CreateIoTCloudConnectorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateIoTCloudConnectorResponse(),
            self.do_rpcrequest('CreateIoTCloudConnector', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_io_tcloud_connector_with_options_async(
        self,
        request: io_tcc20210513_models.CreateIoTCloudConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.CreateIoTCloudConnectorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateIoTCloudConnectorResponse(),
            await self.do_rpcrequest_async('CreateIoTCloudConnector', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_io_tcloud_connector(
        self,
        request: io_tcc20210513_models.CreateIoTCloudConnectorRequest,
    ) -> io_tcc20210513_models.CreateIoTCloudConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_io_tcloud_connector_with_options(request, runtime)

    async def create_io_tcloud_connector_async(
        self,
        request: io_tcc20210513_models.CreateIoTCloudConnectorRequest,
    ) -> io_tcc20210513_models.CreateIoTCloudConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_io_tcloud_connector_with_options_async(request, runtime)

    def update_authorization_rule_attribute_with_options(
        self,
        request: io_tcc20210513_models.UpdateAuthorizationRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.UpdateAuthorizationRuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateAuthorizationRuleAttributeResponse(),
            self.do_rpcrequest('UpdateAuthorizationRuleAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_authorization_rule_attribute_with_options_async(
        self,
        request: io_tcc20210513_models.UpdateAuthorizationRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.UpdateAuthorizationRuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.UpdateAuthorizationRuleAttributeResponse(),
            await self.do_rpcrequest_async('UpdateAuthorizationRuleAttribute', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_authorization_rule_attribute(
        self,
        request: io_tcc20210513_models.UpdateAuthorizationRuleAttributeRequest,
    ) -> io_tcc20210513_models.UpdateAuthorizationRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_authorization_rule_attribute_with_options(request, runtime)

    async def update_authorization_rule_attribute_async(
        self,
        request: io_tcc20210513_models.UpdateAuthorizationRuleAttributeRequest,
    ) -> io_tcc20210513_models.UpdateAuthorizationRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_authorization_rule_attribute_with_options_async(request, runtime)

    def create_service_entry_with_options(
        self,
        request: io_tcc20210513_models.CreateServiceEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.CreateServiceEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateServiceEntryResponse(),
            self.do_rpcrequest('CreateServiceEntry', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_entry_with_options_async(
        self,
        request: io_tcc20210513_models.CreateServiceEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> io_tcc20210513_models.CreateServiceEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            io_tcc20210513_models.CreateServiceEntryResponse(),
            await self.do_rpcrequest_async('CreateServiceEntry', '2021-05-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_entry(
        self,
        request: io_tcc20210513_models.CreateServiceEntryRequest,
    ) -> io_tcc20210513_models.CreateServiceEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_entry_with_options(request, runtime)

    async def create_service_entry_async(
        self,
        request: io_tcc20210513_models.CreateServiceEntryRequest,
    ) -> io_tcc20210513_models.CreateServiceEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_entry_with_options_async(request, runtime)
