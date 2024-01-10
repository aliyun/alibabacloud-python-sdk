# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_gateway_spi.client import Client as SPIClient
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_sls.client import Client as GatewayClientClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_sls20201230 import models as sls_20201230_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    _client: SPIClient = None

    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._client = GatewayClientClient()
        self._spi = self._client
        self._endpoint_rule = 'central'

    def apply_config_to_machine_group_with_options(
        self,
        project: str,
        machine_group: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ApplyConfigToMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyConfigToMachineGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ApplyConfigToMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}/configs/{config_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.ApplyConfigToMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def apply_config_to_machine_group_with_options_async(
        self,
        project: str,
        machine_group: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ApplyConfigToMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyConfigToMachineGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ApplyConfigToMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}/configs/{config_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.ApplyConfigToMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def apply_config_to_machine_group(
        self,
        project: str,
        machine_group: str,
        config_name: str,
    ) -> sls_20201230_models.ApplyConfigToMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: ApplyConfigToMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.apply_config_to_machine_group_with_options(project, machine_group, config_name, headers, runtime)

    async def apply_config_to_machine_group_async(
        self,
        project: str,
        machine_group: str,
        config_name: str,
    ) -> sls_20201230_models.ApplyConfigToMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: ApplyConfigToMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.apply_config_to_machine_group_with_options_async(project, machine_group, config_name, headers, runtime)

    def change_resource_group_with_options(
        self,
        project: str,
        request: sls_20201230_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/resourcegroup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.ChangeResourceGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/resourcegroup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.ChangeResourceGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        project: str,
        request: sls_20201230_models.ChangeResourceGroupRequest,
    ) -> sls_20201230_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(project, request, headers, runtime)

    async def change_resource_group_async(
        self,
        project: str,
        request: sls_20201230_models.ChangeResourceGroupRequest,
    ) -> sls_20201230_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(project, request, headers, runtime)

    def consumer_group_heart_beat_with_options(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.ConsumerGroupHeartBeatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ConsumerGroupHeartBeatResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.consumer):
            query['consumer'] = request.consumer
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='ConsumerGroupHeartBeat',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups/{consumer_group}?type=heartbeat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ConsumerGroupHeartBeatResponse(),
            self.execute(params, req, runtime)
        )

    async def consumer_group_heart_beat_with_options_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.ConsumerGroupHeartBeatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ConsumerGroupHeartBeatResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.consumer):
            query['consumer'] = request.consumer
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='ConsumerGroupHeartBeat',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups/{consumer_group}?type=heartbeat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ConsumerGroupHeartBeatResponse(),
            await self.execute_async(params, req, runtime)
        )

    def consumer_group_heart_beat(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.ConsumerGroupHeartBeatRequest,
    ) -> sls_20201230_models.ConsumerGroupHeartBeatResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.consumer_group_heart_beat_with_options(project, logstore, consumer_group, request, headers, runtime)

    async def consumer_group_heart_beat_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.ConsumerGroupHeartBeatRequest,
    ) -> sls_20201230_models.ConsumerGroupHeartBeatResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.consumer_group_heart_beat_with_options_async(project, logstore, consumer_group, request, headers, runtime)

    def create_annotation_data_set_with_options(
        self,
        request: sls_20201230_models.CreateAnnotationDataSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateAnnotationDataSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['datasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    async def create_annotation_data_set_with_options_async(
        self,
        request: sls_20201230_models.CreateAnnotationDataSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateAnnotationDataSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['datasetId'] = request.dataset_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateAnnotationDataSetResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_annotation_data_set(
        self,
        request: sls_20201230_models.CreateAnnotationDataSetRequest,
    ) -> sls_20201230_models.CreateAnnotationDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_annotation_data_set_with_options(request, headers, runtime)

    async def create_annotation_data_set_async(
        self,
        request: sls_20201230_models.CreateAnnotationDataSetRequest,
    ) -> sls_20201230_models.CreateAnnotationDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_annotation_data_set_with_options_async(request, headers, runtime)

    def create_annotation_label_with_options(
        self,
        request: sls_20201230_models.CreateAnnotationLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateAnnotationLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationlabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    async def create_annotation_label_with_options_async(
        self,
        request: sls_20201230_models.CreateAnnotationLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateAnnotationLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationlabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateAnnotationLabelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_annotation_label(
        self,
        request: sls_20201230_models.CreateAnnotationLabelRequest,
    ) -> sls_20201230_models.CreateAnnotationLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_annotation_label_with_options(request, headers, runtime)

    async def create_annotation_label_async(
        self,
        request: sls_20201230_models.CreateAnnotationLabelRequest,
    ) -> sls_20201230_models.CreateAnnotationLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_annotation_label_with_options_async(request, headers, runtime)

    def create_config_with_options(
        self,
        project: str,
        request: sls_20201230_models.CreateConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateConfigResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def create_config_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.CreateConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateConfigResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/configs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_config(
        self,
        project: str,
        request: sls_20201230_models.CreateConfigRequest,
    ) -> sls_20201230_models.CreateConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_config_with_options(project, request, headers, runtime)

    async def create_config_async(
        self,
        project: str,
        request: sls_20201230_models.CreateConfigRequest,
    ) -> sls_20201230_models.CreateConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_config_with_options_async(project, request, headers, runtime)

    def create_consumer_group_with_options(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.CreateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateConsumerGroupResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   You can create up to 30 consumer groups for a Logstore.
        *   Simple Log Service provides examples of both regular log consumption and consumer group-based log consumption by using Simple Log Service SDKs for Java. For more information, see [Consume log data](~~120035~~) and [Use consumer groups to consume data](~~28998~~).
        
        @param request: CreateConsumerGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.consumer_group):
            body['consumerGroup'] = request.consumer_group
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.CreateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateConsumerGroupResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   You can create up to 30 consumer groups for a Logstore.
        *   Simple Log Service provides examples of both regular log consumption and consumer group-based log consumption by using Simple Log Service SDKs for Java. For more information, see [Consume log data](~~120035~~) and [Use consumer groups to consume data](~~28998~~).
        
        @param request: CreateConsumerGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.consumer_group):
            body['consumerGroup'] = request.consumer_group
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateConsumerGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_consumer_group(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.CreateConsumerGroupRequest,
    ) -> sls_20201230_models.CreateConsumerGroupResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   You can create up to 30 consumer groups for a Logstore.
        *   Simple Log Service provides examples of both regular log consumption and consumer group-based log consumption by using Simple Log Service SDKs for Java. For more information, see [Consume log data](~~120035~~) and [Use consumer groups to consume data](~~28998~~).
        
        @param request: CreateConsumerGroupRequest
        @return: CreateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_consumer_group_with_options(project, logstore, request, headers, runtime)

    async def create_consumer_group_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.CreateConsumerGroupRequest,
    ) -> sls_20201230_models.CreateConsumerGroupResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   You can create up to 30 consumer groups for a Logstore.
        *   Simple Log Service provides examples of both regular log consumption and consumer group-based log consumption by using Simple Log Service SDKs for Java. For more information, see [Consume log data](~~120035~~) and [Use consumer groups to consume data](~~28998~~).
        
        @param request: CreateConsumerGroupRequest
        @return: CreateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_consumer_group_with_options_async(project, logstore, request, headers, runtime)

    def create_dashboard_with_options(
        self,
        project: str,
        request: sls_20201230_models.CreateDashboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateDashboardResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/dashboards',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateDashboardResponse(),
            self.execute(params, req, runtime)
        )

    async def create_dashboard_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.CreateDashboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateDashboardResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/dashboards',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateDashboardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_dashboard(
        self,
        project: str,
        request: sls_20201230_models.CreateDashboardRequest,
    ) -> sls_20201230_models.CreateDashboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_dashboard_with_options(project, request, headers, runtime)

    async def create_dashboard_async(
        self,
        project: str,
        request: sls_20201230_models.CreateDashboardRequest,
    ) -> sls_20201230_models.CreateDashboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_dashboard_with_options_async(project, request, headers, runtime)

    def create_domain_with_options(
        self,
        project: str,
        request: sls_20201230_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateDomainResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['domainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateDomainResponse(),
            self.execute(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateDomainResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateDomainRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.domain_name):
            body['domainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/domains',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateDomainResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_domain(
        self,
        project: str,
        request: sls_20201230_models.CreateDomainRequest,
    ) -> sls_20201230_models.CreateDomainResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_domain_with_options(project, request, headers, runtime)

    async def create_domain_async(
        self,
        project: str,
        request: sls_20201230_models.CreateDomainRequest,
    ) -> sls_20201230_models.CreateDomainResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_domain_with_options_async(project, request, headers, runtime)

    def create_index_with_options(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.CreateIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateIndexResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIndexResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.log_reduce):
            body['log_reduce'] = request.log_reduce
        if not UtilClient.is_unset(request.log_reduce_black_list):
            body['log_reduce_black_list'] = request.log_reduce_black_list
        if not UtilClient.is_unset(request.log_reduce_white_list):
            body['log_reduce_white_list'] = request.log_reduce_white_list
        if not UtilClient.is_unset(request.max_text_len):
            body['max_text_len'] = request.max_text_len
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/index',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateIndexResponse(),
            self.execute(params, req, runtime)
        )

    async def create_index_with_options_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.CreateIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateIndexResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIndexResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.log_reduce):
            body['log_reduce'] = request.log_reduce
        if not UtilClient.is_unset(request.log_reduce_black_list):
            body['log_reduce_black_list'] = request.log_reduce_black_list
        if not UtilClient.is_unset(request.log_reduce_white_list):
            body['log_reduce_white_list'] = request.log_reduce_white_list
        if not UtilClient.is_unset(request.max_text_len):
            body['max_text_len'] = request.max_text_len
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/index',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateIndexResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_index(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.CreateIndexRequest,
    ) -> sls_20201230_models.CreateIndexResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateIndexRequest
        @return: CreateIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_index_with_options(project, logstore, request, headers, runtime)

    async def create_index_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.CreateIndexRequest,
    ) -> sls_20201230_models.CreateIndexResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateIndexRequest
        @return: CreateIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_index_with_options_async(project, logstore, request, headers, runtime)

    def create_log_store_with_options(
        self,
        project: str,
        request: sls_20201230_models.CreateLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateLogStoreResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateLogStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLogStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not UtilClient.is_unset(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not UtilClient.is_unset(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def create_log_store_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.CreateLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateLogStoreResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateLogStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLogStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not UtilClient.is_unset(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not UtilClient.is_unset(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLogStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_log_store(
        self,
        project: str,
        request: sls_20201230_models.CreateLogStoreRequest,
    ) -> sls_20201230_models.CreateLogStoreResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateLogStoreRequest
        @return: CreateLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_log_store_with_options(project, request, headers, runtime)

    async def create_log_store_async(
        self,
        project: str,
        request: sls_20201230_models.CreateLogStoreRequest,
    ) -> sls_20201230_models.CreateLogStoreResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateLogStoreRequest
        @return: CreateLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_log_store_with_options_async(project, request, headers, runtime)

    def create_logging_with_options(
        self,
        project: str,
        request: sls_20201230_models.CreateLoggingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateLoggingResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateLoggingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoggingResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.logging_details):
            body['loggingDetails'] = request.logging_details
        if not UtilClient.is_unset(request.logging_project):
            body['loggingProject'] = request.logging_project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logging',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLoggingResponse(),
            self.execute(params, req, runtime)
        )

    async def create_logging_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.CreateLoggingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateLoggingResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateLoggingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoggingResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.logging_details):
            body['loggingDetails'] = request.logging_details
        if not UtilClient.is_unset(request.logging_project):
            body['loggingProject'] = request.logging_project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logging',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLoggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_logging(
        self,
        project: str,
        request: sls_20201230_models.CreateLoggingRequest,
    ) -> sls_20201230_models.CreateLoggingResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateLoggingRequest
        @return: CreateLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_logging_with_options(project, request, headers, runtime)

    async def create_logging_async(
        self,
        project: str,
        request: sls_20201230_models.CreateLoggingRequest,
    ) -> sls_20201230_models.CreateLoggingResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateLoggingRequest
        @return: CreateLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_logging_with_options_async(project, request, headers, runtime)

    def create_logtail_pipeline_config_with_options(
        self,
        project: str,
        request: sls_20201230_models.CreateLogtailPipelineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateLogtailPipelineConfigResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.aggregators):
            body['aggregators'] = request.aggregators
        if not UtilClient.is_unset(request.config_name):
            body['configName'] = request.config_name
        if not UtilClient.is_unset(request.flushers):
            body['flushers'] = request.flushers
        if not UtilClient.is_unset(request.global_):
            body['global'] = request.global_
        if not UtilClient.is_unset(request.inputs):
            body['inputs'] = request.inputs
        if not UtilClient.is_unset(request.log_sample):
            body['logSample'] = request.log_sample
        if not UtilClient.is_unset(request.processors):
            body['processors'] = request.processors
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/pipelineconfigs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def create_logtail_pipeline_config_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.CreateLogtailPipelineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateLogtailPipelineConfigResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.aggregators):
            body['aggregators'] = request.aggregators
        if not UtilClient.is_unset(request.config_name):
            body['configName'] = request.config_name
        if not UtilClient.is_unset(request.flushers):
            body['flushers'] = request.flushers
        if not UtilClient.is_unset(request.global_):
            body['global'] = request.global_
        if not UtilClient.is_unset(request.inputs):
            body['inputs'] = request.inputs
        if not UtilClient.is_unset(request.log_sample):
            body['logSample'] = request.log_sample
        if not UtilClient.is_unset(request.processors):
            body['processors'] = request.processors
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/pipelineconfigs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateLogtailPipelineConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_logtail_pipeline_config(
        self,
        project: str,
        request: sls_20201230_models.CreateLogtailPipelineConfigRequest,
    ) -> sls_20201230_models.CreateLogtailPipelineConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_logtail_pipeline_config_with_options(project, request, headers, runtime)

    async def create_logtail_pipeline_config_async(
        self,
        project: str,
        request: sls_20201230_models.CreateLogtailPipelineConfigRequest,
    ) -> sls_20201230_models.CreateLogtailPipelineConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_logtail_pipeline_config_with_options_async(project, request, headers, runtime)

    def create_machine_group_with_options(
        self,
        project: str,
        request: sls_20201230_models.CreateMachineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateMachineGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateMachineGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMachineGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.group_attribute):
            body['groupAttribute'] = request.group_attribute
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            body['groupType'] = request.group_type
        if not UtilClient.is_unset(request.machine_identify_type):
            body['machineIdentifyType'] = request.machine_identify_type
        if not UtilClient.is_unset(request.machine_list):
            body['machineList'] = request.machine_list
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def create_machine_group_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.CreateMachineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateMachineGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateMachineGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMachineGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.group_attribute):
            body['groupAttribute'] = request.group_attribute
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            body['groupType'] = request.group_type
        if not UtilClient.is_unset(request.machine_identify_type):
            body['machineIdentifyType'] = request.machine_identify_type
        if not UtilClient.is_unset(request.machine_list):
            body['machineList'] = request.machine_list
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_machine_group(
        self,
        project: str,
        request: sls_20201230_models.CreateMachineGroupRequest,
    ) -> sls_20201230_models.CreateMachineGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateMachineGroupRequest
        @return: CreateMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_machine_group_with_options(project, request, headers, runtime)

    async def create_machine_group_async(
        self,
        project: str,
        request: sls_20201230_models.CreateMachineGroupRequest,
    ) -> sls_20201230_models.CreateMachineGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateMachineGroupRequest
        @return: CreateMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_machine_group_with_options_async(project, request, headers, runtime)

    def create_oss_external_store_with_options(
        self,
        project: str,
        request: sls_20201230_models.CreateOssExternalStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateOssExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateOssExternalStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOssExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOssExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateOssExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def create_oss_external_store_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.CreateOssExternalStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateOssExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateOssExternalStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOssExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOssExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateOssExternalStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_oss_external_store(
        self,
        project: str,
        request: sls_20201230_models.CreateOssExternalStoreRequest,
    ) -> sls_20201230_models.CreateOssExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateOssExternalStoreRequest
        @return: CreateOssExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_oss_external_store_with_options(project, request, headers, runtime)

    async def create_oss_external_store_async(
        self,
        project: str,
        request: sls_20201230_models.CreateOssExternalStoreRequest,
    ) -> sls_20201230_models.CreateOssExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateOssExternalStoreRequest
        @return: CreateOssExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_oss_external_store_with_options_async(project, request, headers, runtime)

    def create_project_with_options(
        self,
        request: sls_20201230_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_redundancy_type):
            body['dataRedundancyType'] = request.data_redundancy_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: sls_20201230_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_redundancy_type):
            body['dataRedundancyType'] = request.data_redundancy_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_project(
        self,
        request: sls_20201230_models.CreateProjectRequest,
    ) -> sls_20201230_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: sls_20201230_models.CreateProjectRequest,
    ) -> sls_20201230_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def create_rds_external_store_with_options(
        self,
        project: str,
        request: sls_20201230_models.CreateRdsExternalStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateRdsExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateRdsExternalStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRdsExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRdsExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateRdsExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def create_rds_external_store_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.CreateRdsExternalStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateRdsExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateRdsExternalStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRdsExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRdsExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateRdsExternalStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_rds_external_store(
        self,
        project: str,
        request: sls_20201230_models.CreateRdsExternalStoreRequest,
    ) -> sls_20201230_models.CreateRdsExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateRdsExternalStoreRequest
        @return: CreateRdsExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_rds_external_store_with_options(project, request, headers, runtime)

    async def create_rds_external_store_async(
        self,
        project: str,
        request: sls_20201230_models.CreateRdsExternalStoreRequest,
    ) -> sls_20201230_models.CreateRdsExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateRdsExternalStoreRequest
        @return: CreateRdsExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_rds_external_store_with_options_async(project, request, headers, runtime)

    def create_saved_search_with_options(
        self,
        project: str,
        request: sls_20201230_models.CreateSavedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateSavedSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSavedSearchResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.logstore):
            body['logstore'] = request.logstore
        if not UtilClient.is_unset(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def create_saved_search_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.CreateSavedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateSavedSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSavedSearchResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.logstore):
            body['logstore'] = request.logstore
        if not UtilClient.is_unset(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_saved_search(
        self,
        project: str,
        request: sls_20201230_models.CreateSavedSearchRequest,
    ) -> sls_20201230_models.CreateSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateSavedSearchRequest
        @return: CreateSavedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_saved_search_with_options(project, request, headers, runtime)

    async def create_saved_search_async(
        self,
        project: str,
        request: sls_20201230_models.CreateSavedSearchRequest,
    ) -> sls_20201230_models.CreateSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: CreateSavedSearchRequest
        @return: CreateSavedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_saved_search_with_options_async(project, request, headers, runtime)

    def create_ticket_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateTicketResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateTicket',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/tickets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateTicketResponse(),
            self.execute(params, req, runtime)
        )

    async def create_ticket_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.CreateTicketResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateTicket',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/tickets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.CreateTicketResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_ticket(self) -> sls_20201230_models.CreateTicketResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ticket_with_options(headers, runtime)

    async def create_ticket_async(self) -> sls_20201230_models.CreateTicketResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ticket_with_options_async(headers, runtime)

    def delete_annotation_data_with_options(
        self,
        dataset_id: str,
        annotationdata_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteAnnotationDataResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}/annotationdata/{annotationdata_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_annotation_data_with_options_async(
        self,
        dataset_id: str,
        annotationdata_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteAnnotationDataResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}/annotationdata/{annotationdata_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAnnotationDataResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_annotation_data(
        self,
        dataset_id: str,
        annotationdata_id: str,
    ) -> sls_20201230_models.DeleteAnnotationDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_annotation_data_with_options(dataset_id, annotationdata_id, headers, runtime)

    async def delete_annotation_data_async(
        self,
        dataset_id: str,
        annotationdata_id: str,
    ) -> sls_20201230_models.DeleteAnnotationDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_annotation_data_with_options_async(dataset_id, annotationdata_id, headers, runtime)

    def delete_annotation_data_set_with_options(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteAnnotationDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_annotation_data_set_with_options_async(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteAnnotationDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAnnotationDataSetResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_annotation_data_set(
        self,
        dataset_id: str,
    ) -> sls_20201230_models.DeleteAnnotationDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_annotation_data_set_with_options(dataset_id, headers, runtime)

    async def delete_annotation_data_set_async(
        self,
        dataset_id: str,
    ) -> sls_20201230_models.DeleteAnnotationDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_annotation_data_set_with_options_async(dataset_id, headers, runtime)

    def delete_annotation_label_with_options(
        self,
        label_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteAnnotationLabelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationlabel/{label_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_annotation_label_with_options_async(
        self,
        label_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteAnnotationLabelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationlabel/{label_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteAnnotationLabelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_annotation_label(
        self,
        label_id: str,
    ) -> sls_20201230_models.DeleteAnnotationLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_annotation_label_with_options(label_id, headers, runtime)

    async def delete_annotation_label_async(
        self,
        label_id: str,
    ) -> sls_20201230_models.DeleteAnnotationLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_annotation_label_with_options_async(label_id, headers, runtime)

    def delete_collection_policy_with_options(
        self,
        policy_name: str,
        request: sls_20201230_models.DeleteCollectionPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteCollectionPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_code):
            query['dataCode'] = request.data_code
        if not UtilClient.is_unset(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCollectionPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/collectionpolicy/{policy_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteCollectionPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_collection_policy_with_options_async(
        self,
        policy_name: str,
        request: sls_20201230_models.DeleteCollectionPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteCollectionPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_code):
            query['dataCode'] = request.data_code
        if not UtilClient.is_unset(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCollectionPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/collectionpolicy/{policy_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteCollectionPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_collection_policy(
        self,
        policy_name: str,
        request: sls_20201230_models.DeleteCollectionPolicyRequest,
    ) -> sls_20201230_models.DeleteCollectionPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_collection_policy_with_options(policy_name, request, headers, runtime)

    async def delete_collection_policy_async(
        self,
        policy_name: str,
        request: sls_20201230_models.DeleteCollectionPolicyRequest,
    ) -> sls_20201230_models.DeleteCollectionPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_collection_policy_with_options_async(policy_name, request, headers, runtime)

    def delete_config_with_options(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/configs/{config_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_config_with_options_async(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/configs/{config_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_config(
        self,
        project: str,
        config_name: str,
    ) -> sls_20201230_models.DeleteConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_config_with_options(project, config_name, headers, runtime)

    async def delete_config_async(
        self,
        project: str,
        config_name: str,
    ) -> sls_20201230_models.DeleteConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_config_with_options_async(project, config_name, headers, runtime)

    def delete_consumer_group_with_options(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteConsumerGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteConsumerGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConsumerGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteConsumerGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_consumer_group(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
    ) -> sls_20201230_models.DeleteConsumerGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_with_options(project, logstore, consumer_group, headers, runtime)

    async def delete_consumer_group_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
    ) -> sls_20201230_models.DeleteConsumerGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_consumer_group_with_options_async(project, logstore, consumer_group, headers, runtime)

    def delete_dashboard_with_options(
        self,
        project: str,
        dashboard_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteDashboardResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/dashboards/{dashboard_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteDashboardResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_dashboard_with_options_async(
        self,
        project: str,
        dashboard_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteDashboardResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/dashboards/{dashboard_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteDashboardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_dashboard(
        self,
        project: str,
        dashboard_name: str,
    ) -> sls_20201230_models.DeleteDashboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_dashboard_with_options(project, dashboard_name, headers, runtime)

    async def delete_dashboard_async(
        self,
        project: str,
        dashboard_name: str,
    ) -> sls_20201230_models.DeleteDashboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_dashboard_with_options_async(project, dashboard_name, headers, runtime)

    def delete_domain_with_options(
        self,
        project: str,
        domain_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteDomainResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/domains/{domain_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteDomainResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        project: str,
        domain_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteDomainResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/domains/{domain_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteDomainResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_domain(
        self,
        project: str,
        domain_name: str,
    ) -> sls_20201230_models.DeleteDomainResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_domain_with_options(project, domain_name, headers, runtime)

    async def delete_domain_async(
        self,
        project: str,
        domain_name: str,
    ) -> sls_20201230_models.DeleteDomainResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_domain_with_options_async(project, domain_name, headers, runtime)

    def delete_external_store_with_options(
        self,
        project: str,
        external_store_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExternalStoreResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores/{external_store_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_external_store_with_options_async(
        self,
        project: str,
        external_store_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExternalStoreResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores/{external_store_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteExternalStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_external_store(
        self,
        project: str,
        external_store_name: str,
    ) -> sls_20201230_models.DeleteExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_external_store_with_options(project, external_store_name, headers, runtime)

    async def delete_external_store_async(
        self,
        project: str,
        external_store_name: str,
    ) -> sls_20201230_models.DeleteExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_external_store_with_options_async(project, external_store_name, headers, runtime)

    def delete_index_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteIndexResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndexResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/index',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteIndexResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_index_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteIndexResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndexResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/index',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteIndexResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_index(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.DeleteIndexResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_with_options(project, logstore, headers, runtime)

    async def delete_index_async(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.DeleteIndexResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_index_with_options_async(project, logstore, headers, runtime)

    def delete_log_store_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteLogStoreResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLogStoreResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_log_store_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteLogStoreResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLogStoreResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLogStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_log_store(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.DeleteLogStoreResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_log_store_with_options(project, logstore, headers, runtime)

    async def delete_log_store_async(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.DeleteLogStoreResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_log_store_with_options_async(project, logstore, headers, runtime)

    def delete_logging_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteLoggingResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logging',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLoggingResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_logging_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteLoggingResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logging',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLoggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_logging(
        self,
        project: str,
    ) -> sls_20201230_models.DeleteLoggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_logging_with_options(project, headers, runtime)

    async def delete_logging_async(
        self,
        project: str,
    ) -> sls_20201230_models.DeleteLoggingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_logging_with_options_async(project, headers, runtime)

    def delete_logtail_pipeline_config_with_options(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteLogtailPipelineConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/pipelineconfigs/{config_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_logtail_pipeline_config_with_options_async(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteLogtailPipelineConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/pipelineconfigs/{config_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteLogtailPipelineConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_logtail_pipeline_config(
        self,
        project: str,
        config_name: str,
    ) -> sls_20201230_models.DeleteLogtailPipelineConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_logtail_pipeline_config_with_options(project, config_name, headers, runtime)

    async def delete_logtail_pipeline_config_async(
        self,
        project: str,
        config_name: str,
    ) -> sls_20201230_models.DeleteLogtailPipelineConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_logtail_pipeline_config_with_options_async(project, config_name, headers, runtime)

    def delete_machine_group_with_options(
        self,
        project: str,
        machine_group: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteMachineGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMachineGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_machine_group_with_options_async(
        self,
        project: str,
        machine_group: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteMachineGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMachineGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_machine_group(
        self,
        project: str,
        machine_group: str,
    ) -> sls_20201230_models.DeleteMachineGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_machine_group_with_options(project, machine_group, headers, runtime)

    async def delete_machine_group_async(
        self,
        project: str,
        machine_group: str,
    ) -> sls_20201230_models.DeleteMachineGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_machine_group_with_options_async(project, machine_group, headers, runtime)

    def delete_project_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteProjectResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteProjectResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_project(
        self,
        project: str,
    ) -> sls_20201230_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project, headers, runtime)

    async def delete_project_async(
        self,
        project: str,
    ) -> sls_20201230_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(project, headers, runtime)

    def delete_project_policy_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteProjectPolicyResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectPolicyResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProjectPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/policy',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteProjectPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_project_policy_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteProjectPolicyResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectPolicyResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProjectPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/policy',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteProjectPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_project_policy(
        self,
        project: str,
    ) -> sls_20201230_models.DeleteProjectPolicyResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteProjectPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_policy_with_options(project, headers, runtime)

    async def delete_project_policy_async(
        self,
        project: str,
    ) -> sls_20201230_models.DeleteProjectPolicyResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteProjectPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_policy_with_options_async(project, headers, runtime)

    def delete_saved_search_with_options(
        self,
        project: str,
        savedsearch_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSavedSearchResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches/{savedsearch_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_saved_search_with_options_async(
        self,
        project: str,
        savedsearch_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSavedSearchResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches/{savedsearch_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_saved_search(
        self,
        project: str,
        savedsearch_name: str,
    ) -> sls_20201230_models.DeleteSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteSavedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_saved_search_with_options(project, savedsearch_name, headers, runtime)

    async def delete_saved_search_async(
        self,
        project: str,
        savedsearch_name: str,
    ) -> sls_20201230_models.DeleteSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteSavedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_saved_search_with_options_async(project, savedsearch_name, headers, runtime)

    def delete_shipper_with_options(
        self,
        project: str,
        logstore: str,
        shipper_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteShipperResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteShipperResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteShipper',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shipper/{shipper_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteShipperResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_shipper_with_options_async(
        self,
        project: str,
        logstore: str,
        shipper_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.DeleteShipperResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteShipperResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteShipper',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shipper/{shipper_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.DeleteShipperResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_shipper(
        self,
        project: str,
        logstore: str,
        shipper_name: str,
    ) -> sls_20201230_models.DeleteShipperResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteShipperResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_shipper_with_options(project, logstore, shipper_name, headers, runtime)

    async def delete_shipper_async(
        self,
        project: str,
        logstore: str,
        shipper_name: str,
    ) -> sls_20201230_models.DeleteShipperResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: DeleteShipperResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_shipper_with_options_async(project, logstore, shipper_name, headers, runtime)

    def get_annotation_data_with_options(
        self,
        dataset_id: str,
        annotationdata_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetAnnotationDataResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}/annotationdata/{annotationdata_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    async def get_annotation_data_with_options_async(
        self,
        dataset_id: str,
        annotationdata_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetAnnotationDataResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}/annotationdata/{annotationdata_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAnnotationDataResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_annotation_data(
        self,
        dataset_id: str,
        annotationdata_id: str,
    ) -> sls_20201230_models.GetAnnotationDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_annotation_data_with_options(dataset_id, annotationdata_id, headers, runtime)

    async def get_annotation_data_async(
        self,
        dataset_id: str,
        annotationdata_id: str,
    ) -> sls_20201230_models.GetAnnotationDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_annotation_data_with_options_async(dataset_id, annotationdata_id, headers, runtime)

    def get_annotation_data_set_with_options(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetAnnotationDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    async def get_annotation_data_set_with_options_async(
        self,
        dataset_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetAnnotationDataSetResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAnnotationDataSetResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_annotation_data_set(
        self,
        dataset_id: str,
    ) -> sls_20201230_models.GetAnnotationDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_annotation_data_set_with_options(dataset_id, headers, runtime)

    async def get_annotation_data_set_async(
        self,
        dataset_id: str,
    ) -> sls_20201230_models.GetAnnotationDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_annotation_data_set_with_options_async(dataset_id, headers, runtime)

    def get_annotation_label_with_options(
        self,
        label_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetAnnotationLabelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationlabel/{label_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    async def get_annotation_label_with_options_async(
        self,
        label_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetAnnotationLabelResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationlabel/{label_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAnnotationLabelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_annotation_label(
        self,
        label_id: str,
    ) -> sls_20201230_models.GetAnnotationLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_annotation_label_with_options(label_id, headers, runtime)

    async def get_annotation_label_async(
        self,
        label_id: str,
    ) -> sls_20201230_models.GetAnnotationLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_annotation_label_with_options_async(label_id, headers, runtime)

    def get_applied_configs_with_options(
        self,
        project: str,
        machine_group: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetAppliedConfigsResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppliedConfigsResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppliedConfigs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAppliedConfigsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_applied_configs_with_options_async(
        self,
        project: str,
        machine_group: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetAppliedConfigsResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppliedConfigsResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppliedConfigs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAppliedConfigsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_applied_configs(
        self,
        project: str,
        machine_group: str,
    ) -> sls_20201230_models.GetAppliedConfigsResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetAppliedConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_applied_configs_with_options(project, machine_group, headers, runtime)

    async def get_applied_configs_async(
        self,
        project: str,
        machine_group: str,
    ) -> sls_20201230_models.GetAppliedConfigsResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetAppliedConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_applied_configs_with_options_async(project, machine_group, headers, runtime)

    def get_applied_machine_groups_with_options(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetAppliedMachineGroupsResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppliedMachineGroupsResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppliedMachineGroups',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/configs/{config_name}/machinegroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAppliedMachineGroupsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_applied_machine_groups_with_options_async(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetAppliedMachineGroupsResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppliedMachineGroupsResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppliedMachineGroups',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/configs/{config_name}/machinegroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetAppliedMachineGroupsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_applied_machine_groups(
        self,
        project: str,
        config_name: str,
    ) -> sls_20201230_models.GetAppliedMachineGroupsResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetAppliedMachineGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_applied_machine_groups_with_options(project, config_name, headers, runtime)

    async def get_applied_machine_groups_async(
        self,
        project: str,
        config_name: str,
    ) -> sls_20201230_models.GetAppliedMachineGroupsResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetAppliedMachineGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_applied_machine_groups_with_options_async(project, config_name, headers, runtime)

    def get_check_point_with_options(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.GetCheckPointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetCheckPointResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetCheckPointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCheckPointResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.shard):
            query['shard'] = request.shard
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCheckPoint',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCheckPointResponse(),
            self.execute(params, req, runtime)
        )

    async def get_check_point_with_options_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.GetCheckPointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetCheckPointResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetCheckPointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCheckPointResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.shard):
            query['shard'] = request.shard
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCheckPoint',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCheckPointResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_check_point(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.GetCheckPointRequest,
    ) -> sls_20201230_models.GetCheckPointResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetCheckPointRequest
        @return: GetCheckPointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_check_point_with_options(project, logstore, consumer_group, request, headers, runtime)

    async def get_check_point_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.GetCheckPointRequest,
    ) -> sls_20201230_models.GetCheckPointResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetCheckPointRequest
        @return: GetCheckPointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_check_point_with_options_async(project, logstore, consumer_group, request, headers, runtime)

    def get_collection_policy_with_options(
        self,
        policy_name: str,
        request: sls_20201230_models.GetCollectionPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetCollectionPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_code):
            query['dataCode'] = request.data_code
        if not UtilClient.is_unset(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCollectionPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/collectionpolicy/{policy_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCollectionPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def get_collection_policy_with_options_async(
        self,
        policy_name: str,
        request: sls_20201230_models.GetCollectionPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetCollectionPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_code):
            query['dataCode'] = request.data_code
        if not UtilClient.is_unset(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCollectionPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/collectionpolicy/{policy_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCollectionPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_collection_policy(
        self,
        policy_name: str,
        request: sls_20201230_models.GetCollectionPolicyRequest,
    ) -> sls_20201230_models.GetCollectionPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_collection_policy_with_options(policy_name, request, headers, runtime)

    async def get_collection_policy_async(
        self,
        policy_name: str,
        request: sls_20201230_models.GetCollectionPolicyRequest,
    ) -> sls_20201230_models.GetCollectionPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_collection_policy_with_options_async(policy_name, request, headers, runtime)

    def get_config_with_options(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/configs/{config_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def get_config_with_options_async(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/configs/{config_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_config(
        self,
        project: str,
        config_name: str,
    ) -> sls_20201230_models.GetConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_config_with_options(project, config_name, headers, runtime)

    async def get_config_async(
        self,
        project: str,
        config_name: str,
    ) -> sls_20201230_models.GetConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_config_with_options_async(project, config_name, headers, runtime)

    def get_context_logs_with_options(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetContextLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetContextLogsResponse:
        """
        You can specify a log as the start log. The time range of a contextual query is one day before and one day after the generation time of the start log.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetContextLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContextLogsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.back_lines):
            query['back_lines'] = request.back_lines
        if not UtilClient.is_unset(request.forward_lines):
            query['forward_lines'] = request.forward_lines
        if not UtilClient.is_unset(request.pack_id):
            query['pack_id'] = request.pack_id
        if not UtilClient.is_unset(request.pack_meta):
            query['pack_meta'] = request.pack_meta
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContextLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetContextLogsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_context_logs_with_options_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetContextLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetContextLogsResponse:
        """
        You can specify a log as the start log. The time range of a contextual query is one day before and one day after the generation time of the start log.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetContextLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContextLogsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.back_lines):
            query['back_lines'] = request.back_lines
        if not UtilClient.is_unset(request.forward_lines):
            query['forward_lines'] = request.forward_lines
        if not UtilClient.is_unset(request.pack_id):
            query['pack_id'] = request.pack_id
        if not UtilClient.is_unset(request.pack_meta):
            query['pack_meta'] = request.pack_meta
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContextLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetContextLogsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_context_logs(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetContextLogsRequest,
    ) -> sls_20201230_models.GetContextLogsResponse:
        """
        You can specify a log as the start log. The time range of a contextual query is one day before and one day after the generation time of the start log.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetContextLogsRequest
        @return: GetContextLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_context_logs_with_options(project, logstore, request, headers, runtime)

    async def get_context_logs_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetContextLogsRequest,
    ) -> sls_20201230_models.GetContextLogsResponse:
        """
        You can specify a log as the start log. The time range of a contextual query is one day before and one day after the generation time of the start log.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetContextLogsRequest
        @return: GetContextLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_context_logs_with_options_async(project, logstore, request, headers, runtime)

    def get_cursor_with_options(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: sls_20201230_models.GetCursorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetCursorResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   The following content describes the relationships among a cursor, project, Logstore, and shard:
        *   A project can have multiple Logstores.
        *   A Logstore can have multiple shards.
        *   You can use a cursor to obtain a log in a shard.
        
        @param request: GetCursorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCursorResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCursor',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shards/{shard_id}?type=cursor',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCursorResponse(),
            self.execute(params, req, runtime)
        )

    async def get_cursor_with_options_async(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: sls_20201230_models.GetCursorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetCursorResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   The following content describes the relationships among a cursor, project, Logstore, and shard:
        *   A project can have multiple Logstores.
        *   A Logstore can have multiple shards.
        *   You can use a cursor to obtain a log in a shard.
        
        @param request: GetCursorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCursorResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCursor',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shards/{shard_id}?type=cursor',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCursorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_cursor(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: sls_20201230_models.GetCursorRequest,
    ) -> sls_20201230_models.GetCursorResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   The following content describes the relationships among a cursor, project, Logstore, and shard:
        *   A project can have multiple Logstores.
        *   A Logstore can have multiple shards.
        *   You can use a cursor to obtain a log in a shard.
        
        @param request: GetCursorRequest
        @return: GetCursorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cursor_with_options(project, logstore, shard_id, request, headers, runtime)

    async def get_cursor_async(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: sls_20201230_models.GetCursorRequest,
    ) -> sls_20201230_models.GetCursorResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   The following content describes the relationships among a cursor, project, Logstore, and shard:
        *   A project can have multiple Logstores.
        *   A Logstore can have multiple shards.
        *   You can use a cursor to obtain a log in a shard.
        
        @param request: GetCursorRequest
        @return: GetCursorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cursor_with_options_async(project, logstore, shard_id, request, headers, runtime)

    def get_cursor_time_with_options(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: sls_20201230_models.GetCursorTimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetCursorTimeResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['cursor'] = request.cursor
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCursorTime',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shards/{shard_id}?type=cursor_time',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCursorTimeResponse(),
            self.execute(params, req, runtime)
        )

    async def get_cursor_time_with_options_async(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: sls_20201230_models.GetCursorTimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetCursorTimeResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.cursor):
            query['cursor'] = request.cursor
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCursorTime',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shards/{shard_id}?type=cursor_time',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetCursorTimeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_cursor_time(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: sls_20201230_models.GetCursorTimeRequest,
    ) -> sls_20201230_models.GetCursorTimeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cursor_time_with_options(project, logstore, shard_id, request, headers, runtime)

    async def get_cursor_time_async(
        self,
        project: str,
        logstore: str,
        shard_id: str,
        request: sls_20201230_models.GetCursorTimeRequest,
    ) -> sls_20201230_models.GetCursorTimeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cursor_time_with_options_async(project, logstore, shard_id, request, headers, runtime)

    def get_dashboard_with_options(
        self,
        project: str,
        dashboard_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetDashboardResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/dashboards/{dashboard_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetDashboardResponse(),
            self.execute(params, req, runtime)
        )

    async def get_dashboard_with_options_async(
        self,
        project: str,
        dashboard_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetDashboardResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/dashboards/{dashboard_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetDashboardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_dashboard(
        self,
        project: str,
        dashboard_name: str,
    ) -> sls_20201230_models.GetDashboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_dashboard_with_options(project, dashboard_name, headers, runtime)

    async def get_dashboard_async(
        self,
        project: str,
        dashboard_name: str,
    ) -> sls_20201230_models.GetDashboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_dashboard_with_options_async(project, dashboard_name, headers, runtime)

    def get_external_store_with_options(
        self,
        project: str,
        external_store_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetExternalStoreResponse:
        """
        The supported data sources of external stores include Object Storage Service (OSS) buckets and ApsaraDB RDS for MySQL databases in a virtual private cloud (VPC).
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExternalStoreResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores/{external_store_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def get_external_store_with_options_async(
        self,
        project: str,
        external_store_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetExternalStoreResponse:
        """
        The supported data sources of external stores include Object Storage Service (OSS) buckets and ApsaraDB RDS for MySQL databases in a virtual private cloud (VPC).
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExternalStoreResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores/{external_store_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetExternalStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_external_store(
        self,
        project: str,
        external_store_name: str,
    ) -> sls_20201230_models.GetExternalStoreResponse:
        """
        The supported data sources of external stores include Object Storage Service (OSS) buckets and ApsaraDB RDS for MySQL databases in a virtual private cloud (VPC).
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_external_store_with_options(project, external_store_name, headers, runtime)

    async def get_external_store_async(
        self,
        project: str,
        external_store_name: str,
    ) -> sls_20201230_models.GetExternalStoreResponse:
        """
        The supported data sources of external stores include Object Storage Service (OSS) buckets and ApsaraDB RDS for MySQL databases in a virtual private cloud (VPC).
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_external_store_with_options_async(project, external_store_name, headers, runtime)

    def get_histograms_with_options(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetHistogramsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetHistogramsResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   The time range is evenly divided into subintervals in the responses. If the time range that is specified in the request remains unchanged, the subintervals in the responses also remain unchanged.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot predict the number of times that you must call this operation to obtain the complete result. In this case, you must check the value of the progress parameter in the response of each request and determine whether to call this operation one more time to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log after a short latency. The latency of a query varies based on the type of the log. Simple Log Service classifies logs into the following types based on the log time:
        *   Real-time data: The difference between the time record in a log and the current time on Simple Log Service is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as real-time data. After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds.
        *   Historical data: The difference between the time record in a log and the current time on Simple Log Service is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as historical data. This type of log is usually generated in data backfill scenarios.
        After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        > Simple Log Service calculates the difference between the log time that is specified by the \\__time\\_\\_ field and the receiving time that is specified by the \\__tag\\_\\_:\\__receive_time\\_\\_ field for each log. The receiving time indicates the time at which Simple Log Service receives the log. If the difference is within the interval (-180 seconds,900 seconds], Simple Log Service processes the log as real-time data. If the difference is within the interval \\[-604,800 seconds,-180 seconds), Simple Log Service processes the log as historical data.
        *   Simple Log Service provides examples on how to call the GetHistograms operation by using Simple Log Service SDK for Java. For more information, see [Use GetHistograms to query the distribution of logs](~~462234~~).
        
        @param request: GetHistogramsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHistogramsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            query['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistograms',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/index?type=histogram',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetHistogramsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_histograms_with_options_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetHistogramsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetHistogramsResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   The time range is evenly divided into subintervals in the responses. If the time range that is specified in the request remains unchanged, the subintervals in the responses also remain unchanged.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot predict the number of times that you must call this operation to obtain the complete result. In this case, you must check the value of the progress parameter in the response of each request and determine whether to call this operation one more time to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log after a short latency. The latency of a query varies based on the type of the log. Simple Log Service classifies logs into the following types based on the log time:
        *   Real-time data: The difference between the time record in a log and the current time on Simple Log Service is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as real-time data. After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds.
        *   Historical data: The difference between the time record in a log and the current time on Simple Log Service is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as historical data. This type of log is usually generated in data backfill scenarios.
        After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        > Simple Log Service calculates the difference between the log time that is specified by the \\__time\\_\\_ field and the receiving time that is specified by the \\__tag\\_\\_:\\__receive_time\\_\\_ field for each log. The receiving time indicates the time at which Simple Log Service receives the log. If the difference is within the interval (-180 seconds,900 seconds], Simple Log Service processes the log as real-time data. If the difference is within the interval \\[-604,800 seconds,-180 seconds), Simple Log Service processes the log as historical data.
        *   Simple Log Service provides examples on how to call the GetHistograms operation by using Simple Log Service SDK for Java. For more information, see [Use GetHistograms to query the distribution of logs](~~462234~~).
        
        @param request: GetHistogramsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHistogramsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            query['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistograms',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/index?type=histogram',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetHistogramsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_histograms(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetHistogramsRequest,
    ) -> sls_20201230_models.GetHistogramsResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   The time range is evenly divided into subintervals in the responses. If the time range that is specified in the request remains unchanged, the subintervals in the responses also remain unchanged.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot predict the number of times that you must call this operation to obtain the complete result. In this case, you must check the value of the progress parameter in the response of each request and determine whether to call this operation one more time to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log after a short latency. The latency of a query varies based on the type of the log. Simple Log Service classifies logs into the following types based on the log time:
        *   Real-time data: The difference between the time record in a log and the current time on Simple Log Service is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as real-time data. After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds.
        *   Historical data: The difference between the time record in a log and the current time on Simple Log Service is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as historical data. This type of log is usually generated in data backfill scenarios.
        After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        > Simple Log Service calculates the difference between the log time that is specified by the \\__time\\_\\_ field and the receiving time that is specified by the \\__tag\\_\\_:\\__receive_time\\_\\_ field for each log. The receiving time indicates the time at which Simple Log Service receives the log. If the difference is within the interval (-180 seconds,900 seconds], Simple Log Service processes the log as real-time data. If the difference is within the interval \\[-604,800 seconds,-180 seconds), Simple Log Service processes the log as historical data.
        *   Simple Log Service provides examples on how to call the GetHistograms operation by using Simple Log Service SDK for Java. For more information, see [Use GetHistograms to query the distribution of logs](~~462234~~).
        
        @param request: GetHistogramsRequest
        @return: GetHistogramsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_histograms_with_options(project, logstore, request, headers, runtime)

    async def get_histograms_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetHistogramsRequest,
    ) -> sls_20201230_models.GetHistogramsResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   The time range is evenly divided into subintervals in the responses. If the time range that is specified in the request remains unchanged, the subintervals in the responses also remain unchanged.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot predict the number of times that you must call this operation to obtain the complete result. In this case, you must check the value of the progress parameter in the response of each request and determine whether to call this operation one more time to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log after a short latency. The latency of a query varies based on the type of the log. Simple Log Service classifies logs into the following types based on the log time:
        *   Real-time data: The difference between the time record in a log and the current time on Simple Log Service is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as real-time data. After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds.
        *   Historical data: The difference between the time record in a log and the current time on Simple Log Service is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as historical data. This type of log is usually generated in data backfill scenarios.
        After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        > Simple Log Service calculates the difference between the log time that is specified by the \\__time\\_\\_ field and the receiving time that is specified by the \\__tag\\_\\_:\\__receive_time\\_\\_ field for each log. The receiving time indicates the time at which Simple Log Service receives the log. If the difference is within the interval (-180 seconds,900 seconds], Simple Log Service processes the log as real-time data. If the difference is within the interval \\[-604,800 seconds,-180 seconds), Simple Log Service processes the log as historical data.
        *   Simple Log Service provides examples on how to call the GetHistograms operation by using Simple Log Service SDK for Java. For more information, see [Use GetHistograms to query the distribution of logs](~~462234~~).
        
        @param request: GetHistogramsRequest
        @return: GetHistogramsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_histograms_with_options_async(project, logstore, request, headers, runtime)

    def get_index_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetIndexResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIndexResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/index',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetIndexResponse(),
            self.execute(params, req, runtime)
        )

    async def get_index_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetIndexResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIndexResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/index',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetIndexResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_index(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.GetIndexResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_index_with_options(project, logstore, headers, runtime)

    async def get_index_async(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.GetIndexResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_index_with_options_async(project, logstore, headers, runtime)

    def get_log_store_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLogStoreResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogStoreResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def get_log_store_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLogStoreResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogStoreResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_log_store(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.GetLogStoreResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_log_store_with_options(project, logstore, headers, runtime)

    async def get_log_store_async(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.GetLogStoreResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_log_store_with_options_async(project, logstore, headers, runtime)

    def get_log_store_metering_mode_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLogStoreMeteringModeResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogStoreMeteringMode',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/meteringmode',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogStoreMeteringModeResponse(),
            self.execute(params, req, runtime)
        )

    async def get_log_store_metering_mode_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLogStoreMeteringModeResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogStoreMeteringMode',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/meteringmode',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogStoreMeteringModeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_log_store_metering_mode(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.GetLogStoreMeteringModeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_log_store_metering_mode_with_options(project, logstore, headers, runtime)

    async def get_log_store_metering_mode_async(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.GetLogStoreMeteringModeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_log_store_metering_mode_with_options_async(project, logstore, headers, runtime)

    def get_logging_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLoggingResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoggingResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logging',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLoggingResponse(),
            self.execute(params, req, runtime)
        )

    async def get_logging_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLoggingResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoggingResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logging',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLoggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_logging(
        self,
        project: str,
    ) -> sls_20201230_models.GetLoggingResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_logging_with_options(project, headers, runtime)

    async def get_logging_async(
        self,
        project: str,
    ) -> sls_20201230_models.GetLoggingResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_logging_with_options_async(project, headers, runtime)

    def get_logs_with_options(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLogsResponse:
        """
        ### Usage notes
        > Simple Log Service allows you to create a Scheduled SQL job. For more information, see [Create a Scheduled SQL job](~~286457~~).
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot forecast the number of times that you must call this operation to obtain the complete result. In this case, you must check the value of the x-log-progress parameter in the response of each request and determine whether to call this operation one more time to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log after a short latency. The latency of a query varies based on the type of the log. Simple Log Service classifies logs into the following types based on the log time:
        Real-time data: The difference between the time record in a log and the current time on Simple Log Service is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as real-time data. This type of log is usually generated in common scenarios.
        *   Historical data: The difference between the time record in a log and the current time on Simple Log Service is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as historical data. This type of log is usually generated in data backfill scenarios.
        After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        > Simple Log Service calculates the difference between the log time that is specified by the \\__time\\_\\_ field and the receiving time that is specified by the \\__tag\\_\\_:**receive_time** field for each log. The receiving time indicates the time at which Simple Log Service receives the log. If the difference is within the interval (-180 seconds,900 seconds], Simple Log Service processes the log as real-time data. If the difference is within the interval \\[-604,800 seconds,-180 seconds), Simple Log Service processes the log as historical data.
        *   Simple Log Service provides examples on how to call the GetLogs operation by using Simple Log Service SDK for Java and Simple Log Service SDK for Python. For more information, see [Examples of calling the GetLogs operation by using Simple Log Service SDK for Java](~~407683~~) and [Examples of calling the GetLogs operation by using Simple Log Service SDK for Python](~~407684~~).
        
        @param request: GetLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.line):
            query['line'] = request.line
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.power_sql):
            query['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.reverse):
            query['reverse'] = request.reverse
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            query['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}?type=log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_logs_with_options_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLogsResponse:
        """
        ### Usage notes
        > Simple Log Service allows you to create a Scheduled SQL job. For more information, see [Create a Scheduled SQL job](~~286457~~).
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot forecast the number of times that you must call this operation to obtain the complete result. In this case, you must check the value of the x-log-progress parameter in the response of each request and determine whether to call this operation one more time to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log after a short latency. The latency of a query varies based on the type of the log. Simple Log Service classifies logs into the following types based on the log time:
        Real-time data: The difference between the time record in a log and the current time on Simple Log Service is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as real-time data. This type of log is usually generated in common scenarios.
        *   Historical data: The difference between the time record in a log and the current time on Simple Log Service is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as historical data. This type of log is usually generated in data backfill scenarios.
        After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        > Simple Log Service calculates the difference between the log time that is specified by the \\__time\\_\\_ field and the receiving time that is specified by the \\__tag\\_\\_:**receive_time** field for each log. The receiving time indicates the time at which Simple Log Service receives the log. If the difference is within the interval (-180 seconds,900 seconds], Simple Log Service processes the log as real-time data. If the difference is within the interval \\[-604,800 seconds,-180 seconds), Simple Log Service processes the log as historical data.
        *   Simple Log Service provides examples on how to call the GetLogs operation by using Simple Log Service SDK for Java and Simple Log Service SDK for Python. For more information, see [Examples of calling the GetLogs operation by using Simple Log Service SDK for Java](~~407683~~) and [Examples of calling the GetLogs operation by using Simple Log Service SDK for Python](~~407684~~).
        
        @param request: GetLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.line):
            query['line'] = request.line
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.power_sql):
            query['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.reverse):
            query['reverse'] = request.reverse
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            query['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}?type=log',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_logs(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetLogsRequest,
    ) -> sls_20201230_models.GetLogsResponse:
        """
        ### Usage notes
        > Simple Log Service allows you to create a Scheduled SQL job. For more information, see [Create a Scheduled SQL job](~~286457~~).
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot forecast the number of times that you must call this operation to obtain the complete result. In this case, you must check the value of the x-log-progress parameter in the response of each request and determine whether to call this operation one more time to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log after a short latency. The latency of a query varies based on the type of the log. Simple Log Service classifies logs into the following types based on the log time:
        Real-time data: The difference between the time record in a log and the current time on Simple Log Service is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as real-time data. This type of log is usually generated in common scenarios.
        *   Historical data: The difference between the time record in a log and the current time on Simple Log Service is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as historical data. This type of log is usually generated in data backfill scenarios.
        After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        > Simple Log Service calculates the difference between the log time that is specified by the \\__time\\_\\_ field and the receiving time that is specified by the \\__tag\\_\\_:**receive_time** field for each log. The receiving time indicates the time at which Simple Log Service receives the log. If the difference is within the interval (-180 seconds,900 seconds], Simple Log Service processes the log as real-time data. If the difference is within the interval \\[-604,800 seconds,-180 seconds), Simple Log Service processes the log as historical data.
        *   Simple Log Service provides examples on how to call the GetLogs operation by using Simple Log Service SDK for Java and Simple Log Service SDK for Python. For more information, see [Examples of calling the GetLogs operation by using Simple Log Service SDK for Java](~~407683~~) and [Examples of calling the GetLogs operation by using Simple Log Service SDK for Python](~~407684~~).
        
        @param request: GetLogsRequest
        @return: GetLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_logs_with_options(project, logstore, request, headers, runtime)

    async def get_logs_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetLogsRequest,
    ) -> sls_20201230_models.GetLogsResponse:
        """
        ### Usage notes
        > Simple Log Service allows you to create a Scheduled SQL job. For more information, see [Create a Scheduled SQL job](~~286457~~).
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot forecast the number of times that you must call this operation to obtain the complete result. In this case, you must check the value of the x-log-progress parameter in the response of each request and determine whether to call this operation one more time to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log after a short latency. The latency of a query varies based on the type of the log. Simple Log Service classifies logs into the following types based on the log time:
        Real-time data: The difference between the time record in a log and the current time on Simple Log Service is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as real-time data. This type of log is usually generated in common scenarios.
        *   Historical data: The difference between the time record in a log and the current time on Simple Log Service is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and Simple Log Service received the log at 12:05:00, September 25, 2014 (UTC), Simple Log Service processes the log as historical data. This type of log is usually generated in data backfill scenarios.
        After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        > Simple Log Service calculates the difference between the log time that is specified by the \\__time\\_\\_ field and the receiving time that is specified by the \\__tag\\_\\_:**receive_time** field for each log. The receiving time indicates the time at which Simple Log Service receives the log. If the difference is within the interval (-180 seconds,900 seconds], Simple Log Service processes the log as real-time data. If the difference is within the interval \\[-604,800 seconds,-180 seconds), Simple Log Service processes the log as historical data.
        *   Simple Log Service provides examples on how to call the GetLogs operation by using Simple Log Service SDK for Java and Simple Log Service SDK for Python. For more information, see [Examples of calling the GetLogs operation by using Simple Log Service SDK for Java](~~407683~~) and [Examples of calling the GetLogs operation by using Simple Log Service SDK for Python](~~407684~~).
        
        @param request: GetLogsRequest
        @return: GetLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_logs_with_options_async(project, logstore, request, headers, runtime)

    def get_logs_v2with_options(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetLogsV2Request,
        headers: sls_20201230_models.GetLogsV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLogsV2Response:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot predict the number of times you must call this API operation to obtain a complete result. In this case, you must check the value of the progress parameter in the response of each request and determine whether to call this operation again to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log. The latency of the query varies based on the type of the log. Simple Log Service classifies logs into the following types based on log timestamps:
        1.  1.  Real-time data: The difference between the time record in the log and the current server time is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and the server received the log at 12:05:00, September 25, 2014 (UTC), the server processes the log as real-time data. This type of log is usually generated in common scenarios.
        2.  2.  Historical data: The difference between the time record in the log and the current server time is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and the server received the log at 12:05:00, September 25, 2014 (UTC), the server processes the log as historical data. This type of log is usually generated in data backfill scenarios. After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        
        @param request: GetLogsV2Request
        @param headers: GetLogsV2Headers
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogsV2Response
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.forward):
            body['forward'] = request.forward
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.offset):
            body['offset'] = request.offset
        if not UtilClient.is_unset(request.power_sql):
            body['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.reverse):
            body['reverse'] = request.reverse
        if not UtilClient.is_unset(request.session):
            body['session'] = request.session
        if not UtilClient.is_unset(request.shard):
            body['shard'] = request.shard
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.accept_encoding):
            real_headers['Accept-Encoding'] = UtilClient.to_jsonstring(headers.accept_encoding)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLogsV2',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/logs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogsV2Response(),
            self.execute(params, req, runtime)
        )

    async def get_logs_v2with_options_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetLogsV2Request,
        headers: sls_20201230_models.GetLogsV2Headers,
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLogsV2Response:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot predict the number of times you must call this API operation to obtain a complete result. In this case, you must check the value of the progress parameter in the response of each request and determine whether to call this operation again to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log. The latency of the query varies based on the type of the log. Simple Log Service classifies logs into the following types based on log timestamps:
        1.  1.  Real-time data: The difference between the time record in the log and the current server time is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and the server received the log at 12:05:00, September 25, 2014 (UTC), the server processes the log as real-time data. This type of log is usually generated in common scenarios.
        2.  2.  Historical data: The difference between the time record in the log and the current server time is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and the server received the log at 12:05:00, September 25, 2014 (UTC), the server processes the log as historical data. This type of log is usually generated in data backfill scenarios. After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        
        @param request: GetLogsV2Request
        @param headers: GetLogsV2Headers
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogsV2Response
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.forward):
            body['forward'] = request.forward
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.offset):
            body['offset'] = request.offset
        if not UtilClient.is_unset(request.power_sql):
            body['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.reverse):
            body['reverse'] = request.reverse
        if not UtilClient.is_unset(request.session):
            body['session'] = request.session
        if not UtilClient.is_unset(request.shard):
            body['shard'] = request.shard
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.accept_encoding):
            real_headers['Accept-Encoding'] = UtilClient.to_jsonstring(headers.accept_encoding)
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLogsV2',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/logs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogsV2Response(),
            await self.execute_async(params, req, runtime)
        )

    def get_logs_v2(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetLogsV2Request,
    ) -> sls_20201230_models.GetLogsV2Response:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot predict the number of times you must call this API operation to obtain a complete result. In this case, you must check the value of the progress parameter in the response of each request and determine whether to call this operation again to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log. The latency of the query varies based on the type of the log. Simple Log Service classifies logs into the following types based on log timestamps:
        1.  1.  Real-time data: The difference between the time record in the log and the current server time is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and the server received the log at 12:05:00, September 25, 2014 (UTC), the server processes the log as real-time data. This type of log is usually generated in common scenarios.
        2.  2.  Historical data: The difference between the time record in the log and the current server time is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and the server received the log at 12:05:00, September 25, 2014 (UTC), the server processes the log as historical data. This type of log is usually generated in data backfill scenarios. After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        
        @param request: GetLogsV2Request
        @return: GetLogsV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = sls_20201230_models.GetLogsV2Headers()
        return self.get_logs_v2with_options(project, logstore, request, headers, runtime)

    async def get_logs_v2_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.GetLogsV2Request,
    ) -> sls_20201230_models.GetLogsV2Response:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   If the number of logs in a Logstore significantly changes, Simple Log Service cannot predict the number of times you must call this API operation to obtain a complete result. In this case, you must check the value of the progress parameter in the response of each request and determine whether to call this operation again to obtain the complete result. Each time you call this operation, the same number of charge units (CUs) are consumed.
        *   After a log is written to a Logstore, you can call the GetHistograms or GetLogs operation to query the log. The latency of the query varies based on the type of the log. Simple Log Service classifies logs into the following types based on log timestamps:
        1.  1.  Real-time data: The difference between the time record in the log and the current server time is within the interval (-180 seconds,900 seconds]. For example, if a log was generated at 12:03:00, September 25, 2014 (UTC) and the server received the log at 12:05:00, September 25, 2014 (UTC), the server processes the log as real-time data. This type of log is usually generated in common scenarios.
        2.  2.  Historical data: The difference between the time record in the log and the current server time is within the interval \\[-604,800 seconds,-180 seconds). For example, if a log was generated at 12:00:00, September 25, 2014 (UTC) and the server received the log at 12:05:00, September 25, 2014 (UTC), the server processes the log as historical data. This type of log is usually generated in data backfill scenarios. After real-time data is written to a Logstore, the data can be queried with a maximum latency of 3 seconds. For 99.9% of queries, the latency is no more than 1 second.
        
        @param request: GetLogsV2Request
        @return: GetLogsV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = sls_20201230_models.GetLogsV2Headers()
        return await self.get_logs_v2with_options_async(project, logstore, request, headers, runtime)

    def get_logtail_pipeline_config_with_options(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLogtailPipelineConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/pipelineconfigs/{config_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def get_logtail_pipeline_config_with_options_async(
        self,
        project: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetLogtailPipelineConfigResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/pipelineconfigs/{config_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetLogtailPipelineConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_logtail_pipeline_config(
        self,
        project: str,
        config_name: str,
    ) -> sls_20201230_models.GetLogtailPipelineConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_logtail_pipeline_config_with_options(project, config_name, headers, runtime)

    async def get_logtail_pipeline_config_async(
        self,
        project: str,
        config_name: str,
    ) -> sls_20201230_models.GetLogtailPipelineConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_logtail_pipeline_config_with_options_async(project, config_name, headers, runtime)

    def get_mlservice_results_with_options(
        self,
        service_name: str,
        request: sls_20201230_models.GetMLServiceResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetMLServiceResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_builtin):
            query['allowBuiltin'] = request.allow_builtin
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='GetMLServiceResults',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/service/{service_name}/analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetMLServiceResultsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_mlservice_results_with_options_async(
        self,
        service_name: str,
        request: sls_20201230_models.GetMLServiceResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetMLServiceResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_builtin):
            query['allowBuiltin'] = request.allow_builtin
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='GetMLServiceResults',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/service/{service_name}/analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetMLServiceResultsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_mlservice_results(
        self,
        service_name: str,
        request: sls_20201230_models.GetMLServiceResultsRequest,
    ) -> sls_20201230_models.GetMLServiceResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mlservice_results_with_options(service_name, request, headers, runtime)

    async def get_mlservice_results_async(
        self,
        service_name: str,
        request: sls_20201230_models.GetMLServiceResultsRequest,
    ) -> sls_20201230_models.GetMLServiceResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mlservice_results_with_options_async(service_name, request, headers, runtime)

    def get_machine_group_with_options(
        self,
        project: str,
        machine_group: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMachineGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def get_machine_group_with_options_async(
        self,
        project: str,
        machine_group: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMachineGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_machine_group(
        self,
        project: str,
        machine_group: str,
    ) -> sls_20201230_models.GetMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_machine_group_with_options(project, machine_group, headers, runtime)

    async def get_machine_group_async(
        self,
        project: str,
        machine_group: str,
    ) -> sls_20201230_models.GetMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_machine_group_with_options_async(project, machine_group, headers, runtime)

    def get_project_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetProjectResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetProjectResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_project(
        self,
        project: str,
    ) -> sls_20201230_models.GetProjectResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project, headers, runtime)

    async def get_project_async(
        self,
        project: str,
    ) -> sls_20201230_models.GetProjectResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(project, headers, runtime)

    def get_project_logs_with_options(
        self,
        project: str,
        request: sls_20201230_models.GetProjectLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetProjectLogsResponse:
        """
        ### Usage notes
        *   You can use the query parameter to specify a standard SQL statement.
        *   You must specify a project in the domain name of the request.
        *   You must specify a Logstore in the FROM clause of the SQL statement. A Logstore can be used as an SQL table.
        *   You must specify a time range in the SQL statement by using the \\__date\\_\\_ parameter or \\__time\\_\\_ parameter. The value of the \\__date\\_\\_ parameter is a timestamp, and the value of the \\__time\\_\\_ parameter is an integer. The unit of the \\__time\\_\\_ parameter is seconds.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetProjectLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectLogsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.power_sql):
            query['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectLogsResponse(),
            self.execute(params, req, runtime)
        )

    async def get_project_logs_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.GetProjectLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetProjectLogsResponse:
        """
        ### Usage notes
        *   You can use the query parameter to specify a standard SQL statement.
        *   You must specify a project in the domain name of the request.
        *   You must specify a Logstore in the FROM clause of the SQL statement. A Logstore can be used as an SQL table.
        *   You must specify a time range in the SQL statement by using the \\__date\\_\\_ parameter or \\__time\\_\\_ parameter. The value of the \\__date\\_\\_ parameter is a timestamp, and the value of the \\__time\\_\\_ parameter is an integer. The unit of the \\__time\\_\\_ parameter is seconds.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetProjectLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectLogsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.power_sql):
            query['powerSql'] = request.power_sql
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectLogs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectLogsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_project_logs(
        self,
        project: str,
        request: sls_20201230_models.GetProjectLogsRequest,
    ) -> sls_20201230_models.GetProjectLogsResponse:
        """
        ### Usage notes
        *   You can use the query parameter to specify a standard SQL statement.
        *   You must specify a project in the domain name of the request.
        *   You must specify a Logstore in the FROM clause of the SQL statement. A Logstore can be used as an SQL table.
        *   You must specify a time range in the SQL statement by using the \\__date\\_\\_ parameter or \\__time\\_\\_ parameter. The value of the \\__date\\_\\_ parameter is a timestamp, and the value of the \\__time\\_\\_ parameter is an integer. The unit of the \\__time\\_\\_ parameter is seconds.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetProjectLogsRequest
        @return: GetProjectLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_logs_with_options(project, request, headers, runtime)

    async def get_project_logs_async(
        self,
        project: str,
        request: sls_20201230_models.GetProjectLogsRequest,
    ) -> sls_20201230_models.GetProjectLogsResponse:
        """
        ### Usage notes
        *   You can use the query parameter to specify a standard SQL statement.
        *   You must specify a project in the domain name of the request.
        *   You must specify a Logstore in the FROM clause of the SQL statement. A Logstore can be used as an SQL table.
        *   You must specify a time range in the SQL statement by using the \\__date\\_\\_ parameter or \\__time\\_\\_ parameter. The value of the \\__date\\_\\_ parameter is a timestamp, and the value of the \\__time\\_\\_ parameter is an integer. The unit of the \\__time\\_\\_ parameter is seconds.
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetProjectLogsRequest
        @return: GetProjectLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_logs_with_options_async(project, request, headers, runtime)

    def get_project_policy_with_options(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetProjectPolicyResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectPolicyResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def get_project_policy_with_options_async(
        self,
        project: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetProjectPolicyResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectPolicyResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetProjectPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_project_policy(
        self,
        project: str,
    ) -> sls_20201230_models.GetProjectPolicyResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetProjectPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_policy_with_options(project, headers, runtime)

    async def get_project_policy_async(
        self,
        project: str,
    ) -> sls_20201230_models.GetProjectPolicyResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetProjectPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_policy_with_options_async(project, headers, runtime)

    def get_saved_search_with_options(
        self,
        project: str,
        savedsearch_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavedSearchResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches/{savedsearch_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def get_saved_search_with_options_async(
        self,
        project: str,
        savedsearch_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavedSearchResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches/{savedsearch_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_saved_search(
        self,
        project: str,
        savedsearch_name: str,
    ) -> sls_20201230_models.GetSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetSavedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_saved_search_with_options(project, savedsearch_name, headers, runtime)

    async def get_saved_search_async(
        self,
        project: str,
        savedsearch_name: str,
    ) -> sls_20201230_models.GetSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: GetSavedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_saved_search_with_options_async(project, savedsearch_name, headers, runtime)

    def get_shipper_status_with_options(
        self,
        project: str,
        logstore: str,
        shipper_name: str,
        request: sls_20201230_models.GetShipperStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetShipperStatusResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetShipperStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetShipperStatusResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetShipperStatus',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shipper/{shipper_name}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetShipperStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_shipper_status_with_options_async(
        self,
        project: str,
        logstore: str,
        shipper_name: str,
        request: sls_20201230_models.GetShipperStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.GetShipperStatusResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetShipperStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetShipperStatusResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetShipperStatus',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shipper/{shipper_name}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.GetShipperStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_shipper_status(
        self,
        project: str,
        logstore: str,
        shipper_name: str,
        request: sls_20201230_models.GetShipperStatusRequest,
    ) -> sls_20201230_models.GetShipperStatusResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetShipperStatusRequest
        @return: GetShipperStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_shipper_status_with_options(project, logstore, shipper_name, request, headers, runtime)

    async def get_shipper_status_async(
        self,
        project: str,
        logstore: str,
        shipper_name: str,
        request: sls_20201230_models.GetShipperStatusRequest,
    ) -> sls_20201230_models.GetShipperStatusResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: GetShipperStatusRequest
        @return: GetShipperStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_shipper_status_with_options_async(project, logstore, shipper_name, request, headers, runtime)

    def list_annotation_data_with_options(
        self,
        dataset_id: str,
        request: sls_20201230_models.ListAnnotationDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListAnnotationDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}/annotationdata',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    async def list_annotation_data_with_options_async(
        self,
        dataset_id: str,
        request: sls_20201230_models.ListAnnotationDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListAnnotationDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}/annotationdata',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAnnotationDataResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_annotation_data(
        self,
        dataset_id: str,
        request: sls_20201230_models.ListAnnotationDataRequest,
    ) -> sls_20201230_models.ListAnnotationDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_annotation_data_with_options(dataset_id, request, headers, runtime)

    async def list_annotation_data_async(
        self,
        dataset_id: str,
        request: sls_20201230_models.ListAnnotationDataRequest,
    ) -> sls_20201230_models.ListAnnotationDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_annotation_data_with_options_async(dataset_id, request, headers, runtime)

    def list_annotation_data_sets_with_options(
        self,
        request: sls_20201230_models.ListAnnotationDataSetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListAnnotationDataSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationDataSets',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAnnotationDataSetsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_annotation_data_sets_with_options_async(
        self,
        request: sls_20201230_models.ListAnnotationDataSetsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListAnnotationDataSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationDataSets',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAnnotationDataSetsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_annotation_data_sets(
        self,
        request: sls_20201230_models.ListAnnotationDataSetsRequest,
    ) -> sls_20201230_models.ListAnnotationDataSetsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_annotation_data_sets_with_options(request, headers, runtime)

    async def list_annotation_data_sets_async(
        self,
        request: sls_20201230_models.ListAnnotationDataSetsRequest,
    ) -> sls_20201230_models.ListAnnotationDataSetsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_annotation_data_sets_with_options_async(request, headers, runtime)

    def list_annotation_labels_with_options(
        self,
        request: sls_20201230_models.ListAnnotationLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListAnnotationLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationLabels',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationlabel',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAnnotationLabelsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_annotation_labels_with_options_async(
        self,
        request: sls_20201230_models.ListAnnotationLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListAnnotationLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnnotationLabels',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationlabel',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListAnnotationLabelsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_annotation_labels(
        self,
        request: sls_20201230_models.ListAnnotationLabelsRequest,
    ) -> sls_20201230_models.ListAnnotationLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_annotation_labels_with_options(request, headers, runtime)

    async def list_annotation_labels_async(
        self,
        request: sls_20201230_models.ListAnnotationLabelsRequest,
    ) -> sls_20201230_models.ListAnnotationLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_annotation_labels_with_options_async(request, headers, runtime)

    def list_collection_policies_with_options(
        self,
        tmp_req: sls_20201230_models.ListCollectionPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListCollectionPoliciesResponse:
        UtilClient.validate_model(tmp_req)
        request = sls_20201230_models.ListCollectionPoliciesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attribute):
            request.attribute_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attribute, 'attribute', 'json')
        query = {}
        if not UtilClient.is_unset(request.attribute_shrink):
            query['attribute'] = request.attribute_shrink
        if not UtilClient.is_unset(request.data_code):
            query['dataCode'] = request.data_code
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_name):
            query['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCollectionPolicies',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/collectionpolicy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListCollectionPoliciesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_collection_policies_with_options_async(
        self,
        tmp_req: sls_20201230_models.ListCollectionPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListCollectionPoliciesResponse:
        UtilClient.validate_model(tmp_req)
        request = sls_20201230_models.ListCollectionPoliciesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attribute):
            request.attribute_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attribute, 'attribute', 'json')
        query = {}
        if not UtilClient.is_unset(request.attribute_shrink):
            query['attribute'] = request.attribute_shrink
        if not UtilClient.is_unset(request.data_code):
            query['dataCode'] = request.data_code
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_name):
            query['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.product_code):
            query['productCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCollectionPolicies',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/collectionpolicy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListCollectionPoliciesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_collection_policies(
        self,
        request: sls_20201230_models.ListCollectionPoliciesRequest,
    ) -> sls_20201230_models.ListCollectionPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_collection_policies_with_options(request, headers, runtime)

    async def list_collection_policies_async(
        self,
        request: sls_20201230_models.ListCollectionPoliciesRequest,
    ) -> sls_20201230_models.ListCollectionPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_collection_policies_with_options_async(request, headers, runtime)

    def list_config_with_options(
        self,
        project: str,
        request: sls_20201230_models.ListConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListConfigResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['configName'] = request.config_name
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def list_config_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.ListConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListConfigResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['configName'] = request.config_name
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_config(
        self,
        project: str,
        request: sls_20201230_models.ListConfigRequest,
    ) -> sls_20201230_models.ListConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_config_with_options(project, request, headers, runtime)

    async def list_config_async(
        self,
        project: str,
        request: sls_20201230_models.ListConfigRequest,
    ) -> sls_20201230_models.ListConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_config_with_options_async(project, request, headers, runtime)

    def list_consumer_group_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListConsumerGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumerGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def list_consumer_group_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListConsumerGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumerGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListConsumerGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_consumer_group(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.ListConsumerGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: ListConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumer_group_with_options(project, logstore, headers, runtime)

    async def list_consumer_group_async(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.ListConsumerGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: ListConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_consumer_group_with_options_async(project, logstore, headers, runtime)

    def list_dashboard_with_options(
        self,
        project: str,
        request: sls_20201230_models.ListDashboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListDashboardResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/dashboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListDashboardResponse(),
            self.execute(params, req, runtime)
        )

    async def list_dashboard_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.ListDashboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListDashboardResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/dashboards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListDashboardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_dashboard(
        self,
        project: str,
        request: sls_20201230_models.ListDashboardRequest,
    ) -> sls_20201230_models.ListDashboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dashboard_with_options(project, request, headers, runtime)

    async def list_dashboard_async(
        self,
        project: str,
        request: sls_20201230_models.ListDashboardRequest,
    ) -> sls_20201230_models.ListDashboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dashboard_with_options_async(project, request, headers, runtime)

    def list_domains_with_options(
        self,
        project: str,
        request: sls_20201230_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListDomainsResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Only one custom domain name can be bound to each project.
        
        @param request: ListDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListDomainsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListDomainsResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Only one custom domain name can be bound to each project.
        
        @param request: ListDomainsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/domains',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListDomainsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_domains(
        self,
        project: str,
        request: sls_20201230_models.ListDomainsRequest,
    ) -> sls_20201230_models.ListDomainsResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Only one custom domain name can be bound to each project.
        
        @param request: ListDomainsRequest
        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_domains_with_options(project, request, headers, runtime)

    async def list_domains_async(
        self,
        project: str,
        request: sls_20201230_models.ListDomainsRequest,
    ) -> sls_20201230_models.ListDomainsResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Only one custom domain name can be bound to each project.
        
        @param request: ListDomainsRequest
        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_domains_with_options_async(project, request, headers, runtime)

    def list_external_store_with_options(
        self,
        project: str,
        request: sls_20201230_models.ListExternalStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListExternalStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.external_store_name):
            query['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.sizs):
            query['sizs'] = request.sizs
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def list_external_store_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.ListExternalStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListExternalStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.external_store_name):
            query['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.sizs):
            query['sizs'] = request.sizs
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListExternalStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_external_store(
        self,
        project: str,
        request: sls_20201230_models.ListExternalStoreRequest,
    ) -> sls_20201230_models.ListExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListExternalStoreRequest
        @return: ListExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_external_store_with_options(project, request, headers, runtime)

    async def list_external_store_async(
        self,
        project: str,
        request: sls_20201230_models.ListExternalStoreRequest,
    ) -> sls_20201230_models.ListExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListExternalStoreRequest
        @return: ListExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_external_store_with_options_async(project, request, headers, runtime)

    def list_log_stores_with_options(
        self,
        project: str,
        request: sls_20201230_models.ListLogStoresRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListLogStoresResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListLogStoresRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogStoresResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.mode):
            query['mode'] = request.mode
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.telemetry_type):
            query['telemetryType'] = request.telemetry_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogStores',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListLogStoresResponse(),
            self.execute(params, req, runtime)
        )

    async def list_log_stores_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.ListLogStoresRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListLogStoresResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListLogStoresRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogStoresResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.mode):
            query['mode'] = request.mode
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.telemetry_type):
            query['telemetryType'] = request.telemetry_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogStores',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListLogStoresResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_log_stores(
        self,
        project: str,
        request: sls_20201230_models.ListLogStoresRequest,
    ) -> sls_20201230_models.ListLogStoresResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListLogStoresRequest
        @return: ListLogStoresResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_log_stores_with_options(project, request, headers, runtime)

    async def list_log_stores_async(
        self,
        project: str,
        request: sls_20201230_models.ListLogStoresRequest,
    ) -> sls_20201230_models.ListLogStoresResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListLogStoresRequest
        @return: ListLogStoresResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_log_stores_with_options_async(project, request, headers, runtime)

    def list_logtail_pipeline_config_with_options(
        self,
        project: str,
        request: sls_20201230_models.ListLogtailPipelineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListLogtailPipelineConfigResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['configName'] = request.config_name
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/pipelineconfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def list_logtail_pipeline_config_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.ListLogtailPipelineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListLogtailPipelineConfigResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['configName'] = request.config_name
        if not UtilClient.is_unset(request.logstore_name):
            query['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/pipelineconfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListLogtailPipelineConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_logtail_pipeline_config(
        self,
        project: str,
        request: sls_20201230_models.ListLogtailPipelineConfigRequest,
    ) -> sls_20201230_models.ListLogtailPipelineConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logtail_pipeline_config_with_options(project, request, headers, runtime)

    async def list_logtail_pipeline_config_async(
        self,
        project: str,
        request: sls_20201230_models.ListLogtailPipelineConfigRequest,
    ) -> sls_20201230_models.ListLogtailPipelineConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_logtail_pipeline_config_with_options_async(project, request, headers, runtime)

    def list_machine_group_with_options(
        self,
        project: str,
        request: sls_20201230_models.ListMachineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListMachineGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMachineGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['groupName'] = request.group_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def list_machine_group_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.ListMachineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListMachineGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMachineGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['groupName'] = request.group_name
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_machine_group(
        self,
        project: str,
        request: sls_20201230_models.ListMachineGroupRequest,
    ) -> sls_20201230_models.ListMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListMachineGroupRequest
        @return: ListMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_machine_group_with_options(project, request, headers, runtime)

    async def list_machine_group_async(
        self,
        project: str,
        request: sls_20201230_models.ListMachineGroupRequest,
    ) -> sls_20201230_models.ListMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListMachineGroupRequest
        @return: ListMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_machine_group_with_options_async(project, request, headers, runtime)

    def list_machines_with_options(
        self,
        project: str,
        machine_group: str,
        request: sls_20201230_models.ListMachinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListMachinesResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListMachinesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMachinesResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMachines',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}/machines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListMachinesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_machines_with_options_async(
        self,
        project: str,
        machine_group: str,
        request: sls_20201230_models.ListMachinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListMachinesResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListMachinesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMachinesResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMachines',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}/machines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListMachinesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_machines(
        self,
        project: str,
        machine_group: str,
        request: sls_20201230_models.ListMachinesRequest,
    ) -> sls_20201230_models.ListMachinesResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListMachinesRequest
        @return: ListMachinesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_machines_with_options(project, machine_group, request, headers, runtime)

    async def list_machines_async(
        self,
        project: str,
        machine_group: str,
        request: sls_20201230_models.ListMachinesRequest,
    ) -> sls_20201230_models.ListMachinesResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListMachinesRequest
        @return: ListMachinesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_machines_with_options_async(project, machine_group, request, headers, runtime)

    def list_project_with_options(
        self,
        request: sls_20201230_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListProjectResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.project_name):
            query['projectName'] = request.project_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def list_project_with_options_async(
        self,
        request: sls_20201230_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListProjectResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.project_name):
            query['projectName'] = request.project_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_project(
        self,
        request: sls_20201230_models.ListProjectRequest,
    ) -> sls_20201230_models.ListProjectResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListProjectRequest
        @return: ListProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_with_options(request, headers, runtime)

    async def list_project_async(
        self,
        request: sls_20201230_models.ListProjectRequest,
    ) -> sls_20201230_models.ListProjectResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListProjectRequest
        @return: ListProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_with_options_async(request, headers, runtime)

    def list_saved_search_with_options(
        self,
        project: str,
        request: sls_20201230_models.ListSavedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListSavedSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSavedSearchResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def list_saved_search_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.ListSavedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListSavedSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSavedSearchResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['offset'] = request.offset
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_saved_search(
        self,
        project: str,
        request: sls_20201230_models.ListSavedSearchRequest,
    ) -> sls_20201230_models.ListSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListSavedSearchRequest
        @return: ListSavedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_saved_search_with_options(project, request, headers, runtime)

    async def list_saved_search_async(
        self,
        project: str,
        request: sls_20201230_models.ListSavedSearchRequest,
    ) -> sls_20201230_models.ListSavedSearchResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListSavedSearchRequest
        @return: ListSavedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_saved_search_with_options_async(project, request, headers, runtime)

    def list_shards_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListShardsResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListShards',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListShardsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_shards_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListShardsResponse:
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListShards',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shards',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListShardsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_shards(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.ListShardsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shards_with_options(project, logstore, headers, runtime)

    async def list_shards_async(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.ListShardsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_shards_with_options_async(project, logstore, headers, runtime)

    def list_shipper_with_options(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListShipperResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListShipperResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListShipper',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shipper',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListShipperResponse(),
            self.execute(params, req, runtime)
        )

    async def list_shipper_with_options_async(
        self,
        project: str,
        logstore: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListShipperResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListShipperResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='ListShipper',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shipper',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListShipperResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_shipper(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.ListShipperResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: ListShipperResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shipper_with_options(project, logstore, headers, runtime)

    async def list_shipper_async(
        self,
        project: str,
        logstore: str,
    ) -> sls_20201230_models.ListShipperResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: ListShipperResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_shipper_with_options_async(project, logstore, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: sls_20201230_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListTagResourcesResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param tmp_req: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sls_20201230_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListTagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: sls_20201230_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.ListTagResourcesResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param tmp_req: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = sls_20201230_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.ListTagResourcesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: sls_20201230_models.ListTagResourcesRequest,
    ) -> sls_20201230_models.ListTagResourcesResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: sls_20201230_models.ListTagResourcesRequest,
    ) -> sls_20201230_models.ListTagResourcesResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def put_annotation_data_with_options(
        self,
        dataset_id: str,
        request: sls_20201230_models.PutAnnotationDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.PutAnnotationDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotationdata_id):
            query['annotationdataId'] = request.annotationdata_id
        body = {}
        if not UtilClient.is_unset(request.ml_data_param):
            body['mlDataParam'] = request.ml_data_param
        if not UtilClient.is_unset(request.raw_log):
            body['rawLog'] = request.raw_log
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}/annotationdata',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutAnnotationDataResponse(),
            self.execute(params, req, runtime)
        )

    async def put_annotation_data_with_options_async(
        self,
        dataset_id: str,
        request: sls_20201230_models.PutAnnotationDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.PutAnnotationDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotationdata_id):
            query['annotationdataId'] = request.annotationdata_id
        body = {}
        if not UtilClient.is_unset(request.ml_data_param):
            body['mlDataParam'] = request.ml_data_param
        if not UtilClient.is_unset(request.raw_log):
            body['rawLog'] = request.raw_log
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutAnnotationData',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}/annotationdata',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutAnnotationDataResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_annotation_data(
        self,
        dataset_id: str,
        request: sls_20201230_models.PutAnnotationDataRequest,
    ) -> sls_20201230_models.PutAnnotationDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_annotation_data_with_options(dataset_id, request, headers, runtime)

    async def put_annotation_data_async(
        self,
        dataset_id: str,
        request: sls_20201230_models.PutAnnotationDataRequest,
    ) -> sls_20201230_models.PutAnnotationDataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_annotation_data_with_options_async(dataset_id, request, headers, runtime)

    def put_project_policy_with_options(
        self,
        project: str,
        request: sls_20201230_models.PutProjectPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.PutProjectPolicyResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Alibaba Cloud Simple Log Service allows you to configure a project policy to authorize other users to access the specified Log Service resources.
        *   You must configure a project policy based on policy syntax. Before you configure a project policy, you must be familiar with the Action, Resource, and Condition parameters. For more information, see [RAM](~~128139~~).
        *   If you set the Principal element to an asterisk (\\*) and do not configure the Condition element when you configure a project policy, the policy applies to all users except for the project owner. If you set the Principal element to an asterisk (\\*) and configure the Condition element when you configure a project policy, the policy applies to all users including the project owner.
        *   You can configure multiple project policies for a project. The total size of the policies cannot exceed 16 KB.
        
        @param request: PutProjectPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutProjectPolicyResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='PutProjectPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/policy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutProjectPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def put_project_policy_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.PutProjectPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.PutProjectPolicyResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Alibaba Cloud Simple Log Service allows you to configure a project policy to authorize other users to access the specified Log Service resources.
        *   You must configure a project policy based on policy syntax. Before you configure a project policy, you must be familiar with the Action, Resource, and Condition parameters. For more information, see [RAM](~~128139~~).
        *   If you set the Principal element to an asterisk (\\*) and do not configure the Condition element when you configure a project policy, the policy applies to all users except for the project owner. If you set the Principal element to an asterisk (\\*) and configure the Condition element when you configure a project policy, the policy applies to all users including the project owner.
        *   You can configure multiple project policies for a project. The total size of the policies cannot exceed 16 KB.
        
        @param request: PutProjectPolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutProjectPolicyResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='PutProjectPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/policy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutProjectPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_project_policy(
        self,
        project: str,
        request: sls_20201230_models.PutProjectPolicyRequest,
    ) -> sls_20201230_models.PutProjectPolicyResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Alibaba Cloud Simple Log Service allows you to configure a project policy to authorize other users to access the specified Log Service resources.
        *   You must configure a project policy based on policy syntax. Before you configure a project policy, you must be familiar with the Action, Resource, and Condition parameters. For more information, see [RAM](~~128139~~).
        *   If you set the Principal element to an asterisk (\\*) and do not configure the Condition element when you configure a project policy, the policy applies to all users except for the project owner. If you set the Principal element to an asterisk (\\*) and configure the Condition element when you configure a project policy, the policy applies to all users including the project owner.
        *   You can configure multiple project policies for a project. The total size of the policies cannot exceed 16 KB.
        
        @param request: PutProjectPolicyRequest
        @return: PutProjectPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_project_policy_with_options(project, request, headers, runtime)

    async def put_project_policy_async(
        self,
        project: str,
        request: sls_20201230_models.PutProjectPolicyRequest,
    ) -> sls_20201230_models.PutProjectPolicyResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Alibaba Cloud Simple Log Service allows you to configure a project policy to authorize other users to access the specified Log Service resources.
        *   You must configure a project policy based on policy syntax. Before you configure a project policy, you must be familiar with the Action, Resource, and Condition parameters. For more information, see [RAM](~~128139~~).
        *   If you set the Principal element to an asterisk (\\*) and do not configure the Condition element when you configure a project policy, the policy applies to all users except for the project owner. If you set the Principal element to an asterisk (\\*) and configure the Condition element when you configure a project policy, the policy applies to all users including the project owner.
        *   You can configure multiple project policies for a project. The total size of the policies cannot exceed 16 KB.
        
        @param request: PutProjectPolicyRequest
        @return: PutProjectPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_project_policy_with_options_async(project, request, headers, runtime)

    def put_project_transfer_acceleration_with_options(
        self,
        project: str,
        request: sls_20201230_models.PutProjectTransferAccelerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.PutProjectTransferAccelerationResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.enabled):
            body['enabled'] = request.enabled
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutProjectTransferAcceleration',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/transferacceleration',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutProjectTransferAccelerationResponse(),
            self.execute(params, req, runtime)
        )

    async def put_project_transfer_acceleration_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.PutProjectTransferAccelerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.PutProjectTransferAccelerationResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.enabled):
            body['enabled'] = request.enabled
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutProjectTransferAcceleration',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/transferacceleration',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutProjectTransferAccelerationResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_project_transfer_acceleration(
        self,
        project: str,
        request: sls_20201230_models.PutProjectTransferAccelerationRequest,
    ) -> sls_20201230_models.PutProjectTransferAccelerationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_project_transfer_acceleration_with_options(project, request, headers, runtime)

    async def put_project_transfer_acceleration_async(
        self,
        project: str,
        request: sls_20201230_models.PutProjectTransferAccelerationRequest,
    ) -> sls_20201230_models.PutProjectTransferAccelerationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_project_transfer_acceleration_with_options_async(project, request, headers, runtime)

    def put_webtracking_with_options(
        self,
        project: str,
        logstore_name: str,
        request: sls_20201230_models.PutWebtrackingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.PutWebtrackingResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.logs):
            body['__logs__'] = request.logs
        if not UtilClient.is_unset(request.source):
            body['__source__'] = request.source
        if not UtilClient.is_unset(request.tags):
            body['__tags__'] = request.tags
        if not UtilClient.is_unset(request.topic):
            body['__topic__'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutWebtracking',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore_name}/track',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutWebtrackingResponse(),
            self.execute(params, req, runtime)
        )

    async def put_webtracking_with_options_async(
        self,
        project: str,
        logstore_name: str,
        request: sls_20201230_models.PutWebtrackingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.PutWebtrackingResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.logs):
            body['__logs__'] = request.logs
        if not UtilClient.is_unset(request.source):
            body['__source__'] = request.source
        if not UtilClient.is_unset(request.tags):
            body['__tags__'] = request.tags
        if not UtilClient.is_unset(request.topic):
            body['__topic__'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutWebtracking',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore_name}/track',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.PutWebtrackingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def put_webtracking(
        self,
        project: str,
        logstore_name: str,
        request: sls_20201230_models.PutWebtrackingRequest,
    ) -> sls_20201230_models.PutWebtrackingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_webtracking_with_options(project, logstore_name, request, headers, runtime)

    async def put_webtracking_async(
        self,
        project: str,
        logstore_name: str,
        request: sls_20201230_models.PutWebtrackingRequest,
    ) -> sls_20201230_models.PutWebtrackingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_webtracking_with_options_async(project, logstore_name, request, headers, runtime)

    def query_mlservice_results_with_options(
        self,
        service_name: str,
        request: sls_20201230_models.QueryMLServiceResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.QueryMLServiceResultsResponse:
        """
        @deprecated
        
        @param request: QueryMLServiceResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMLServiceResultsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_builtin):
            query['allowBuiltin'] = request.allow_builtin
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryMLServiceResults',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/service/{service_name}/analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.QueryMLServiceResultsResponse(),
            self.execute(params, req, runtime)
        )

    async def query_mlservice_results_with_options_async(
        self,
        service_name: str,
        request: sls_20201230_models.QueryMLServiceResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.QueryMLServiceResultsResponse:
        """
        @deprecated
        
        @param request: QueryMLServiceResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMLServiceResultsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_builtin):
            query['allowBuiltin'] = request.allow_builtin
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryMLServiceResults',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/service/{service_name}/analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.QueryMLServiceResultsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def query_mlservice_results(
        self,
        service_name: str,
        request: sls_20201230_models.QueryMLServiceResultsRequest,
    ) -> sls_20201230_models.QueryMLServiceResultsResponse:
        """
        @deprecated
        
        @param request: QueryMLServiceResultsRequest
        @return: QueryMLServiceResultsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_mlservice_results_with_options(service_name, request, headers, runtime)

    async def query_mlservice_results_async(
        self,
        service_name: str,
        request: sls_20201230_models.QueryMLServiceResultsRequest,
    ) -> sls_20201230_models.QueryMLServiceResultsResponse:
        """
        @deprecated
        
        @param request: QueryMLServiceResultsRequest
        @return: QueryMLServiceResultsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_mlservice_results_with_options_async(service_name, request, headers, runtime)

    def remove_config_from_machine_group_with_options(
        self,
        project: str,
        machine_group: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.RemoveConfigFromMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveConfigFromMachineGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveConfigFromMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}/configs/{config_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.RemoveConfigFromMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def remove_config_from_machine_group_with_options_async(
        self,
        project: str,
        machine_group: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.RemoveConfigFromMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveConfigFromMachineGroupResponse
        """
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveConfigFromMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}/configs/{config_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.RemoveConfigFromMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def remove_config_from_machine_group(
        self,
        project: str,
        machine_group: str,
        config_name: str,
    ) -> sls_20201230_models.RemoveConfigFromMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: RemoveConfigFromMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_config_from_machine_group_with_options(project, machine_group, config_name, headers, runtime)

    async def remove_config_from_machine_group_async(
        self,
        project: str,
        machine_group: str,
        config_name: str,
    ) -> sls_20201230_models.RemoveConfigFromMachineGroupResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @return: RemoveConfigFromMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_config_from_machine_group_with_options_async(project, machine_group, config_name, headers, runtime)

    def split_shard_with_options(
        self,
        project: str,
        logstore: str,
        shard: str,
        request: sls_20201230_models.SplitShardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.SplitShardResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Each shard has an MD5 hash range, and each range is a left-closed, right-open interval. The interval is in the `[BeginKey,EndKey)` format. A shard can be in the readwrite or readonly state. You can split a shard and merge shards. For more information, see [Shard](~~28976~~).
        
        @param request: SplitShardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SplitShardResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.shard_count):
            query['shardCount'] = request.shard_count
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SplitShard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shards/{shard}?action=split',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.SplitShardResponse(),
            self.execute(params, req, runtime)
        )

    async def split_shard_with_options_async(
        self,
        project: str,
        logstore: str,
        shard: str,
        request: sls_20201230_models.SplitShardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.SplitShardResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Each shard has an MD5 hash range, and each range is a left-closed, right-open interval. The interval is in the `[BeginKey,EndKey)` format. A shard can be in the readwrite or readonly state. You can split a shard and merge shards. For more information, see [Shard](~~28976~~).
        
        @param request: SplitShardRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SplitShardResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        if not UtilClient.is_unset(request.shard_count):
            query['shardCount'] = request.shard_count
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SplitShard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/shards/{shard}?action=split',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            sls_20201230_models.SplitShardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def split_shard(
        self,
        project: str,
        logstore: str,
        shard: str,
        request: sls_20201230_models.SplitShardRequest,
    ) -> sls_20201230_models.SplitShardResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Each shard has an MD5 hash range, and each range is a left-closed, right-open interval. The interval is in the `[BeginKey,EndKey)` format. A shard can be in the readwrite or readonly state. You can split a shard and merge shards. For more information, see [Shard](~~28976~~).
        
        @param request: SplitShardRequest
        @return: SplitShardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.split_shard_with_options(project, logstore, shard, request, headers, runtime)

    async def split_shard_async(
        self,
        project: str,
        logstore: str,
        shard: str,
        request: sls_20201230_models.SplitShardRequest,
    ) -> sls_20201230_models.SplitShardResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        *   Each shard has an MD5 hash range, and each range is a left-closed, right-open interval. The interval is in the `[BeginKey,EndKey)` format. A shard can be in the readwrite or readonly state. You can split a shard and merge shards. For more information, see [Shard](~~28976~~).
        
        @param request: SplitShardRequest
        @return: SplitShardResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.split_shard_with_options_async(project, logstore, shard, request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: sls_20201230_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.TagResourcesResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/tag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.TagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: sls_20201230_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.TagResourcesResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/tag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.TagResourcesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: sls_20201230_models.TagResourcesRequest,
    ) -> sls_20201230_models.TagResourcesResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: sls_20201230_models.TagResourcesRequest,
    ) -> sls_20201230_models.TagResourcesResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        request: sls_20201230_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UntagResourcesResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['all'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/untag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UntagResourcesResponse(),
            self.execute(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: sls_20201230_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UntagResourcesResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['all'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/untag',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UntagResourcesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: sls_20201230_models.UntagResourcesRequest,
    ) -> sls_20201230_models.UntagResourcesResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: sls_20201230_models.UntagResourcesRequest,
    ) -> sls_20201230_models.UntagResourcesResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_annotation_data_set_with_options(
        self,
        dataset_id: str,
        request: sls_20201230_models.UpdateAnnotationDataSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateAnnotationDataSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateAnnotationDataSetResponse(),
            self.execute(params, req, runtime)
        )

    async def update_annotation_data_set_with_options_async(
        self,
        dataset_id: str,
        request: sls_20201230_models.UpdateAnnotationDataSetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateAnnotationDataSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAnnotationDataSet',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationdataset/{dataset_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateAnnotationDataSetResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_annotation_data_set(
        self,
        dataset_id: str,
        request: sls_20201230_models.UpdateAnnotationDataSetRequest,
    ) -> sls_20201230_models.UpdateAnnotationDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_annotation_data_set_with_options(dataset_id, request, headers, runtime)

    async def update_annotation_data_set_async(
        self,
        dataset_id: str,
        request: sls_20201230_models.UpdateAnnotationDataSetRequest,
    ) -> sls_20201230_models.UpdateAnnotationDataSetResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_annotation_data_set_with_options_async(dataset_id, request, headers, runtime)

    def update_annotation_label_with_options(
        self,
        request: sls_20201230_models.UpdateAnnotationLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateAnnotationLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationlabel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateAnnotationLabelResponse(),
            self.execute(params, req, runtime)
        )

    async def update_annotation_label_with_options_async(
        self,
        request: sls_20201230_models.UpdateAnnotationLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateAnnotationLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateAnnotationLabel',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/ml/annotationlabel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateAnnotationLabelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_annotation_label(
        self,
        request: sls_20201230_models.UpdateAnnotationLabelRequest,
    ) -> sls_20201230_models.UpdateAnnotationLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_annotation_label_with_options(request, headers, runtime)

    async def update_annotation_label_async(
        self,
        request: sls_20201230_models.UpdateAnnotationLabelRequest,
    ) -> sls_20201230_models.UpdateAnnotationLabelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_annotation_label_with_options_async(request, headers, runtime)

    def update_config_with_options(
        self,
        project: str,
        config_name: str,
        request: sls_20201230_models.UpdateConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateConfigResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/configs/{config_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def update_config_with_options_async(
        self,
        project: str,
        config_name: str,
        request: sls_20201230_models.UpdateConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateConfigResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/configs/{config_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_config(
        self,
        project: str,
        config_name: str,
        request: sls_20201230_models.UpdateConfigRequest,
    ) -> sls_20201230_models.UpdateConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_config_with_options(project, config_name, request, headers, runtime)

    async def update_config_async(
        self,
        project: str,
        config_name: str,
        request: sls_20201230_models.UpdateConfigRequest,
    ) -> sls_20201230_models.UpdateConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_config_with_options_async(project, config_name, request, headers, runtime)

    def update_consumer_group_with_options(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.UpdateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateConsumerGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateConsumerGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateConsumerGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def update_consumer_group_with_options_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.UpdateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateConsumerGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateConsumerGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConsumerGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        if not UtilClient.is_unset(request.timeout):
            body['timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConsumerGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/consumergroups/{consumer_group}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateConsumerGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_consumer_group(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.UpdateConsumerGroupRequest,
    ) -> sls_20201230_models.UpdateConsumerGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateConsumerGroupRequest
        @return: UpdateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_consumer_group_with_options(project, logstore, consumer_group, request, headers, runtime)

    async def update_consumer_group_async(
        self,
        project: str,
        logstore: str,
        consumer_group: str,
        request: sls_20201230_models.UpdateConsumerGroupRequest,
    ) -> sls_20201230_models.UpdateConsumerGroupResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateConsumerGroupRequest
        @return: UpdateConsumerGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_consumer_group_with_options_async(project, logstore, consumer_group, request, headers, runtime)

    def update_dashboard_with_options(
        self,
        project: str,
        dashboard_name: str,
        request: sls_20201230_models.UpdateDashboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateDashboardResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.attribute):
            body['attribute'] = request.attribute
        if not UtilClient.is_unset(request.charts):
            body['charts'] = request.charts
        if not UtilClient.is_unset(request.dashboard_name):
            body['dashboardName'] = request.dashboard_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/dashboards/{dashboard_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateDashboardResponse(),
            self.execute(params, req, runtime)
        )

    async def update_dashboard_with_options_async(
        self,
        project: str,
        dashboard_name: str,
        request: sls_20201230_models.UpdateDashboardRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateDashboardResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.attribute):
            body['attribute'] = request.attribute
        if not UtilClient.is_unset(request.charts):
            body['charts'] = request.charts
        if not UtilClient.is_unset(request.dashboard_name):
            body['dashboardName'] = request.dashboard_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDashboard',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/dashboards/{dashboard_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateDashboardResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_dashboard(
        self,
        project: str,
        dashboard_name: str,
        request: sls_20201230_models.UpdateDashboardRequest,
    ) -> sls_20201230_models.UpdateDashboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_dashboard_with_options(project, dashboard_name, request, headers, runtime)

    async def update_dashboard_async(
        self,
        project: str,
        dashboard_name: str,
        request: sls_20201230_models.UpdateDashboardRequest,
    ) -> sls_20201230_models.UpdateDashboardResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_dashboard_with_options_async(project, dashboard_name, request, headers, runtime)

    def update_index_with_options(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateIndexResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIndexResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.log_reduce):
            body['log_reduce'] = request.log_reduce
        if not UtilClient.is_unset(request.log_reduce_black_list):
            body['log_reduce_black_list'] = request.log_reduce_black_list
        if not UtilClient.is_unset(request.log_reduce_white_list):
            body['log_reduce_white_list'] = request.log_reduce_white_list
        if not UtilClient.is_unset(request.max_text_len):
            body['max_text_len'] = request.max_text_len
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/index',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateIndexResponse(),
            self.execute(params, req, runtime)
        )

    async def update_index_with_options_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateIndexResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIndexResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.line):
            body['line'] = request.line
        if not UtilClient.is_unset(request.log_reduce):
            body['log_reduce'] = request.log_reduce
        if not UtilClient.is_unset(request.log_reduce_black_list):
            body['log_reduce_black_list'] = request.log_reduce_black_list
        if not UtilClient.is_unset(request.log_reduce_white_list):
            body['log_reduce_white_list'] = request.log_reduce_white_list
        if not UtilClient.is_unset(request.max_text_len):
            body['max_text_len'] = request.max_text_len
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIndex',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/index',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateIndexResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_index(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateIndexRequest,
    ) -> sls_20201230_models.UpdateIndexResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateIndexRequest
        @return: UpdateIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_index_with_options(project, logstore, request, headers, runtime)

    async def update_index_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateIndexRequest,
    ) -> sls_20201230_models.UpdateIndexResponse:
        """
        ### Usage notes
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateIndexRequest
        @return: UpdateIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_index_with_options_async(project, logstore, request, headers, runtime)

    def update_log_store_with_options(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateLogStoreResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        *   You can call the UpdateLogStore operation to change only the time-to-live (TTL) attribute.
        
        @param request: UpdateLogStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLogStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not UtilClient.is_unset(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not UtilClient.is_unset(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def update_log_store_with_options_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateLogStoreResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        *   You can call the UpdateLogStore operation to change only the time-to-live (TTL) attribute.
        
        @param request: UpdateLogStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLogStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.append_meta):
            body['appendMeta'] = request.append_meta
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.enable_tracking):
            body['enable_tracking'] = request.enable_tracking
        if not UtilClient.is_unset(request.encrypt_conf):
            body['encrypt_conf'] = request.encrypt_conf
        if not UtilClient.is_unset(request.hot_ttl):
            body['hot_ttl'] = request.hot_ttl
        if not UtilClient.is_unset(request.infrequent_access_ttl):
            body['infrequentAccessTTL'] = request.infrequent_access_ttl
        if not UtilClient.is_unset(request.logstore_name):
            body['logstoreName'] = request.logstore_name
        if not UtilClient.is_unset(request.max_split_shard):
            body['maxSplitShard'] = request.max_split_shard
        if not UtilClient.is_unset(request.mode):
            body['mode'] = request.mode
        if not UtilClient.is_unset(request.shard_count):
            body['shardCount'] = request.shard_count
        if not UtilClient.is_unset(request.telemetry_type):
            body['telemetryType'] = request.telemetry_type
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_log_store(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateLogStoreRequest,
    ) -> sls_20201230_models.UpdateLogStoreResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        *   You can call the UpdateLogStore operation to change only the time-to-live (TTL) attribute.
        
        @param request: UpdateLogStoreRequest
        @return: UpdateLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_log_store_with_options(project, logstore, request, headers, runtime)

    async def update_log_store_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateLogStoreRequest,
    ) -> sls_20201230_models.UpdateLogStoreResponse:
        """
        ### Usage notes
        *   Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        *   You can call the UpdateLogStore operation to change only the time-to-live (TTL) attribute.
        
        @param request: UpdateLogStoreRequest
        @return: UpdateLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_log_store_with_options_async(project, logstore, request, headers, runtime)

    def update_log_store_metering_mode_with_options(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateLogStoreMeteringModeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateLogStoreMeteringModeResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.metering_mode):
            body['meteringMode'] = request.metering_mode
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogStoreMeteringMode',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/meteringmode',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogStoreMeteringModeResponse(),
            self.execute(params, req, runtime)
        )

    async def update_log_store_metering_mode_with_options_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateLogStoreMeteringModeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateLogStoreMeteringModeResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.metering_mode):
            body['meteringMode'] = request.metering_mode
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogStoreMeteringMode',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logstores/{logstore}/meteringmode',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogStoreMeteringModeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_log_store_metering_mode(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateLogStoreMeteringModeRequest,
    ) -> sls_20201230_models.UpdateLogStoreMeteringModeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_log_store_metering_mode_with_options(project, logstore, request, headers, runtime)

    async def update_log_store_metering_mode_async(
        self,
        project: str,
        logstore: str,
        request: sls_20201230_models.UpdateLogStoreMeteringModeRequest,
    ) -> sls_20201230_models.UpdateLogStoreMeteringModeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_log_store_metering_mode_with_options_async(project, logstore, request, headers, runtime)

    def update_logging_with_options(
        self,
        project: str,
        request: sls_20201230_models.UpdateLoggingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateLoggingResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateLoggingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoggingResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.logging_details):
            body['loggingDetails'] = request.logging_details
        if not UtilClient.is_unset(request.logging_project):
            body['loggingProject'] = request.logging_project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logging',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLoggingResponse(),
            self.execute(params, req, runtime)
        )

    async def update_logging_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.UpdateLoggingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateLoggingResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateLoggingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLoggingResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.logging_details):
            body['loggingDetails'] = request.logging_details
        if not UtilClient.is_unset(request.logging_project):
            body['loggingProject'] = request.logging_project
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogging',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/logging',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLoggingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_logging(
        self,
        project: str,
        request: sls_20201230_models.UpdateLoggingRequest,
    ) -> sls_20201230_models.UpdateLoggingResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateLoggingRequest
        @return: UpdateLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logging_with_options(project, request, headers, runtime)

    async def update_logging_async(
        self,
        project: str,
        request: sls_20201230_models.UpdateLoggingRequest,
    ) -> sls_20201230_models.UpdateLoggingResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateLoggingRequest
        @return: UpdateLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_logging_with_options_async(project, request, headers, runtime)

    def update_logtail_pipeline_config_with_options(
        self,
        project: str,
        config_name: str,
        request: sls_20201230_models.UpdateLogtailPipelineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateLogtailPipelineConfigResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.aggregators):
            body['aggregators'] = request.aggregators
        if not UtilClient.is_unset(request.config_name):
            body['configName'] = request.config_name
        if not UtilClient.is_unset(request.flushers):
            body['flushers'] = request.flushers
        if not UtilClient.is_unset(request.global_):
            body['global'] = request.global_
        if not UtilClient.is_unset(request.inputs):
            body['inputs'] = request.inputs
        if not UtilClient.is_unset(request.log_sample):
            body['logSample'] = request.log_sample
        if not UtilClient.is_unset(request.processors):
            body['processors'] = request.processors
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/pipelineconfigs/{config_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogtailPipelineConfigResponse(),
            self.execute(params, req, runtime)
        )

    async def update_logtail_pipeline_config_with_options_async(
        self,
        project: str,
        config_name: str,
        request: sls_20201230_models.UpdateLogtailPipelineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateLogtailPipelineConfigResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.aggregators):
            body['aggregators'] = request.aggregators
        if not UtilClient.is_unset(request.config_name):
            body['configName'] = request.config_name
        if not UtilClient.is_unset(request.flushers):
            body['flushers'] = request.flushers
        if not UtilClient.is_unset(request.global_):
            body['global'] = request.global_
        if not UtilClient.is_unset(request.inputs):
            body['inputs'] = request.inputs
        if not UtilClient.is_unset(request.log_sample):
            body['logSample'] = request.log_sample
        if not UtilClient.is_unset(request.processors):
            body['processors'] = request.processors
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLogtailPipelineConfig',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/pipelineconfigs/{config_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateLogtailPipelineConfigResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_logtail_pipeline_config(
        self,
        project: str,
        config_name: str,
        request: sls_20201230_models.UpdateLogtailPipelineConfigRequest,
    ) -> sls_20201230_models.UpdateLogtailPipelineConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_logtail_pipeline_config_with_options(project, config_name, request, headers, runtime)

    async def update_logtail_pipeline_config_async(
        self,
        project: str,
        config_name: str,
        request: sls_20201230_models.UpdateLogtailPipelineConfigRequest,
    ) -> sls_20201230_models.UpdateLogtailPipelineConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_logtail_pipeline_config_with_options_async(project, config_name, request, headers, runtime)

    def update_machine_group_with_options(
        self,
        project: str,
        group_name: str,
        request: sls_20201230_models.UpdateMachineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateMachineGroupResponse:
        """
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateMachineGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMachineGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.group_attribute):
            body['groupAttribute'] = request.group_attribute
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            body['groupType'] = request.group_type
        if not UtilClient.is_unset(request.machine_identify_type):
            body['machineIdentifyType'] = request.machine_identify_type
        if not UtilClient.is_unset(request.machine_list):
            body['machineList'] = request.machine_list
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{group_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateMachineGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def update_machine_group_with_options_async(
        self,
        project: str,
        group_name: str,
        request: sls_20201230_models.UpdateMachineGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateMachineGroupResponse:
        """
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateMachineGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMachineGroupResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.group_attribute):
            body['groupAttribute'] = request.group_attribute
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            body['groupType'] = request.group_type
        if not UtilClient.is_unset(request.machine_identify_type):
            body['machineIdentifyType'] = request.machine_identify_type
        if not UtilClient.is_unset(request.machine_list):
            body['machineList'] = request.machine_list
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMachineGroup',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{group_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateMachineGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_machine_group(
        self,
        project: str,
        group_name: str,
        request: sls_20201230_models.UpdateMachineGroupRequest,
    ) -> sls_20201230_models.UpdateMachineGroupResponse:
        """
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateMachineGroupRequest
        @return: UpdateMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_machine_group_with_options(project, group_name, request, headers, runtime)

    async def update_machine_group_async(
        self,
        project: str,
        group_name: str,
        request: sls_20201230_models.UpdateMachineGroupRequest,
    ) -> sls_20201230_models.UpdateMachineGroupResponse:
        """
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateMachineGroupRequest
        @return: UpdateMachineGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_machine_group_with_options_async(project, group_name, request, headers, runtime)

    def update_machine_group_machine_with_options(
        self,
        project: str,
        machine_group: str,
        request: sls_20201230_models.UpdateMachineGroupMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateMachineGroupMachineResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateMachineGroupMachineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMachineGroupMachineResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateMachineGroupMachine',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}/machines',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateMachineGroupMachineResponse(),
            self.execute(params, req, runtime)
        )

    async def update_machine_group_machine_with_options_async(
        self,
        project: str,
        machine_group: str,
        request: sls_20201230_models.UpdateMachineGroupMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateMachineGroupMachineResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateMachineGroupMachineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMachineGroupMachineResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        query = {}
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateMachineGroupMachine',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/machinegroups/{machine_group}/machines',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateMachineGroupMachineResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_machine_group_machine(
        self,
        project: str,
        machine_group: str,
        request: sls_20201230_models.UpdateMachineGroupMachineRequest,
    ) -> sls_20201230_models.UpdateMachineGroupMachineResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateMachineGroupMachineRequest
        @return: UpdateMachineGroupMachineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_machine_group_machine_with_options(project, machine_group, request, headers, runtime)

    async def update_machine_group_machine_async(
        self,
        project: str,
        machine_group: str,
        request: sls_20201230_models.UpdateMachineGroupMachineRequest,
    ) -> sls_20201230_models.UpdateMachineGroupMachineResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateMachineGroupMachineRequest
        @return: UpdateMachineGroupMachineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_machine_group_machine_with_options_async(project, machine_group, request, headers, runtime)

    def update_oss_external_store_with_options(
        self,
        project: str,
        external_store_name: str,
        request: sls_20201230_models.UpdateOssExternalStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateOssExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateOssExternalStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOssExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOssExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores/{external_store_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateOssExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def update_oss_external_store_with_options_async(
        self,
        project: str,
        external_store_name: str,
        request: sls_20201230_models.UpdateOssExternalStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateOssExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateOssExternalStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOssExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOssExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores/{external_store_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateOssExternalStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_oss_external_store(
        self,
        project: str,
        external_store_name: str,
        request: sls_20201230_models.UpdateOssExternalStoreRequest,
    ) -> sls_20201230_models.UpdateOssExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateOssExternalStoreRequest
        @return: UpdateOssExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_oss_external_store_with_options(project, external_store_name, request, headers, runtime)

    async def update_oss_external_store_async(
        self,
        project: str,
        external_store_name: str,
        request: sls_20201230_models.UpdateOssExternalStoreRequest,
    ) -> sls_20201230_models.UpdateOssExternalStoreResponse:
        """
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateOssExternalStoreRequest
        @return: UpdateOssExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_oss_external_store_with_options_async(project, external_store_name, request, headers, runtime)

    def update_project_with_options(
        self,
        project: str,
        request: sls_20201230_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateProjectResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateProjectResponse(),
            self.execute(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        project: str,
        request: sls_20201230_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateProjectResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateProjectResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_project(
        self,
        project: str,
        request: sls_20201230_models.UpdateProjectRequest,
    ) -> sls_20201230_models.UpdateProjectResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(project, request, headers, runtime)

    async def update_project_async(
        self,
        project: str,
        request: sls_20201230_models.UpdateProjectRequest,
    ) -> sls_20201230_models.UpdateProjectResponse:
        """
        ### Usage notes
        Host consists of a project name and a Simple Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(project, request, headers, runtime)

    def update_rds_external_store_with_options(
        self,
        project: str,
        external_store_name: str,
        request: sls_20201230_models.UpdateRdsExternalStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateRdsExternalStoreResponse:
        """
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateRdsExternalStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRdsExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRdsExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores/{external_store_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateRdsExternalStoreResponse(),
            self.execute(params, req, runtime)
        )

    async def update_rds_external_store_with_options_async(
        self,
        project: str,
        external_store_name: str,
        request: sls_20201230_models.UpdateRdsExternalStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateRdsExternalStoreResponse:
        """
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateRdsExternalStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRdsExternalStoreResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.external_store_name):
            body['externalStoreName'] = request.external_store_name
        if not UtilClient.is_unset(request.parameter):
            body['parameter'] = request.parameter
        if not UtilClient.is_unset(request.store_type):
            body['storeType'] = request.store_type
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRdsExternalStore',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/externalstores/{external_store_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateRdsExternalStoreResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_rds_external_store(
        self,
        project: str,
        external_store_name: str,
        request: sls_20201230_models.UpdateRdsExternalStoreRequest,
    ) -> sls_20201230_models.UpdateRdsExternalStoreResponse:
        """
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateRdsExternalStoreRequest
        @return: UpdateRdsExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_rds_external_store_with_options(project, external_store_name, request, headers, runtime)

    async def update_rds_external_store_async(
        self,
        project: str,
        external_store_name: str,
        request: sls_20201230_models.UpdateRdsExternalStoreRequest,
    ) -> sls_20201230_models.UpdateRdsExternalStoreResponse:
        """
        Host consists of a project name and a Log Service endpoint. You must specify a project in Host.
        
        @param request: UpdateRdsExternalStoreRequest
        @return: UpdateRdsExternalStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_rds_external_store_with_options_async(project, external_store_name, request, headers, runtime)

    def update_saved_search_with_options(
        self,
        project: str,
        savedsearch_name: str,
        request: sls_20201230_models.UpdateSavedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateSavedSearchResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.logstore):
            body['logstore'] = request.logstore
        if not UtilClient.is_unset(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches/{savedsearch_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateSavedSearchResponse(),
            self.execute(params, req, runtime)
        )

    async def update_saved_search_with_options_async(
        self,
        project: str,
        savedsearch_name: str,
        request: sls_20201230_models.UpdateSavedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpdateSavedSearchResponse:
        UtilClient.validate_model(request)
        host_map = {}
        host_map['project'] = project
        body = {}
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.logstore):
            body['logstore'] = request.logstore
        if not UtilClient.is_unset(request.savedsearch_name):
            body['savedsearchName'] = request.savedsearch_name
        if not UtilClient.is_unset(request.search_query):
            body['searchQuery'] = request.search_query
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSavedSearch',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/savedsearches/{savedsearch_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpdateSavedSearchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_saved_search(
        self,
        project: str,
        savedsearch_name: str,
        request: sls_20201230_models.UpdateSavedSearchRequest,
    ) -> sls_20201230_models.UpdateSavedSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_saved_search_with_options(project, savedsearch_name, request, headers, runtime)

    async def update_saved_search_async(
        self,
        project: str,
        savedsearch_name: str,
        request: sls_20201230_models.UpdateSavedSearchRequest,
    ) -> sls_20201230_models.UpdateSavedSearchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_saved_search_with_options_async(project, savedsearch_name, request, headers, runtime)

    def upsert_collection_policy_with_options(
        self,
        request: sls_20201230_models.UpsertCollectionPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpsertCollectionPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attribute):
            body['attribute'] = request.attribute
        if not UtilClient.is_unset(request.centralize_config):
            body['centralizeConfig'] = request.centralize_config
        if not UtilClient.is_unset(request.centralize_enabled):
            body['centralizeEnabled'] = request.centralize_enabled
        if not UtilClient.is_unset(request.data_code):
            body['dataCode'] = request.data_code
        if not UtilClient.is_unset(request.enabled):
            body['enabled'] = request.enabled
        if not UtilClient.is_unset(request.policy_config):
            body['policyConfig'] = request.policy_config
        if not UtilClient.is_unset(request.policy_name):
            body['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.product_code):
            body['productCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertCollectionPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/collectionpolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpsertCollectionPolicyResponse(),
            self.execute(params, req, runtime)
        )

    async def upsert_collection_policy_with_options_async(
        self,
        request: sls_20201230_models.UpsertCollectionPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sls_20201230_models.UpsertCollectionPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attribute):
            body['attribute'] = request.attribute
        if not UtilClient.is_unset(request.centralize_config):
            body['centralizeConfig'] = request.centralize_config
        if not UtilClient.is_unset(request.centralize_enabled):
            body['centralizeEnabled'] = request.centralize_enabled
        if not UtilClient.is_unset(request.data_code):
            body['dataCode'] = request.data_code
        if not UtilClient.is_unset(request.enabled):
            body['enabled'] = request.enabled
        if not UtilClient.is_unset(request.policy_config):
            body['policyConfig'] = request.policy_config
        if not UtilClient.is_unset(request.policy_name):
            body['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.product_code):
            body['productCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertCollectionPolicy',
            version='2020-12-30',
            protocol='HTTPS',
            pathname=f'/collectionpolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sls_20201230_models.UpsertCollectionPolicyResponse(),
            await self.execute_async(params, req, runtime)
        )

    def upsert_collection_policy(
        self,
        request: sls_20201230_models.UpsertCollectionPolicyRequest,
    ) -> sls_20201230_models.UpsertCollectionPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upsert_collection_policy_with_options(request, headers, runtime)

    async def upsert_collection_policy_async(
        self,
        request: sls_20201230_models.UpsertCollectionPolicyRequest,
    ) -> sls_20201230_models.UpsertCollectionPolicyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upsert_collection_policy_with_options_async(request, headers, runtime)
