# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ecd20201001 import models as ecd_20201001_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ecd', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_desktops_with_options(
        self,
        request: ecd_20201001_models.DescribeDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201001_models.DescribeDesktopsResponse:
        """
        @param request: DescribeDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktops',
            version='2020-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201001_models.DescribeDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_desktops_with_options_async(
        self,
        request: ecd_20201001_models.DescribeDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201001_models.DescribeDesktopsResponse:
        """
        @param request: DescribeDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktops',
            version='2020-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201001_models.DescribeDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_desktops(
        self,
        request: ecd_20201001_models.DescribeDesktopsRequest,
    ) -> ecd_20201001_models.DescribeDesktopsResponse:
        """
        @param request: DescribeDesktopsRequest
        @return: DescribeDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_with_options(request, runtime)

    async def describe_desktops_async(
        self,
        request: ecd_20201001_models.DescribeDesktopsRequest,
    ) -> ecd_20201001_models.DescribeDesktopsResponse:
        """
        @param request: DescribeDesktopsRequest
        @return: DescribeDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktops_with_options_async(request, runtime)

    def describe_directories_with_options(
        self,
        request: ecd_20201001_models.DescribeDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201001_models.DescribeDirectoriesResponse:
        """
        @param request: DescribeDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.directory_type):
            query['DirectoryType'] = request.directory_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectories',
            version='2020-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201001_models.DescribeDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_directories_with_options_async(
        self,
        request: ecd_20201001_models.DescribeDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201001_models.DescribeDirectoriesResponse:
        """
        @param request: DescribeDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.directory_type):
            query['DirectoryType'] = request.directory_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectories',
            version='2020-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201001_models.DescribeDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_directories(
        self,
        request: ecd_20201001_models.DescribeDirectoriesRequest,
    ) -> ecd_20201001_models.DescribeDirectoriesResponse:
        """
        @param request: DescribeDirectoriesRequest
        @return: DescribeDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    async def describe_directories_async(
        self,
        request: ecd_20201001_models.DescribeDirectoriesRequest,
    ) -> ecd_20201001_models.DescribeDirectoriesResponse:
        """
        @param request: DescribeDirectoriesRequest
        @return: DescribeDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_directories_with_options_async(request, runtime)

    def get_connection_ticket_with_options(
        self,
        request: ecd_20201001_models.GetConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201001_models.GetConnectionTicketResponse:
        """
        @param request: GetConnectionTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConnectionTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnectionTicket',
            version='2020-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201001_models.GetConnectionTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_connection_ticket_with_options_async(
        self,
        request: ecd_20201001_models.GetConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201001_models.GetConnectionTicketResponse:
        """
        @param request: GetConnectionTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConnectionTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnectionTicket',
            version='2020-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201001_models.GetConnectionTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_connection_ticket(
        self,
        request: ecd_20201001_models.GetConnectionTicketRequest,
    ) -> ecd_20201001_models.GetConnectionTicketResponse:
        """
        @param request: GetConnectionTicketRequest
        @return: GetConnectionTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    async def get_connection_ticket_async(
        self,
        request: ecd_20201001_models.GetConnectionTicketRequest,
    ) -> ecd_20201001_models.GetConnectionTicketResponse:
        """
        @param request: GetConnectionTicketRequest
        @return: GetConnectionTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_connection_ticket_with_options_async(request, runtime)

    def reboot_desktops_with_options(
        self,
        request: ecd_20201001_models.RebootDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201001_models.RebootDesktopsResponse:
        """
        @param request: RebootDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootDesktops',
            version='2020-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201001_models.RebootDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_desktops_with_options_async(
        self,
        request: ecd_20201001_models.RebootDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201001_models.RebootDesktopsResponse:
        """
        @param request: RebootDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootDesktops',
            version='2020-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201001_models.RebootDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_desktops(
        self,
        request: ecd_20201001_models.RebootDesktopsRequest,
    ) -> ecd_20201001_models.RebootDesktopsResponse:
        """
        @param request: RebootDesktopsRequest
        @return: RebootDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reboot_desktops_with_options(request, runtime)

    async def reboot_desktops_async(
        self,
        request: ecd_20201001_models.RebootDesktopsRequest,
    ) -> ecd_20201001_models.RebootDesktopsResponse:
        """
        @param request: RebootDesktopsRequest
        @return: RebootDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reboot_desktops_with_options_async(request, runtime)

    def start_desktops_with_options(
        self,
        request: ecd_20201001_models.StartDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201001_models.StartDesktopsResponse:
        """
        @param request: StartDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDesktops',
            version='2020-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201001_models.StartDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_desktops_with_options_async(
        self,
        request: ecd_20201001_models.StartDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201001_models.StartDesktopsResponse:
        """
        @param request: StartDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDesktops',
            version='2020-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201001_models.StartDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_desktops(
        self,
        request: ecd_20201001_models.StartDesktopsRequest,
    ) -> ecd_20201001_models.StartDesktopsResponse:
        """
        @param request: StartDesktopsRequest
        @return: StartDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_desktops_with_options(request, runtime)

    async def start_desktops_async(
        self,
        request: ecd_20201001_models.StartDesktopsRequest,
    ) -> ecd_20201001_models.StartDesktopsResponse:
        """
        @param request: StartDesktopsRequest
        @return: StartDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_desktops_with_options_async(request, runtime)

    def stop_desktops_with_options(
        self,
        request: ecd_20201001_models.StopDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201001_models.StopDesktopsResponse:
        """
        @param request: StopDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDesktops',
            version='2020-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201001_models.StopDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_desktops_with_options_async(
        self,
        request: ecd_20201001_models.StopDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20201001_models.StopDesktopsResponse:
        """
        @param request: StopDesktopsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDesktopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDesktops',
            version='2020-10-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20201001_models.StopDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_desktops(
        self,
        request: ecd_20201001_models.StopDesktopsRequest,
    ) -> ecd_20201001_models.StopDesktopsResponse:
        """
        @param request: StopDesktopsRequest
        @return: StopDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_desktops_with_options(request, runtime)

    async def stop_desktops_async(
        self,
        request: ecd_20201001_models.StopDesktopsRequest,
    ) -> ecd_20201001_models.StopDesktopsResponse:
        """
        @param request: StopDesktopsRequest
        @return: StopDesktopsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_desktops_with_options_async(request, runtime)
