# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_resourcecenter20221201 import models as resource_center_20221201_models
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
        self._endpoint = self.get_endpoint('resourcecenter', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def associate_default_filter_with_options(
        self,
        request: resource_center_20221201_models.AssociateDefaultFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.AssociateDefaultFilterResponse:
        """
        @summary Sets a default filter.
        
        @param request: AssociateDefaultFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateDefaultFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateDefaultFilter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.AssociateDefaultFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_default_filter_with_options_async(
        self,
        request: resource_center_20221201_models.AssociateDefaultFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.AssociateDefaultFilterResponse:
        """
        @summary Sets a default filter.
        
        @param request: AssociateDefaultFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateDefaultFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateDefaultFilter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.AssociateDefaultFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_default_filter(
        self,
        request: resource_center_20221201_models.AssociateDefaultFilterRequest,
    ) -> resource_center_20221201_models.AssociateDefaultFilterResponse:
        """
        @summary Sets a default filter.
        
        @param request: AssociateDefaultFilterRequest
        @return: AssociateDefaultFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_default_filter_with_options(request, runtime)

    async def associate_default_filter_async(
        self,
        request: resource_center_20221201_models.AssociateDefaultFilterRequest,
    ) -> resource_center_20221201_models.AssociateDefaultFilterResponse:
        """
        @summary Sets a default filter.
        
        @param request: AssociateDefaultFilterRequest
        @return: AssociateDefaultFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_default_filter_with_options_async(request, runtime)

    def create_filter_with_options(
        self,
        request: resource_center_20221201_models.CreateFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.CreateFilterResponse:
        """
        @summary Creates a filter.
        
        @param request: CreateFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_configuration):
            query['FilterConfiguration'] = request.filter_configuration
        if not UtilClient.is_unset(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFilter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.CreateFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_filter_with_options_async(
        self,
        request: resource_center_20221201_models.CreateFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.CreateFilterResponse:
        """
        @summary Creates a filter.
        
        @param request: CreateFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_configuration):
            query['FilterConfiguration'] = request.filter_configuration
        if not UtilClient.is_unset(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFilter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.CreateFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_filter(
        self,
        request: resource_center_20221201_models.CreateFilterRequest,
    ) -> resource_center_20221201_models.CreateFilterResponse:
        """
        @summary Creates a filter.
        
        @param request: CreateFilterRequest
        @return: CreateFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_filter_with_options(request, runtime)

    async def create_filter_async(
        self,
        request: resource_center_20221201_models.CreateFilterRequest,
    ) -> resource_center_20221201_models.CreateFilterResponse:
        """
        @summary Creates a filter.
        
        @param request: CreateFilterRequest
        @return: CreateFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_filter_with_options_async(request, runtime)

    def create_saved_query_with_options(
        self,
        request: resource_center_20221201_models.CreateSavedQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.CreateSavedQueryResponse:
        """
        @summary Creates a custom query template.
        
        @param request: CreateSavedQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSavedQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSavedQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.CreateSavedQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_saved_query_with_options_async(
        self,
        request: resource_center_20221201_models.CreateSavedQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.CreateSavedQueryResponse:
        """
        @summary Creates a custom query template.
        
        @param request: CreateSavedQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSavedQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSavedQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.CreateSavedQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_saved_query(
        self,
        request: resource_center_20221201_models.CreateSavedQueryRequest,
    ) -> resource_center_20221201_models.CreateSavedQueryResponse:
        """
        @summary Creates a custom query template.
        
        @param request: CreateSavedQueryRequest
        @return: CreateSavedQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_saved_query_with_options(request, runtime)

    async def create_saved_query_async(
        self,
        request: resource_center_20221201_models.CreateSavedQueryRequest,
    ) -> resource_center_20221201_models.CreateSavedQueryResponse:
        """
        @summary Creates a custom query template.
        
        @param request: CreateSavedQueryRequest
        @return: CreateSavedQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_saved_query_with_options_async(request, runtime)

    def delete_filter_with_options(
        self,
        request: resource_center_20221201_models.DeleteFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DeleteFilterResponse:
        """
        @summary Deletes a filter.
        
        @param request: DeleteFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFilter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DeleteFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_filter_with_options_async(
        self,
        request: resource_center_20221201_models.DeleteFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DeleteFilterResponse:
        """
        @summary Deletes a filter.
        
        @param request: DeleteFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFilter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DeleteFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_filter(
        self,
        request: resource_center_20221201_models.DeleteFilterRequest,
    ) -> resource_center_20221201_models.DeleteFilterResponse:
        """
        @summary Deletes a filter.
        
        @param request: DeleteFilterRequest
        @return: DeleteFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_filter_with_options(request, runtime)

    async def delete_filter_async(
        self,
        request: resource_center_20221201_models.DeleteFilterRequest,
    ) -> resource_center_20221201_models.DeleteFilterResponse:
        """
        @summary Deletes a filter.
        
        @param request: DeleteFilterRequest
        @return: DeleteFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_filter_with_options_async(request, runtime)

    def delete_saved_query_with_options(
        self,
        request: resource_center_20221201_models.DeleteSavedQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DeleteSavedQueryResponse:
        """
        @summary Deletes a custom query template.
        
        @param request: DeleteSavedQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSavedQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSavedQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DeleteSavedQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_saved_query_with_options_async(
        self,
        request: resource_center_20221201_models.DeleteSavedQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DeleteSavedQueryResponse:
        """
        @summary Deletes a custom query template.
        
        @param request: DeleteSavedQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSavedQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSavedQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DeleteSavedQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_saved_query(
        self,
        request: resource_center_20221201_models.DeleteSavedQueryRequest,
    ) -> resource_center_20221201_models.DeleteSavedQueryResponse:
        """
        @summary Deletes a custom query template.
        
        @param request: DeleteSavedQueryRequest
        @return: DeleteSavedQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_saved_query_with_options(request, runtime)

    async def delete_saved_query_async(
        self,
        request: resource_center_20221201_models.DeleteSavedQueryRequest,
    ) -> resource_center_20221201_models.DeleteSavedQueryResponse:
        """
        @summary Deletes a custom query template.
        
        @param request: DeleteSavedQueryRequest
        @return: DeleteSavedQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_saved_query_with_options_async(request, runtime)

    def disable_multi_account_resource_center_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DisableMultiAccountResourceCenterResponse:
        """
        @summary Disables the cross-account resource search feature by using the management account of a resource directory or a delegated administrator account of Resource Center.
        
        @param request: DisableMultiAccountResourceCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableMultiAccountResourceCenterResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableMultiAccountResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DisableMultiAccountResourceCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_multi_account_resource_center_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DisableMultiAccountResourceCenterResponse:
        """
        @summary Disables the cross-account resource search feature by using the management account of a resource directory or a delegated administrator account of Resource Center.
        
        @param request: DisableMultiAccountResourceCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableMultiAccountResourceCenterResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableMultiAccountResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DisableMultiAccountResourceCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_multi_account_resource_center(self) -> resource_center_20221201_models.DisableMultiAccountResourceCenterResponse:
        """
        @summary Disables the cross-account resource search feature by using the management account of a resource directory or a delegated administrator account of Resource Center.
        
        @return: DisableMultiAccountResourceCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_multi_account_resource_center_with_options(runtime)

    async def disable_multi_account_resource_center_async(self) -> resource_center_20221201_models.DisableMultiAccountResourceCenterResponse:
        """
        @summary Disables the cross-account resource search feature by using the management account of a resource directory or a delegated administrator account of Resource Center.
        
        @return: DisableMultiAccountResourceCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_multi_account_resource_center_with_options_async(runtime)

    def disable_resource_center_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DisableResourceCenterResponse:
        """
        @summary Deactivates the Resource Center service.
        
        @param request: DisableResourceCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableResourceCenterResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DisableResourceCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_resource_center_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DisableResourceCenterResponse:
        """
        @summary Deactivates the Resource Center service.
        
        @param request: DisableResourceCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableResourceCenterResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DisableResourceCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_resource_center(self) -> resource_center_20221201_models.DisableResourceCenterResponse:
        """
        @summary Deactivates the Resource Center service.
        
        @return: DisableResourceCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_resource_center_with_options(runtime)

    async def disable_resource_center_async(self) -> resource_center_20221201_models.DisableResourceCenterResponse:
        """
        @summary Deactivates the Resource Center service.
        
        @return: DisableResourceCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_resource_center_with_options_async(runtime)

    def disassociate_default_filter_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DisassociateDefaultFilterResponse:
        """
        @summary Cancels the default filter.
        
        @param request: DisassociateDefaultFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisassociateDefaultFilterResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisassociateDefaultFilter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DisassociateDefaultFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_default_filter_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.DisassociateDefaultFilterResponse:
        """
        @summary Cancels the default filter.
        
        @param request: DisassociateDefaultFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisassociateDefaultFilterResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisassociateDefaultFilter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.DisassociateDefaultFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_default_filter(self) -> resource_center_20221201_models.DisassociateDefaultFilterResponse:
        """
        @summary Cancels the default filter.
        
        @return: DisassociateDefaultFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disassociate_default_filter_with_options(runtime)

    async def disassociate_default_filter_async(self) -> resource_center_20221201_models.DisassociateDefaultFilterResponse:
        """
        @summary Cancels the default filter.
        
        @return: DisassociateDefaultFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_default_filter_with_options_async(runtime)

    def enable_multi_account_resource_center_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.EnableMultiAccountResourceCenterResponse:
        """
        @summary Enables the cross-account resource search feature by using the management account of a resource directory or a delegated administrator account of Resource Center.
        
        @description If you have created a resource directory for your enterprise, you can enable the cross-account resource search feature by using the management account of the resource directory or a delegated administrator account of Resource Center to view the resources of members in the resource directory. For more information about a resource directory, see [Resource Directory overview](https://help.aliyun.com/document_detail/200506.html).
        
        @param request: EnableMultiAccountResourceCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableMultiAccountResourceCenterResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableMultiAccountResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.EnableMultiAccountResourceCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_multi_account_resource_center_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.EnableMultiAccountResourceCenterResponse:
        """
        @summary Enables the cross-account resource search feature by using the management account of a resource directory or a delegated administrator account of Resource Center.
        
        @description If you have created a resource directory for your enterprise, you can enable the cross-account resource search feature by using the management account of the resource directory or a delegated administrator account of Resource Center to view the resources of members in the resource directory. For more information about a resource directory, see [Resource Directory overview](https://help.aliyun.com/document_detail/200506.html).
        
        @param request: EnableMultiAccountResourceCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableMultiAccountResourceCenterResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableMultiAccountResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.EnableMultiAccountResourceCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_multi_account_resource_center(self) -> resource_center_20221201_models.EnableMultiAccountResourceCenterResponse:
        """
        @summary Enables the cross-account resource search feature by using the management account of a resource directory or a delegated administrator account of Resource Center.
        
        @description If you have created a resource directory for your enterprise, you can enable the cross-account resource search feature by using the management account of the resource directory or a delegated administrator account of Resource Center to view the resources of members in the resource directory. For more information about a resource directory, see [Resource Directory overview](https://help.aliyun.com/document_detail/200506.html).
        
        @return: EnableMultiAccountResourceCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_multi_account_resource_center_with_options(runtime)

    async def enable_multi_account_resource_center_async(self) -> resource_center_20221201_models.EnableMultiAccountResourceCenterResponse:
        """
        @summary Enables the cross-account resource search feature by using the management account of a resource directory or a delegated administrator account of Resource Center.
        
        @description If you have created a resource directory for your enterprise, you can enable the cross-account resource search feature by using the management account of the resource directory or a delegated administrator account of Resource Center to view the resources of members in the resource directory. For more information about a resource directory, see [Resource Directory overview](https://help.aliyun.com/document_detail/200506.html).
        
        @return: EnableMultiAccountResourceCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_multi_account_resource_center_with_options_async(runtime)

    def enable_resource_center_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.EnableResourceCenterResponse:
        """
        @summary Activates the Resource Center service.
        
        @param request: EnableResourceCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableResourceCenterResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.EnableResourceCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_resource_center_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.EnableResourceCenterResponse:
        """
        @summary Activates the Resource Center service.
        
        @param request: EnableResourceCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableResourceCenterResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableResourceCenter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.EnableResourceCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_resource_center(self) -> resource_center_20221201_models.EnableResourceCenterResponse:
        """
        @summary Activates the Resource Center service.
        
        @return: EnableResourceCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_resource_center_with_options(runtime)

    async def enable_resource_center_async(self) -> resource_center_20221201_models.EnableResourceCenterResponse:
        """
        @summary Activates the Resource Center service.
        
        @return: EnableResourceCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_resource_center_with_options_async(runtime)

    def execute_multi_account_sqlquery_with_options(
        self,
        request: resource_center_20221201_models.ExecuteMultiAccountSQLQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ExecuteMultiAccountSQLQueryResponse:
        """
        @summary Executes an SQL statement to query resources across accounts.
        
        @param request: ExecuteMultiAccountSQLQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteMultiAccountSQLQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteMultiAccountSQLQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ExecuteMultiAccountSQLQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_multi_account_sqlquery_with_options_async(
        self,
        request: resource_center_20221201_models.ExecuteMultiAccountSQLQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ExecuteMultiAccountSQLQueryResponse:
        """
        @summary Executes an SQL statement to query resources across accounts.
        
        @param request: ExecuteMultiAccountSQLQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteMultiAccountSQLQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteMultiAccountSQLQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ExecuteMultiAccountSQLQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_multi_account_sqlquery(
        self,
        request: resource_center_20221201_models.ExecuteMultiAccountSQLQueryRequest,
    ) -> resource_center_20221201_models.ExecuteMultiAccountSQLQueryResponse:
        """
        @summary Executes an SQL statement to query resources across accounts.
        
        @param request: ExecuteMultiAccountSQLQueryRequest
        @return: ExecuteMultiAccountSQLQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_multi_account_sqlquery_with_options(request, runtime)

    async def execute_multi_account_sqlquery_async(
        self,
        request: resource_center_20221201_models.ExecuteMultiAccountSQLQueryRequest,
    ) -> resource_center_20221201_models.ExecuteMultiAccountSQLQueryResponse:
        """
        @summary Executes an SQL statement to query resources across accounts.
        
        @param request: ExecuteMultiAccountSQLQueryRequest
        @return: ExecuteMultiAccountSQLQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_multi_account_sqlquery_with_options_async(request, runtime)

    def execute_sqlquery_with_options(
        self,
        request: resource_center_20221201_models.ExecuteSQLQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ExecuteSQLQueryResponse:
        """
        @summary Executes an SQL statement to query the resources that can be accessed within the current account.
        
        @param request: ExecuteSQLQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSQLQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteSQLQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ExecuteSQLQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_sqlquery_with_options_async(
        self,
        request: resource_center_20221201_models.ExecuteSQLQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ExecuteSQLQueryResponse:
        """
        @summary Executes an SQL statement to query the resources that can be accessed within the current account.
        
        @param request: ExecuteSQLQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSQLQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteSQLQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ExecuteSQLQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_sqlquery(
        self,
        request: resource_center_20221201_models.ExecuteSQLQueryRequest,
    ) -> resource_center_20221201_models.ExecuteSQLQueryResponse:
        """
        @summary Executes an SQL statement to query the resources that can be accessed within the current account.
        
        @param request: ExecuteSQLQueryRequest
        @return: ExecuteSQLQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_sqlquery_with_options(request, runtime)

    async def execute_sqlquery_async(
        self,
        request: resource_center_20221201_models.ExecuteSQLQueryRequest,
    ) -> resource_center_20221201_models.ExecuteSQLQueryResponse:
        """
        @summary Executes an SQL statement to query the resources that can be accessed within the current account.
        
        @param request: ExecuteSQLQueryRequest
        @return: ExecuteSQLQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_sqlquery_with_options_async(request, runtime)

    def get_example_query_with_options(
        self,
        request: resource_center_20221201_models.GetExampleQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetExampleQueryResponse:
        """
        @summary Queries the information about a sample query template.
        
        @param request: GetExampleQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExampleQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExampleQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetExampleQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_example_query_with_options_async(
        self,
        request: resource_center_20221201_models.GetExampleQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetExampleQueryResponse:
        """
        @summary Queries the information about a sample query template.
        
        @param request: GetExampleQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExampleQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExampleQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetExampleQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_example_query(
        self,
        request: resource_center_20221201_models.GetExampleQueryRequest,
    ) -> resource_center_20221201_models.GetExampleQueryResponse:
        """
        @summary Queries the information about a sample query template.
        
        @param request: GetExampleQueryRequest
        @return: GetExampleQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_example_query_with_options(request, runtime)

    async def get_example_query_async(
        self,
        request: resource_center_20221201_models.GetExampleQueryRequest,
    ) -> resource_center_20221201_models.GetExampleQueryResponse:
        """
        @summary Queries the information about a sample query template.
        
        @param request: GetExampleQueryRequest
        @return: GetExampleQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_example_query_with_options_async(request, runtime)

    def get_multi_account_resource_center_service_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetMultiAccountResourceCenterServiceStatusResponse:
        """
        @summary Queries the status of the cross-account resource search feature by using the management account of a resource directory or a delegated administrator account of Resource Center.
        
        @param request: GetMultiAccountResourceCenterServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMultiAccountResourceCenterServiceStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetMultiAccountResourceCenterServiceStatus',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetMultiAccountResourceCenterServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_account_resource_center_service_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetMultiAccountResourceCenterServiceStatusResponse:
        """
        @summary Queries the status of the cross-account resource search feature by using the management account of a resource directory or a delegated administrator account of Resource Center.
        
        @param request: GetMultiAccountResourceCenterServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMultiAccountResourceCenterServiceStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetMultiAccountResourceCenterServiceStatus',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetMultiAccountResourceCenterServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_account_resource_center_service_status(self) -> resource_center_20221201_models.GetMultiAccountResourceCenterServiceStatusResponse:
        """
        @summary Queries the status of the cross-account resource search feature by using the management account of a resource directory or a delegated administrator account of Resource Center.
        
        @return: GetMultiAccountResourceCenterServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_multi_account_resource_center_service_status_with_options(runtime)

    async def get_multi_account_resource_center_service_status_async(self) -> resource_center_20221201_models.GetMultiAccountResourceCenterServiceStatusResponse:
        """
        @summary Queries the status of the cross-account resource search feature by using the management account of a resource directory or a delegated administrator account of Resource Center.
        
        @return: GetMultiAccountResourceCenterServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_multi_account_resource_center_service_status_with_options_async(runtime)

    def get_multi_account_resource_configuration_with_options(
        self,
        request: resource_center_20221201_models.GetMultiAccountResourceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetMultiAccountResourceConfigurationResponse:
        """
        @summary Queries the configurations of a resource within the management account or a member of a resource directory.
        
        @param request: GetMultiAccountResourceConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMultiAccountResourceConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiAccountResourceConfiguration',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetMultiAccountResourceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_account_resource_configuration_with_options_async(
        self,
        request: resource_center_20221201_models.GetMultiAccountResourceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetMultiAccountResourceConfigurationResponse:
        """
        @summary Queries the configurations of a resource within the management account or a member of a resource directory.
        
        @param request: GetMultiAccountResourceConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMultiAccountResourceConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiAccountResourceConfiguration',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetMultiAccountResourceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_account_resource_configuration(
        self,
        request: resource_center_20221201_models.GetMultiAccountResourceConfigurationRequest,
    ) -> resource_center_20221201_models.GetMultiAccountResourceConfigurationResponse:
        """
        @summary Queries the configurations of a resource within the management account or a member of a resource directory.
        
        @param request: GetMultiAccountResourceConfigurationRequest
        @return: GetMultiAccountResourceConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_multi_account_resource_configuration_with_options(request, runtime)

    async def get_multi_account_resource_configuration_async(
        self,
        request: resource_center_20221201_models.GetMultiAccountResourceConfigurationRequest,
    ) -> resource_center_20221201_models.GetMultiAccountResourceConfigurationResponse:
        """
        @summary Queries the configurations of a resource within the management account or a member of a resource directory.
        
        @param request: GetMultiAccountResourceConfigurationRequest
        @return: GetMultiAccountResourceConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_multi_account_resource_configuration_with_options_async(request, runtime)

    def get_resource_center_service_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetResourceCenterServiceStatusResponse:
        """
        @summary Queries the status of the Resource Center service.
        
        @param request: GetResourceCenterServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceCenterServiceStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceCenterServiceStatus',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetResourceCenterServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_center_service_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetResourceCenterServiceStatusResponse:
        """
        @summary Queries the status of the Resource Center service.
        
        @param request: GetResourceCenterServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceCenterServiceStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceCenterServiceStatus',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetResourceCenterServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_center_service_status(self) -> resource_center_20221201_models.GetResourceCenterServiceStatusResponse:
        """
        @summary Queries the status of the Resource Center service.
        
        @return: GetResourceCenterServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_center_service_status_with_options(runtime)

    async def get_resource_center_service_status_async(self) -> resource_center_20221201_models.GetResourceCenterServiceStatusResponse:
        """
        @summary Queries the status of the Resource Center service.
        
        @return: GetResourceCenterServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_center_service_status_with_options_async(runtime)

    def get_resource_configuration_with_options(
        self,
        request: resource_center_20221201_models.GetResourceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetResourceConfigurationResponse:
        """
        @summary Queries the configurations of a resource within the current account.
        
        @param request: GetResourceConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceConfiguration',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetResourceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_configuration_with_options_async(
        self,
        request: resource_center_20221201_models.GetResourceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetResourceConfigurationResponse:
        """
        @summary Queries the configurations of a resource within the current account.
        
        @param request: GetResourceConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceConfiguration',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetResourceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_configuration(
        self,
        request: resource_center_20221201_models.GetResourceConfigurationRequest,
    ) -> resource_center_20221201_models.GetResourceConfigurationResponse:
        """
        @summary Queries the configurations of a resource within the current account.
        
        @param request: GetResourceConfigurationRequest
        @return: GetResourceConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_configuration_with_options(request, runtime)

    async def get_resource_configuration_async(
        self,
        request: resource_center_20221201_models.GetResourceConfigurationRequest,
    ) -> resource_center_20221201_models.GetResourceConfigurationResponse:
        """
        @summary Queries the configurations of a resource within the current account.
        
        @param request: GetResourceConfigurationRequest
        @return: GetResourceConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_configuration_with_options_async(request, runtime)

    def get_resource_counts_with_options(
        self,
        request: resource_center_20221201_models.GetResourceCountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetResourceCountsResponse:
        """
        @summary Queries the numbers of resources on which the current account has access permissions.
        
        @param request: GetResourceCountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceCountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.group_by_key):
            query['GroupByKey'] = request.group_by_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceCounts',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetResourceCountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_counts_with_options_async(
        self,
        request: resource_center_20221201_models.GetResourceCountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetResourceCountsResponse:
        """
        @summary Queries the numbers of resources on which the current account has access permissions.
        
        @param request: GetResourceCountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceCountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.group_by_key):
            query['GroupByKey'] = request.group_by_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceCounts',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetResourceCountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_counts(
        self,
        request: resource_center_20221201_models.GetResourceCountsRequest,
    ) -> resource_center_20221201_models.GetResourceCountsResponse:
        """
        @summary Queries the numbers of resources on which the current account has access permissions.
        
        @param request: GetResourceCountsRequest
        @return: GetResourceCountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_counts_with_options(request, runtime)

    async def get_resource_counts_async(
        self,
        request: resource_center_20221201_models.GetResourceCountsRequest,
    ) -> resource_center_20221201_models.GetResourceCountsResponse:
        """
        @summary Queries the numbers of resources on which the current account has access permissions.
        
        @param request: GetResourceCountsRequest
        @return: GetResourceCountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_counts_with_options_async(request, runtime)

    def get_saved_query_with_options(
        self,
        request: resource_center_20221201_models.GetSavedQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetSavedQueryResponse:
        """
        @summary Queries the information about a custom query template.
        
        @param request: GetSavedQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavedQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSavedQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetSavedQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_saved_query_with_options_async(
        self,
        request: resource_center_20221201_models.GetSavedQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.GetSavedQueryResponse:
        """
        @summary Queries the information about a custom query template.
        
        @param request: GetSavedQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavedQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSavedQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.GetSavedQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_saved_query(
        self,
        request: resource_center_20221201_models.GetSavedQueryRequest,
    ) -> resource_center_20221201_models.GetSavedQueryResponse:
        """
        @summary Queries the information about a custom query template.
        
        @param request: GetSavedQueryRequest
        @return: GetSavedQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_saved_query_with_options(request, runtime)

    async def get_saved_query_async(
        self,
        request: resource_center_20221201_models.GetSavedQueryRequest,
    ) -> resource_center_20221201_models.GetSavedQueryResponse:
        """
        @summary Queries the information about a custom query template.
        
        @param request: GetSavedQueryRequest
        @return: GetSavedQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_saved_query_with_options_async(request, runtime)

    def list_example_queries_with_options(
        self,
        request: resource_center_20221201_models.ListExampleQueriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListExampleQueriesResponse:
        """
        @summary Queries all sample query templates.
        
        @param request: ListExampleQueriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExampleQueriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExampleQueries',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListExampleQueriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_example_queries_with_options_async(
        self,
        request: resource_center_20221201_models.ListExampleQueriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListExampleQueriesResponse:
        """
        @summary Queries all sample query templates.
        
        @param request: ListExampleQueriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExampleQueriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExampleQueries',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListExampleQueriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_example_queries(
        self,
        request: resource_center_20221201_models.ListExampleQueriesRequest,
    ) -> resource_center_20221201_models.ListExampleQueriesResponse:
        """
        @summary Queries all sample query templates.
        
        @param request: ListExampleQueriesRequest
        @return: ListExampleQueriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_example_queries_with_options(request, runtime)

    async def list_example_queries_async(
        self,
        request: resource_center_20221201_models.ListExampleQueriesRequest,
    ) -> resource_center_20221201_models.ListExampleQueriesResponse:
        """
        @summary Queries all sample query templates.
        
        @param request: ListExampleQueriesRequest
        @return: ListExampleQueriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_example_queries_with_options_async(request, runtime)

    def list_filters_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListFiltersResponse:
        """
        @summary Queries a list of filters.
        
        @param request: ListFiltersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFiltersResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListFilters',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListFiltersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_filters_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListFiltersResponse:
        """
        @summary Queries a list of filters.
        
        @param request: ListFiltersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFiltersResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListFilters',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListFiltersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_filters(self) -> resource_center_20221201_models.ListFiltersResponse:
        """
        @summary Queries a list of filters.
        
        @return: ListFiltersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_filters_with_options(runtime)

    async def list_filters_async(self) -> resource_center_20221201_models.ListFiltersResponse:
        """
        @summary Queries a list of filters.
        
        @return: ListFiltersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_filters_with_options_async(runtime)

    def list_multi_account_resource_groups_with_options(
        self,
        request: resource_center_20221201_models.ListMultiAccountResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListMultiAccountResourceGroupsResponse:
        """
        @summary Queries the resource groups within the management account or a member of a resource directory by using the management account of the resource directory or a delegated administrator account of Resource Center.
        
        @param request: ListMultiAccountResourceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMultiAccountResourceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiAccountResourceGroups',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListMultiAccountResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_account_resource_groups_with_options_async(
        self,
        request: resource_center_20221201_models.ListMultiAccountResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListMultiAccountResourceGroupsResponse:
        """
        @summary Queries the resource groups within the management account or a member of a resource directory by using the management account of the resource directory or a delegated administrator account of Resource Center.
        
        @param request: ListMultiAccountResourceGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMultiAccountResourceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiAccountResourceGroups',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListMultiAccountResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_account_resource_groups(
        self,
        request: resource_center_20221201_models.ListMultiAccountResourceGroupsRequest,
    ) -> resource_center_20221201_models.ListMultiAccountResourceGroupsResponse:
        """
        @summary Queries the resource groups within the management account or a member of a resource directory by using the management account of the resource directory or a delegated administrator account of Resource Center.
        
        @param request: ListMultiAccountResourceGroupsRequest
        @return: ListMultiAccountResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_multi_account_resource_groups_with_options(request, runtime)

    async def list_multi_account_resource_groups_async(
        self,
        request: resource_center_20221201_models.ListMultiAccountResourceGroupsRequest,
    ) -> resource_center_20221201_models.ListMultiAccountResourceGroupsResponse:
        """
        @summary Queries the resource groups within the management account or a member of a resource directory by using the management account of the resource directory or a delegated administrator account of Resource Center.
        
        @param request: ListMultiAccountResourceGroupsRequest
        @return: ListMultiAccountResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_multi_account_resource_groups_with_options_async(request, runtime)

    def list_multi_account_tag_keys_with_options(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListMultiAccountTagKeysResponse:
        """
        @summary Queries the tag keys of resources within the management account or a member of a resource directory by using the management account of the resource directory or a delegated administrator account of Resource Center.
        
        @param request: ListMultiAccountTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMultiAccountTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiAccountTagKeys',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListMultiAccountTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_account_tag_keys_with_options_async(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListMultiAccountTagKeysResponse:
        """
        @summary Queries the tag keys of resources within the management account or a member of a resource directory by using the management account of the resource directory or a delegated administrator account of Resource Center.
        
        @param request: ListMultiAccountTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMultiAccountTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiAccountTagKeys',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListMultiAccountTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_account_tag_keys(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagKeysRequest,
    ) -> resource_center_20221201_models.ListMultiAccountTagKeysResponse:
        """
        @summary Queries the tag keys of resources within the management account or a member of a resource directory by using the management account of the resource directory or a delegated administrator account of Resource Center.
        
        @param request: ListMultiAccountTagKeysRequest
        @return: ListMultiAccountTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_multi_account_tag_keys_with_options(request, runtime)

    async def list_multi_account_tag_keys_async(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagKeysRequest,
    ) -> resource_center_20221201_models.ListMultiAccountTagKeysResponse:
        """
        @summary Queries the tag keys of resources within the management account or a member of a resource directory by using the management account of the resource directory or a delegated administrator account of Resource Center.
        
        @param request: ListMultiAccountTagKeysRequest
        @return: ListMultiAccountTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_multi_account_tag_keys_with_options_async(request, runtime)

    def list_multi_account_tag_values_with_options(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListMultiAccountTagValuesResponse:
        """
        @summary Queries the tag values of resources within the management account or a member of a resource directory by using the management account of the resource directory or a delegated administrator account of Resource Center.
        
        @param request: ListMultiAccountTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMultiAccountTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiAccountTagValues',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListMultiAccountTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_account_tag_values_with_options_async(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListMultiAccountTagValuesResponse:
        """
        @summary Queries the tag values of resources within the management account or a member of a resource directory by using the management account of the resource directory or a delegated administrator account of Resource Center.
        
        @param request: ListMultiAccountTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMultiAccountTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMultiAccountTagValues',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListMultiAccountTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_account_tag_values(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagValuesRequest,
    ) -> resource_center_20221201_models.ListMultiAccountTagValuesResponse:
        """
        @summary Queries the tag values of resources within the management account or a member of a resource directory by using the management account of the resource directory or a delegated administrator account of Resource Center.
        
        @param request: ListMultiAccountTagValuesRequest
        @return: ListMultiAccountTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_multi_account_tag_values_with_options(request, runtime)

    async def list_multi_account_tag_values_async(
        self,
        request: resource_center_20221201_models.ListMultiAccountTagValuesRequest,
    ) -> resource_center_20221201_models.ListMultiAccountTagValuesResponse:
        """
        @summary Queries the tag values of resources within the management account or a member of a resource directory by using the management account of the resource directory or a delegated administrator account of Resource Center.
        
        @param request: ListMultiAccountTagValuesRequest
        @return: ListMultiAccountTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_multi_account_tag_values_with_options_async(request, runtime)

    def list_resource_types_with_options(
        self,
        request: resource_center_20221201_models.ListResourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListResourceTypesResponse:
        """
        @summary Queries the resource types supported by Resource Center.
        
        @param request: ListResourceTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceTypesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        request: resource_center_20221201_models.ListResourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListResourceTypesResponse:
        """
        @summary Queries the resource types supported by Resource Center.
        
        @param request: ListResourceTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceTypesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_types(
        self,
        request: resource_center_20221201_models.ListResourceTypesRequest,
    ) -> resource_center_20221201_models.ListResourceTypesResponse:
        """
        @summary Queries the resource types supported by Resource Center.
        
        @param request: ListResourceTypesRequest
        @return: ListResourceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_types_with_options(request, runtime)

    async def list_resource_types_async(
        self,
        request: resource_center_20221201_models.ListResourceTypesRequest,
    ) -> resource_center_20221201_models.ListResourceTypesResponse:
        """
        @summary Queries the resource types supported by Resource Center.
        
        @param request: ListResourceTypesRequest
        @return: ListResourceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_types_with_options_async(request, runtime)

    def list_saved_queries_with_options(
        self,
        request: resource_center_20221201_models.ListSavedQueriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListSavedQueriesResponse:
        """
        @summary Queries all custom query templates.
        
        @param request: ListSavedQueriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSavedQueriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavedQueries',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListSavedQueriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_saved_queries_with_options_async(
        self,
        request: resource_center_20221201_models.ListSavedQueriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListSavedQueriesResponse:
        """
        @summary Queries all custom query templates.
        
        @param request: ListSavedQueriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSavedQueriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavedQueries',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListSavedQueriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_saved_queries(
        self,
        request: resource_center_20221201_models.ListSavedQueriesRequest,
    ) -> resource_center_20221201_models.ListSavedQueriesResponse:
        """
        @summary Queries all custom query templates.
        
        @param request: ListSavedQueriesRequest
        @return: ListSavedQueriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_saved_queries_with_options(request, runtime)

    async def list_saved_queries_async(
        self,
        request: resource_center_20221201_models.ListSavedQueriesRequest,
    ) -> resource_center_20221201_models.ListSavedQueriesResponse:
        """
        @summary Queries all custom query templates.
        
        @param request: ListSavedQueriesRequest
        @return: ListSavedQueriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_saved_queries_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: resource_center_20221201_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListTagKeysResponse:
        """
        @summary Queries the tag keys of resources within the current account.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: resource_center_20221201_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListTagKeysResponse:
        """
        @summary Queries the tag keys of resources within the current account.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: resource_center_20221201_models.ListTagKeysRequest,
    ) -> resource_center_20221201_models.ListTagKeysResponse:
        """
        @summary Queries the tag keys of resources within the current account.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: resource_center_20221201_models.ListTagKeysRequest,
    ) -> resource_center_20221201_models.ListTagKeysResponse:
        """
        @summary Queries the tag keys of resources within the current account.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: resource_center_20221201_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListTagValuesResponse:
        """
        @summary Queries the tag values of resources within the current account.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: resource_center_20221201_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.ListTagValuesResponse:
        """
        @summary Queries the tag values of resources within the current account.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: resource_center_20221201_models.ListTagValuesRequest,
    ) -> resource_center_20221201_models.ListTagValuesResponse:
        """
        @summary Queries the tag values of resources within the current account.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: resource_center_20221201_models.ListTagValuesRequest,
    ) -> resource_center_20221201_models.ListTagValuesResponse:
        """
        @summary Queries the tag values of resources within the current account.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def search_multi_account_resources_with_options(
        self,
        request: resource_center_20221201_models.SearchMultiAccountResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.SearchMultiAccountResourcesResponse:
        """
        @summary Searches for resources within the management account or members of a resource directory.
        
        @description    You can use this operation to search for only resources whose types are supported by Resource Center in services that work with Resource Center. For more information about the services and the resource types that are supported by Resource Center, see [Services that work with Resource Center](https://help.aliyun.com/document_detail/477798.html).
        Before you use a RAM user or a RAM role to call the operation, you must make sure that the RAM user or RAM role is granted the required permissions. For more information, see [Grant a RAM user the permissions to use Resource Center](https://help.aliyun.com/document_detail/600556.html).
        By default, the operation returns a maximum of 20 entries. You can configure the `MaxResults` parameter to specify the maximum number of entries to return.
        If the response does not contain the `NextToken` parameter, all entries are returned. Otherwise, more entries exist. If you want to obtain the entries, you can call the operation again to initiate another query request. In the request, set the `NextToken` parameter to the value of `NextToken` in the last response of the operation. If you do not configure the `NextToken` parameter, entries on the first page are returned by default.
        You can specify one or more filter conditions to narrow the search scope. For more information about supported filter parameters and matching methods, see the Supported filter parameters section. Multiple filter conditions have logical `AND` relations. Only resources that meet all filter conditions are returned. The values of a filter condition have logical `OR` relations. Resources that meet any value of the filter condition are returned.
        You can visit [Sample Code Center](https://api.alibabacloud.com/api-tools/demo/ResourceCenter) to view more sample queries.
        
        @param request: SearchMultiAccountResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchMultiAccountResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMultiAccountResources',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.SearchMultiAccountResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_multi_account_resources_with_options_async(
        self,
        request: resource_center_20221201_models.SearchMultiAccountResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.SearchMultiAccountResourcesResponse:
        """
        @summary Searches for resources within the management account or members of a resource directory.
        
        @description    You can use this operation to search for only resources whose types are supported by Resource Center in services that work with Resource Center. For more information about the services and the resource types that are supported by Resource Center, see [Services that work with Resource Center](https://help.aliyun.com/document_detail/477798.html).
        Before you use a RAM user or a RAM role to call the operation, you must make sure that the RAM user or RAM role is granted the required permissions. For more information, see [Grant a RAM user the permissions to use Resource Center](https://help.aliyun.com/document_detail/600556.html).
        By default, the operation returns a maximum of 20 entries. You can configure the `MaxResults` parameter to specify the maximum number of entries to return.
        If the response does not contain the `NextToken` parameter, all entries are returned. Otherwise, more entries exist. If you want to obtain the entries, you can call the operation again to initiate another query request. In the request, set the `NextToken` parameter to the value of `NextToken` in the last response of the operation. If you do not configure the `NextToken` parameter, entries on the first page are returned by default.
        You can specify one or more filter conditions to narrow the search scope. For more information about supported filter parameters and matching methods, see the Supported filter parameters section. Multiple filter conditions have logical `AND` relations. Only resources that meet all filter conditions are returned. The values of a filter condition have logical `OR` relations. Resources that meet any value of the filter condition are returned.
        You can visit [Sample Code Center](https://api.alibabacloud.com/api-tools/demo/ResourceCenter) to view more sample queries.
        
        @param request: SearchMultiAccountResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchMultiAccountResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMultiAccountResources',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.SearchMultiAccountResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_multi_account_resources(
        self,
        request: resource_center_20221201_models.SearchMultiAccountResourcesRequest,
    ) -> resource_center_20221201_models.SearchMultiAccountResourcesResponse:
        """
        @summary Searches for resources within the management account or members of a resource directory.
        
        @description    You can use this operation to search for only resources whose types are supported by Resource Center in services that work with Resource Center. For more information about the services and the resource types that are supported by Resource Center, see [Services that work with Resource Center](https://help.aliyun.com/document_detail/477798.html).
        Before you use a RAM user or a RAM role to call the operation, you must make sure that the RAM user or RAM role is granted the required permissions. For more information, see [Grant a RAM user the permissions to use Resource Center](https://help.aliyun.com/document_detail/600556.html).
        By default, the operation returns a maximum of 20 entries. You can configure the `MaxResults` parameter to specify the maximum number of entries to return.
        If the response does not contain the `NextToken` parameter, all entries are returned. Otherwise, more entries exist. If you want to obtain the entries, you can call the operation again to initiate another query request. In the request, set the `NextToken` parameter to the value of `NextToken` in the last response of the operation. If you do not configure the `NextToken` parameter, entries on the first page are returned by default.
        You can specify one or more filter conditions to narrow the search scope. For more information about supported filter parameters and matching methods, see the Supported filter parameters section. Multiple filter conditions have logical `AND` relations. Only resources that meet all filter conditions are returned. The values of a filter condition have logical `OR` relations. Resources that meet any value of the filter condition are returned.
        You can visit [Sample Code Center](https://api.alibabacloud.com/api-tools/demo/ResourceCenter) to view more sample queries.
        
        @param request: SearchMultiAccountResourcesRequest
        @return: SearchMultiAccountResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_multi_account_resources_with_options(request, runtime)

    async def search_multi_account_resources_async(
        self,
        request: resource_center_20221201_models.SearchMultiAccountResourcesRequest,
    ) -> resource_center_20221201_models.SearchMultiAccountResourcesResponse:
        """
        @summary Searches for resources within the management account or members of a resource directory.
        
        @description    You can use this operation to search for only resources whose types are supported by Resource Center in services that work with Resource Center. For more information about the services and the resource types that are supported by Resource Center, see [Services that work with Resource Center](https://help.aliyun.com/document_detail/477798.html).
        Before you use a RAM user or a RAM role to call the operation, you must make sure that the RAM user or RAM role is granted the required permissions. For more information, see [Grant a RAM user the permissions to use Resource Center](https://help.aliyun.com/document_detail/600556.html).
        By default, the operation returns a maximum of 20 entries. You can configure the `MaxResults` parameter to specify the maximum number of entries to return.
        If the response does not contain the `NextToken` parameter, all entries are returned. Otherwise, more entries exist. If you want to obtain the entries, you can call the operation again to initiate another query request. In the request, set the `NextToken` parameter to the value of `NextToken` in the last response of the operation. If you do not configure the `NextToken` parameter, entries on the first page are returned by default.
        You can specify one or more filter conditions to narrow the search scope. For more information about supported filter parameters and matching methods, see the Supported filter parameters section. Multiple filter conditions have logical `AND` relations. Only resources that meet all filter conditions are returned. The values of a filter condition have logical `OR` relations. Resources that meet any value of the filter condition are returned.
        You can visit [Sample Code Center](https://api.alibabacloud.com/api-tools/demo/ResourceCenter) to view more sample queries.
        
        @param request: SearchMultiAccountResourcesRequest
        @return: SearchMultiAccountResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_multi_account_resources_with_options_async(request, runtime)

    def search_resources_with_options(
        self,
        request: resource_center_20221201_models.SearchResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.SearchResourcesResponse:
        """
        @summary Search for resources that you can access within the current account.
        
        @description    You can use this operation to search for only resources whose types are supported by Resource Center in services that work with Resource Center. For more information about the services and the resource types that are supported by Resource Center, see [Services that work with Resource Center](https://help.aliyun.com/document_detail/477798.html).
        By default, the operation returns a maximum of 20 entries. You can configure the `MaxResults` parameter to specify the maximum number of entries to return.
        If the response does not contain the `NextToken` parameter, all entries are returned. Otherwise, more entries exist. If you want to obtain the entries, you can call the operation again to initiate another query request. In the request, set the `NextToken` parameter to the value of `NextToken` in the last response of the operation. If you do not configure the `NextToken` parameter, entries on the first page are returned by default.
        You can specify one or more filter conditions to narrow the search scope. For more information about supported filter parameters and matching methods, see the Supported filter parameters section. Multiple filter conditions have logical `AND` relations. Only resources that meet all filter conditions are returned. The values of a filter condition have logical `OR` relations. Resources that meet any value of the filter condition are returned.
        You can visit [Sample Code Center](https://api.aliyun.com/api-tools/demo/ResourceCenter) to view more sample queries.
        
        @param request: SearchResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchResources',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.SearchResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_resources_with_options_async(
        self,
        request: resource_center_20221201_models.SearchResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.SearchResourcesResponse:
        """
        @summary Search for resources that you can access within the current account.
        
        @description    You can use this operation to search for only resources whose types are supported by Resource Center in services that work with Resource Center. For more information about the services and the resource types that are supported by Resource Center, see [Services that work with Resource Center](https://help.aliyun.com/document_detail/477798.html).
        By default, the operation returns a maximum of 20 entries. You can configure the `MaxResults` parameter to specify the maximum number of entries to return.
        If the response does not contain the `NextToken` parameter, all entries are returned. Otherwise, more entries exist. If you want to obtain the entries, you can call the operation again to initiate another query request. In the request, set the `NextToken` parameter to the value of `NextToken` in the last response of the operation. If you do not configure the `NextToken` parameter, entries on the first page are returned by default.
        You can specify one or more filter conditions to narrow the search scope. For more information about supported filter parameters and matching methods, see the Supported filter parameters section. Multiple filter conditions have logical `AND` relations. Only resources that meet all filter conditions are returned. The values of a filter condition have logical `OR` relations. Resources that meet any value of the filter condition are returned.
        You can visit [Sample Code Center](https://api.aliyun.com/api-tools/demo/ResourceCenter) to view more sample queries.
        
        @param request: SearchResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchResources',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.SearchResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_resources(
        self,
        request: resource_center_20221201_models.SearchResourcesRequest,
    ) -> resource_center_20221201_models.SearchResourcesResponse:
        """
        @summary Search for resources that you can access within the current account.
        
        @description    You can use this operation to search for only resources whose types are supported by Resource Center in services that work with Resource Center. For more information about the services and the resource types that are supported by Resource Center, see [Services that work with Resource Center](https://help.aliyun.com/document_detail/477798.html).
        By default, the operation returns a maximum of 20 entries. You can configure the `MaxResults` parameter to specify the maximum number of entries to return.
        If the response does not contain the `NextToken` parameter, all entries are returned. Otherwise, more entries exist. If you want to obtain the entries, you can call the operation again to initiate another query request. In the request, set the `NextToken` parameter to the value of `NextToken` in the last response of the operation. If you do not configure the `NextToken` parameter, entries on the first page are returned by default.
        You can specify one or more filter conditions to narrow the search scope. For more information about supported filter parameters and matching methods, see the Supported filter parameters section. Multiple filter conditions have logical `AND` relations. Only resources that meet all filter conditions are returned. The values of a filter condition have logical `OR` relations. Resources that meet any value of the filter condition are returned.
        You can visit [Sample Code Center](https://api.aliyun.com/api-tools/demo/ResourceCenter) to view more sample queries.
        
        @param request: SearchResourcesRequest
        @return: SearchResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_resources_with_options(request, runtime)

    async def search_resources_async(
        self,
        request: resource_center_20221201_models.SearchResourcesRequest,
    ) -> resource_center_20221201_models.SearchResourcesResponse:
        """
        @summary Search for resources that you can access within the current account.
        
        @description    You can use this operation to search for only resources whose types are supported by Resource Center in services that work with Resource Center. For more information about the services and the resource types that are supported by Resource Center, see [Services that work with Resource Center](https://help.aliyun.com/document_detail/477798.html).
        By default, the operation returns a maximum of 20 entries. You can configure the `MaxResults` parameter to specify the maximum number of entries to return.
        If the response does not contain the `NextToken` parameter, all entries are returned. Otherwise, more entries exist. If you want to obtain the entries, you can call the operation again to initiate another query request. In the request, set the `NextToken` parameter to the value of `NextToken` in the last response of the operation. If you do not configure the `NextToken` parameter, entries on the first page are returned by default.
        You can specify one or more filter conditions to narrow the search scope. For more information about supported filter parameters and matching methods, see the Supported filter parameters section. Multiple filter conditions have logical `AND` relations. Only resources that meet all filter conditions are returned. The values of a filter condition have logical `OR` relations. Resources that meet any value of the filter condition are returned.
        You can visit [Sample Code Center](https://api.aliyun.com/api-tools/demo/ResourceCenter) to view more sample queries.
        
        @param request: SearchResourcesRequest
        @return: SearchResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_resources_with_options_async(request, runtime)

    def update_filter_with_options(
        self,
        request: resource_center_20221201_models.UpdateFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.UpdateFilterResponse:
        """
        @summary Updates a filter.
        
        @param request: UpdateFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_configuration):
            query['FilterConfiguration'] = request.filter_configuration
        if not UtilClient.is_unset(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFilter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.UpdateFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_filter_with_options_async(
        self,
        request: resource_center_20221201_models.UpdateFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.UpdateFilterResponse:
        """
        @summary Updates a filter.
        
        @param request: UpdateFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_configuration):
            query['FilterConfiguration'] = request.filter_configuration
        if not UtilClient.is_unset(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFilter',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.UpdateFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_filter(
        self,
        request: resource_center_20221201_models.UpdateFilterRequest,
    ) -> resource_center_20221201_models.UpdateFilterResponse:
        """
        @summary Updates a filter.
        
        @param request: UpdateFilterRequest
        @return: UpdateFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_filter_with_options(request, runtime)

    async def update_filter_async(
        self,
        request: resource_center_20221201_models.UpdateFilterRequest,
    ) -> resource_center_20221201_models.UpdateFilterResponse:
        """
        @summary Updates a filter.
        
        @param request: UpdateFilterRequest
        @return: UpdateFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_filter_with_options_async(request, runtime)

    def update_saved_query_with_options(
        self,
        request: resource_center_20221201_models.UpdateSavedQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.UpdateSavedQueryResponse:
        """
        @summary Updates a custom query template.
        
        @param request: UpdateSavedQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSavedQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSavedQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.UpdateSavedQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_saved_query_with_options_async(
        self,
        request: resource_center_20221201_models.UpdateSavedQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_center_20221201_models.UpdateSavedQueryResponse:
        """
        @summary Updates a custom query template.
        
        @param request: UpdateSavedQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSavedQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSavedQuery',
            version='2022-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_center_20221201_models.UpdateSavedQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_saved_query(
        self,
        request: resource_center_20221201_models.UpdateSavedQueryRequest,
    ) -> resource_center_20221201_models.UpdateSavedQueryResponse:
        """
        @summary Updates a custom query template.
        
        @param request: UpdateSavedQueryRequest
        @return: UpdateSavedQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_saved_query_with_options(request, runtime)

    async def update_saved_query_async(
        self,
        request: resource_center_20221201_models.UpdateSavedQueryRequest,
    ) -> resource_center_20221201_models.UpdateSavedQueryResponse:
        """
        @summary Updates a custom query template.
        
        @param request: UpdateSavedQueryRequest
        @return: UpdateSavedQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_saved_query_with_options_async(request, runtime)
