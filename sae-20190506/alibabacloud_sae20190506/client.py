# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sae20190506 import models as sae_20190506_models
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
        self._endpoint = self.get_endpoint('sae', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abort_and_rollback_change_order_with_options(
        self,
        request: sae_20190506_models.AbortAndRollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.AbortAndRollbackChangeOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortAndRollbackChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/AbortAndRollbackChangeOrder',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.AbortAndRollbackChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_and_rollback_change_order_with_options_async(
        self,
        request: sae_20190506_models.AbortAndRollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.AbortAndRollbackChangeOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortAndRollbackChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/AbortAndRollbackChangeOrder',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.AbortAndRollbackChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_and_rollback_change_order(
        self,
        request: sae_20190506_models.AbortAndRollbackChangeOrderRequest,
    ) -> sae_20190506_models.AbortAndRollbackChangeOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_and_rollback_change_order_with_options(request, headers, runtime)

    async def abort_and_rollback_change_order_async(
        self,
        request: sae_20190506_models.AbortAndRollbackChangeOrderRequest,
    ) -> sae_20190506_models.AbortAndRollbackChangeOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.abort_and_rollback_change_order_with_options_async(request, headers, runtime)

    def abort_change_order_with_options(
        self,
        request: sae_20190506_models.AbortChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.AbortChangeOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/AbortChangeOrder',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.AbortChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_change_order_with_options_async(
        self,
        request: sae_20190506_models.AbortChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.AbortChangeOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/AbortChangeOrder',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.AbortChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_change_order(
        self,
        request: sae_20190506_models.AbortChangeOrderRequest,
    ) -> sae_20190506_models.AbortChangeOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_change_order_with_options(request, headers, runtime)

    async def abort_change_order_async(
        self,
        request: sae_20190506_models.AbortChangeOrderRequest,
    ) -> sae_20190506_models.AbortChangeOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.abort_change_order_with_options_async(request, headers, runtime)

    def batch_start_applications_with_options(
        self,
        request: sae_20190506_models.BatchStartApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.BatchStartApplicationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/batchStartApplications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BatchStartApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_start_applications_with_options_async(
        self,
        request: sae_20190506_models.BatchStartApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.BatchStartApplicationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/batchStartApplications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BatchStartApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_start_applications(
        self,
        request: sae_20190506_models.BatchStartApplicationsRequest,
    ) -> sae_20190506_models.BatchStartApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_start_applications_with_options(request, headers, runtime)

    async def batch_start_applications_async(
        self,
        request: sae_20190506_models.BatchStartApplicationsRequest,
    ) -> sae_20190506_models.BatchStartApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_start_applications_with_options_async(request, headers, runtime)

    def batch_stop_applications_with_options(
        self,
        request: sae_20190506_models.BatchStopApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.BatchStopApplicationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/batchStopApplications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BatchStopApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_applications_with_options_async(
        self,
        request: sae_20190506_models.BatchStopApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.BatchStopApplicationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/batchStopApplications',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BatchStopApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_stop_applications(
        self,
        request: sae_20190506_models.BatchStopApplicationsRequest,
    ) -> sae_20190506_models.BatchStopApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_stop_applications_with_options(request, headers, runtime)

    async def batch_stop_applications_async(
        self,
        request: sae_20190506_models.BatchStopApplicationsRequest,
    ) -> sae_20190506_models.BatchStopApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_stop_applications_with_options_async(request, headers, runtime)

    def bind_slb_with_options(
        self,
        request: sae_20190506_models.BindSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.BindSlbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.internet):
            query['Internet'] = request.internet
        if not UtilClient.is_unset(request.internet_slb_id):
            query['InternetSlbId'] = request.internet_slb_id
        if not UtilClient.is_unset(request.intranet):
            query['Intranet'] = request.intranet
        if not UtilClient.is_unset(request.intranet_slb_id):
            query['IntranetSlbId'] = request.intranet_slb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSlb',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/slb',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BindSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_slb_with_options_async(
        self,
        request: sae_20190506_models.BindSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.BindSlbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.internet):
            query['Internet'] = request.internet
        if not UtilClient.is_unset(request.internet_slb_id):
            query['InternetSlbId'] = request.internet_slb_id
        if not UtilClient.is_unset(request.intranet):
            query['Intranet'] = request.intranet
        if not UtilClient.is_unset(request.intranet_slb_id):
            query['IntranetSlbId'] = request.intranet_slb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSlb',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/slb',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.BindSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_slb(
        self,
        request: sae_20190506_models.BindSlbRequest,
    ) -> sae_20190506_models.BindSlbResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_slb_with_options(request, headers, runtime)

    async def bind_slb_async(
        self,
        request: sae_20190506_models.BindSlbRequest,
    ) -> sae_20190506_models.BindSlbResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.bind_slb_with_options_async(request, headers, runtime)

    def confirm_pipeline_batch_with_options(
        self,
        request: sae_20190506_models.ConfirmPipelineBatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ConfirmPipelineBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.confirm):
            query['Confirm'] = request.confirm
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmPipelineBatch',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/ConfirmPipelineBatch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ConfirmPipelineBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_pipeline_batch_with_options_async(
        self,
        request: sae_20190506_models.ConfirmPipelineBatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ConfirmPipelineBatchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.confirm):
            query['Confirm'] = request.confirm
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmPipelineBatch',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/ConfirmPipelineBatch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ConfirmPipelineBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_pipeline_batch(
        self,
        request: sae_20190506_models.ConfirmPipelineBatchRequest,
    ) -> sae_20190506_models.ConfirmPipelineBatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.confirm_pipeline_batch_with_options(request, headers, runtime)

    async def confirm_pipeline_batch_async(
        self,
        request: sae_20190506_models.ConfirmPipelineBatchRequest,
    ) -> sae_20190506_models.ConfirmPipelineBatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.confirm_pipeline_batch_with_options_async(request, headers, runtime)

    def create_application_with_options(
        self,
        request: sae_20190506_models.CreateApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.deploy):
            query['Deploy'] = request.deploy
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.micro_registration):
            query['MicroRegistration'] = request.micro_registration
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.pvtz_discovery_svc):
            query['PvtzDiscoverySvc'] = request.pvtz_discovery_svc
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/createApplication',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        request: sae_20190506_models.CreateApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.deploy):
            query['Deploy'] = request.deploy
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.micro_registration):
            query['MicroRegistration'] = request.micro_registration
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.pvtz_discovery_svc):
            query['PvtzDiscoverySvc'] = request.pvtz_discovery_svc
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/createApplication',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: sae_20190506_models.CreateApplicationRequest,
    ) -> sae_20190506_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_application_with_options(request, headers, runtime)

    async def create_application_async(
        self,
        request: sae_20190506_models.CreateApplicationRequest,
    ) -> sae_20190506_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_application_with_options_async(request, headers, runtime)

    def create_application_scaling_rule_with_options(
        self,
        request: sae_20190506_models.CreateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateApplicationScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_scaling_rule_with_options_async(
        self,
        request: sae_20190506_models.CreateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateApplicationScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_scaling_rule(
        self,
        request: sae_20190506_models.CreateApplicationScalingRuleRequest,
    ) -> sae_20190506_models.CreateApplicationScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_application_scaling_rule_with_options(request, headers, runtime)

    async def create_application_scaling_rule_async(
        self,
        request: sae_20190506_models.CreateApplicationScalingRuleRequest,
    ) -> sae_20190506_models.CreateApplicationScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_application_scaling_rule_with_options_async(request, headers, runtime)

    def create_config_map_with_options(
        self,
        request: sae_20190506_models.CreateConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateConfigMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_map_with_options_async(
        self,
        request: sae_20190506_models.CreateConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateConfigMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config_map(
        self,
        request: sae_20190506_models.CreateConfigMapRequest,
    ) -> sae_20190506_models.CreateConfigMapResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_config_map_with_options(request, headers, runtime)

    async def create_config_map_async(
        self,
        request: sae_20190506_models.CreateConfigMapRequest,
    ) -> sae_20190506_models.CreateConfigMapResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_config_map_with_options_async(request, headers, runtime)

    def create_grey_tag_route_with_options(
        self,
        request: sae_20190506_models.CreateGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateGreyTagRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_rules):
            query['AlbRules'] = request.alb_rules
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_grey_tag_route_with_options_async(
        self,
        request: sae_20190506_models.CreateGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateGreyTagRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_rules):
            query['AlbRules'] = request.alb_rules
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_grey_tag_route(
        self,
        request: sae_20190506_models.CreateGreyTagRouteRequest,
    ) -> sae_20190506_models.CreateGreyTagRouteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_grey_tag_route_with_options(request, headers, runtime)

    async def create_grey_tag_route_async(
        self,
        request: sae_20190506_models.CreateGreyTagRouteRequest,
    ) -> sae_20190506_models.CreateGreyTagRouteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_grey_tag_route_with_options_async(request, headers, runtime)

    def create_ingress_with_options(
        self,
        request: sae_20190506_models.CreateIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateIngressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        body = {}
        if not UtilClient.is_unset(request.rules):
            body['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateIngressResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ingress_with_options_async(
        self,
        request: sae_20190506_models.CreateIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateIngressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        body = {}
        if not UtilClient.is_unset(request.rules):
            body['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateIngressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ingress(
        self,
        request: sae_20190506_models.CreateIngressRequest,
    ) -> sae_20190506_models.CreateIngressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_ingress_with_options(request, headers, runtime)

    async def create_ingress_async(
        self,
        request: sae_20190506_models.CreateIngressRequest,
    ) -> sae_20190506_models.CreateIngressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_ingress_with_options_async(request, headers, runtime)

    def create_job_with_options(
        self,
        request: sae_20190506_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.backoff_limit):
            query['BackoffLimit'] = request.backoff_limit
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.concurrency_policy):
            query['ConcurrencyPolicy'] = request.concurrency_policy
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.ref_app_id):
            query['RefAppId'] = request.ref_app_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.slice):
            query['Slice'] = request.slice
        if not UtilClient.is_unset(request.slice_envs):
            query['SliceEnvs'] = request.slice_envs
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.trigger_config):
            query['TriggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.enable_image_accl):
            body['EnableImageAccl'] = request.enable_image_accl
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/createJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: sae_20190506_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auto_config):
            query['AutoConfig'] = request.auto_config
        if not UtilClient.is_unset(request.backoff_limit):
            query['BackoffLimit'] = request.backoff_limit
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.concurrency_policy):
            query['ConcurrencyPolicy'] = request.concurrency_policy
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.ref_app_id):
            query['RefAppId'] = request.ref_app_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.slice):
            query['Slice'] = request.slice
        if not UtilClient.is_unset(request.slice_envs):
            query['SliceEnvs'] = request.slice_envs
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.trigger_config):
            query['TriggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.enable_image_accl):
            body['EnableImageAccl'] = request.enable_image_accl
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/createJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: sae_20190506_models.CreateJobRequest,
    ) -> sae_20190506_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(request, headers, runtime)

    async def create_job_async(
        self,
        request: sae_20190506_models.CreateJobRequest,
    ) -> sae_20190506_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(request, headers, runtime)

    def create_namespace_with_options(
        self,
        request: sae_20190506_models.CreateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: sae_20190506_models.CreateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: sae_20190506_models.CreateNamespaceRequest,
    ) -> sae_20190506_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_namespace_with_options(request, headers, runtime)

    async def create_namespace_async(
        self,
        request: sae_20190506_models.CreateNamespaceRequest,
    ) -> sae_20190506_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_namespace_with_options_async(request, headers, runtime)

    def create_secret_with_options(
        self,
        request: sae_20190506_models.CreateSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.secret_type):
            query['SecretType'] = request.secret_type
        body = {}
        if not UtilClient.is_unset(request.secret_data):
            body['SecretData'] = request.secret_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_secret_with_options_async(
        self,
        request: sae_20190506_models.CreateSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.CreateSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.secret_type):
            query['SecretType'] = request.secret_type
        body = {}
        if not UtilClient.is_unset(request.secret_data):
            body['SecretData'] = request.secret_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.CreateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_secret(
        self,
        request: sae_20190506_models.CreateSecretRequest,
    ) -> sae_20190506_models.CreateSecretResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_secret_with_options(request, headers, runtime)

    async def create_secret_async(
        self,
        request: sae_20190506_models.CreateSecretRequest,
    ) -> sae_20190506_models.CreateSecretResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_secret_with_options_async(request, headers, runtime)

    def delete_application_with_options(
        self,
        request: sae_20190506_models.DeleteApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/deleteApplication',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: sae_20190506_models.DeleteApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/deleteApplication',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: sae_20190506_models.DeleteApplicationRequest,
    ) -> sae_20190506_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_application_with_options(request, headers, runtime)

    async def delete_application_async(
        self,
        request: sae_20190506_models.DeleteApplicationRequest,
    ) -> sae_20190506_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_application_with_options_async(request, headers, runtime)

    def delete_application_scaling_rule_with_options(
        self,
        request: sae_20190506_models.DeleteApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteApplicationScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_scaling_rule_with_options_async(
        self,
        request: sae_20190506_models.DeleteApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteApplicationScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_scaling_rule(
        self,
        request: sae_20190506_models.DeleteApplicationScalingRuleRequest,
    ) -> sae_20190506_models.DeleteApplicationScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_application_scaling_rule_with_options(request, headers, runtime)

    async def delete_application_scaling_rule_async(
        self,
        request: sae_20190506_models.DeleteApplicationScalingRuleRequest,
    ) -> sae_20190506_models.DeleteApplicationScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_application_scaling_rule_with_options_async(request, headers, runtime)

    def delete_config_map_with_options(
        self,
        request: sae_20190506_models.DeleteConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteConfigMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_map_with_options_async(
        self,
        request: sae_20190506_models.DeleteConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteConfigMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config_map(
        self,
        request: sae_20190506_models.DeleteConfigMapRequest,
    ) -> sae_20190506_models.DeleteConfigMapResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_config_map_with_options(request, headers, runtime)

    async def delete_config_map_async(
        self,
        request: sae_20190506_models.DeleteConfigMapRequest,
    ) -> sae_20190506_models.DeleteConfigMapResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_config_map_with_options_async(request, headers, runtime)

    def delete_grey_tag_route_with_options(
        self,
        request: sae_20190506_models.DeleteGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteGreyTagRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_grey_tag_route_with_options_async(
        self,
        request: sae_20190506_models.DeleteGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteGreyTagRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_grey_tag_route(
        self,
        request: sae_20190506_models.DeleteGreyTagRouteRequest,
    ) -> sae_20190506_models.DeleteGreyTagRouteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_grey_tag_route_with_options(request, headers, runtime)

    async def delete_grey_tag_route_async(
        self,
        request: sae_20190506_models.DeleteGreyTagRouteRequest,
    ) -> sae_20190506_models.DeleteGreyTagRouteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_grey_tag_route_with_options_async(request, headers, runtime)

    def delete_history_job_with_options(
        self,
        request: sae_20190506_models.DeleteHistoryJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteHistoryJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHistoryJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/deleteHistoryJob',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteHistoryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_history_job_with_options_async(
        self,
        request: sae_20190506_models.DeleteHistoryJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteHistoryJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHistoryJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/deleteHistoryJob',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteHistoryJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_history_job(
        self,
        request: sae_20190506_models.DeleteHistoryJobRequest,
    ) -> sae_20190506_models.DeleteHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_history_job_with_options(request, headers, runtime)

    async def delete_history_job_async(
        self,
        request: sae_20190506_models.DeleteHistoryJobRequest,
    ) -> sae_20190506_models.DeleteHistoryJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_history_job_with_options_async(request, headers, runtime)

    def delete_ingress_with_options(
        self,
        request: sae_20190506_models.DeleteIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteIngressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteIngressResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ingress_with_options_async(
        self,
        request: sae_20190506_models.DeleteIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteIngressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteIngressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ingress(
        self,
        request: sae_20190506_models.DeleteIngressRequest,
    ) -> sae_20190506_models.DeleteIngressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ingress_with_options(request, headers, runtime)

    async def delete_ingress_async(
        self,
        request: sae_20190506_models.DeleteIngressRequest,
    ) -> sae_20190506_models.DeleteIngressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_ingress_with_options_async(request, headers, runtime)

    def delete_job_with_options(
        self,
        request: sae_20190506_models.DeleteJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/deleteJob',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        request: sae_20190506_models.DeleteJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/deleteJob',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job(
        self,
        request: sae_20190506_models.DeleteJobRequest,
    ) -> sae_20190506_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_job_with_options(request, headers, runtime)

    async def delete_job_async(
        self,
        request: sae_20190506_models.DeleteJobRequest,
    ) -> sae_20190506_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_job_with_options_async(request, headers, runtime)

    def delete_namespace_with_options(
        self,
        request: sae_20190506_models.DeleteNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: sae_20190506_models.DeleteNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: sae_20190506_models.DeleteNamespaceRequest,
    ) -> sae_20190506_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_namespace_with_options(request, headers, runtime)

    async def delete_namespace_async(
        self,
        request: sae_20190506_models.DeleteNamespaceRequest,
    ) -> sae_20190506_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_namespace_with_options_async(request, headers, runtime)

    def delete_secret_with_options(
        self,
        request: sae_20190506_models.DeleteSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_with_options_async(
        self,
        request: sae_20190506_models.DeleteSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeleteSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeleteSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret(
        self,
        request: sae_20190506_models.DeleteSecretRequest,
    ) -> sae_20190506_models.DeleteSecretResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_secret_with_options(request, headers, runtime)

    async def delete_secret_async(
        self,
        request: sae_20190506_models.DeleteSecretRequest,
    ) -> sae_20190506_models.DeleteSecretResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_secret_with_options_async(request, headers, runtime)

    def deploy_application_with_options(
        self,
        request: sae_20190506_models.DeployApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeployApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.change_order_desc):
            query['ChangeOrderDesc'] = request.change_order_desc
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.deploy):
            query['Deploy'] = request.deploy
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not UtilClient.is_unset(request.enable_grey_tag_route):
            query['EnableGreyTagRoute'] = request.enable_grey_tag_route
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.micro_registration):
            query['MicroRegistration'] = request.micro_registration
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.pvtz_discovery_svc):
            query['PvtzDiscoverySvc'] = request.pvtz_discovery_svc
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/deployApplication',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeployApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_application_with_options_async(
        self,
        request: sae_20190506_models.DeployApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DeployApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.change_order_desc):
            query['ChangeOrderDesc'] = request.change_order_desc
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.deploy):
            query['Deploy'] = request.deploy
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not UtilClient.is_unset(request.enable_grey_tag_route):
            query['EnableGreyTagRoute'] = request.enable_grey_tag_route
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.kafka_configs):
            query['KafkaConfigs'] = request.kafka_configs
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.micro_registration):
            query['MicroRegistration'] = request.micro_registration
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.nas_configs):
            query['NasConfigs'] = request.nas_configs
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_arms_config_location):
            query['PhpArmsConfigLocation'] = request.php_arms_config_location
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.pvtz_discovery_svc):
            query['PvtzDiscoverySvc'] = request.pvtz_discovery_svc
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.associate_eip):
            body['AssociateEip'] = request.associate_eip
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/deployApplication',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DeployApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_application(
        self,
        request: sae_20190506_models.DeployApplicationRequest,
    ) -> sae_20190506_models.DeployApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_application_with_options(request, headers, runtime)

    async def deploy_application_async(
        self,
        request: sae_20190506_models.DeployApplicationRequest,
    ) -> sae_20190506_models.DeployApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_application_with_options_async(request, headers, runtime)

    def describe_app_service_detail_with_options(
        self,
        request: sae_20190506_models.DescribeAppServiceDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeAppServiceDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.service_group):
            query['ServiceGroup'] = request.service_group
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppServiceDetail',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/describeAppServiceDetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeAppServiceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_service_detail_with_options_async(
        self,
        request: sae_20190506_models.DescribeAppServiceDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeAppServiceDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.service_group):
            query['ServiceGroup'] = request.service_group
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppServiceDetail',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/describeAppServiceDetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeAppServiceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_service_detail(
        self,
        request: sae_20190506_models.DescribeAppServiceDetailRequest,
    ) -> sae_20190506_models.DescribeAppServiceDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_service_detail_with_options(request, headers, runtime)

    async def describe_app_service_detail_async(
        self,
        request: sae_20190506_models.DescribeAppServiceDetailRequest,
    ) -> sae_20190506_models.DescribeAppServiceDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_service_detail_with_options_async(request, headers, runtime)

    def describe_application_config_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_config_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationConfig',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_config(
        self,
        request: sae_20190506_models.DescribeApplicationConfigRequest,
    ) -> sae_20190506_models.DescribeApplicationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_config_with_options(request, headers, runtime)

    async def describe_application_config_async(
        self,
        request: sae_20190506_models.DescribeApplicationConfigRequest,
    ) -> sae_20190506_models.DescribeApplicationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_config_with_options_async(request, headers, runtime)

    def describe_application_groups_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationGroups',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_groups_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationGroups',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_groups(
        self,
        request: sae_20190506_models.DescribeApplicationGroupsRequest,
    ) -> sae_20190506_models.DescribeApplicationGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_groups_with_options(request, headers, runtime)

    async def describe_application_groups_async(
        self,
        request: sae_20190506_models.DescribeApplicationGroupsRequest,
    ) -> sae_20190506_models.DescribeApplicationGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_groups_with_options_async(request, headers, runtime)

    def describe_application_image_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationImage',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/container/describeApplicationImage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_image_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationImage',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/container/describeApplicationImage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_image(
        self,
        request: sae_20190506_models.DescribeApplicationImageRequest,
    ) -> sae_20190506_models.DescribeApplicationImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_image_with_options(request, headers, runtime)

    async def describe_application_image_async(
        self,
        request: sae_20190506_models.DescribeApplicationImageRequest,
    ) -> sae_20190506_models.DescribeApplicationImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_image_with_options_async(request, headers, runtime)

    def describe_application_instances_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationInstances',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_instances_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationInstances',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_instances(
        self,
        request: sae_20190506_models.DescribeApplicationInstancesRequest,
    ) -> sae_20190506_models.DescribeApplicationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_instances_with_options(request, headers, runtime)

    async def describe_application_instances_async(
        self,
        request: sae_20190506_models.DescribeApplicationInstancesRequest,
    ) -> sae_20190506_models.DescribeApplicationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_instances_with_options_async(request, headers, runtime)

    def describe_application_scaling_rule_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_scaling_rule_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_scaling_rule(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRuleRequest,
    ) -> sae_20190506_models.DescribeApplicationScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_scaling_rule_with_options(request, headers, runtime)

    async def describe_application_scaling_rule_async(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRuleRequest,
    ) -> sae_20190506_models.DescribeApplicationScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_scaling_rule_with_options_async(request, headers, runtime)

    def describe_application_scaling_rules_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationScalingRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationScalingRules',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_scaling_rules_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationScalingRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationScalingRules',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_scaling_rules(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRulesRequest,
    ) -> sae_20190506_models.DescribeApplicationScalingRulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_scaling_rules_with_options(request, headers, runtime)

    async def describe_application_scaling_rules_async(
        self,
        request: sae_20190506_models.DescribeApplicationScalingRulesRequest,
    ) -> sae_20190506_models.DescribeApplicationScalingRulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_scaling_rules_with_options_async(request, headers, runtime)

    def describe_application_slbs_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationSlbsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationSlbsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationSlbs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/slb',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationSlbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_slbs_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationSlbsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationSlbsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationSlbs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/slb',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationSlbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_slbs(
        self,
        request: sae_20190506_models.DescribeApplicationSlbsRequest,
    ) -> sae_20190506_models.DescribeApplicationSlbsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_slbs_with_options(request, headers, runtime)

    async def describe_application_slbs_async(
        self,
        request: sae_20190506_models.DescribeApplicationSlbsRequest,
    ) -> sae_20190506_models.DescribeApplicationSlbsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_slbs_with_options_async(request, headers, runtime)

    def describe_application_status_with_options(
        self,
        request: sae_20190506_models.DescribeApplicationStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationStatus',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_status_with_options_async(
        self,
        request: sae_20190506_models.DescribeApplicationStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeApplicationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationStatus',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/describeApplicationStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeApplicationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_status(
        self,
        request: sae_20190506_models.DescribeApplicationStatusRequest,
    ) -> sae_20190506_models.DescribeApplicationStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_status_with_options(request, headers, runtime)

    async def describe_application_status_async(
        self,
        request: sae_20190506_models.DescribeApplicationStatusRequest,
    ) -> sae_20190506_models.DescribeApplicationStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_status_with_options_async(request, headers, runtime)

    def describe_change_order_with_options(
        self,
        request: sae_20190506_models.DescribeChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeChangeOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/DescribeChangeOrder',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_change_order_with_options_async(
        self,
        request: sae_20190506_models.DescribeChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeChangeOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChangeOrder',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/DescribeChangeOrder',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_change_order(
        self,
        request: sae_20190506_models.DescribeChangeOrderRequest,
    ) -> sae_20190506_models.DescribeChangeOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_change_order_with_options(request, headers, runtime)

    async def describe_change_order_async(
        self,
        request: sae_20190506_models.DescribeChangeOrderRequest,
    ) -> sae_20190506_models.DescribeChangeOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_change_order_with_options_async(request, headers, runtime)

    def describe_components_with_options(
        self,
        request: sae_20190506_models.DescribeComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponents',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/resource/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_components_with_options_async(
        self,
        request: sae_20190506_models.DescribeComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponents',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/resource/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_components(
        self,
        request: sae_20190506_models.DescribeComponentsRequest,
    ) -> sae_20190506_models.DescribeComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_components_with_options(request, headers, runtime)

    async def describe_components_async(
        self,
        request: sae_20190506_models.DescribeComponentsRequest,
    ) -> sae_20190506_models.DescribeComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_components_with_options_async(request, headers, runtime)

    def describe_config_map_with_options(
        self,
        request: sae_20190506_models.DescribeConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeConfigMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_config_map_with_options_async(
        self,
        request: sae_20190506_models.DescribeConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeConfigMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_config_map(
        self,
        request: sae_20190506_models.DescribeConfigMapRequest,
    ) -> sae_20190506_models.DescribeConfigMapResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_config_map_with_options(request, headers, runtime)

    async def describe_config_map_async(
        self,
        request: sae_20190506_models.DescribeConfigMapRequest,
    ) -> sae_20190506_models.DescribeConfigMapResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_config_map_with_options_async(request, headers, runtime)

    def describe_configuration_price_with_options(
        self,
        request: sae_20190506_models.DescribeConfigurationPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeConfigurationPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigurationPrice',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/configurationPrice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeConfigurationPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_configuration_price_with_options_async(
        self,
        request: sae_20190506_models.DescribeConfigurationPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeConfigurationPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigurationPrice',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/configurationPrice',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeConfigurationPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_configuration_price(
        self,
        request: sae_20190506_models.DescribeConfigurationPriceRequest,
    ) -> sae_20190506_models.DescribeConfigurationPriceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_configuration_price_with_options(request, headers, runtime)

    async def describe_configuration_price_async(
        self,
        request: sae_20190506_models.DescribeConfigurationPriceRequest,
    ) -> sae_20190506_models.DescribeConfigurationPriceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_configuration_price_with_options_async(request, headers, runtime)

    def describe_edas_containers_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeEdasContainersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdasContainers',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/resource/edasContainers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeEdasContainersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_edas_containers_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeEdasContainersResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdasContainers',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/resource/edasContainers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeEdasContainersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_edas_containers(self) -> sae_20190506_models.DescribeEdasContainersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edas_containers_with_options(headers, runtime)

    async def describe_edas_containers_async(self) -> sae_20190506_models.DescribeEdasContainersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_edas_containers_with_options_async(headers, runtime)

    def describe_grey_tag_route_with_options(
        self,
        request: sae_20190506_models.DescribeGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeGreyTagRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grey_tag_route_with_options_async(
        self,
        request: sae_20190506_models.DescribeGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeGreyTagRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grey_tag_route(
        self,
        request: sae_20190506_models.DescribeGreyTagRouteRequest,
    ) -> sae_20190506_models.DescribeGreyTagRouteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_grey_tag_route_with_options(request, headers, runtime)

    async def describe_grey_tag_route_async(
        self,
        request: sae_20190506_models.DescribeGreyTagRouteRequest,
    ) -> sae_20190506_models.DescribeGreyTagRouteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_grey_tag_route_with_options_async(request, headers, runtime)

    def describe_ingress_with_options(
        self,
        request: sae_20190506_models.DescribeIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeIngressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeIngressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ingress_with_options_async(
        self,
        request: sae_20190506_models.DescribeIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeIngressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeIngressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ingress(
        self,
        request: sae_20190506_models.DescribeIngressRequest,
    ) -> sae_20190506_models.DescribeIngressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_ingress_with_options(request, headers, runtime)

    async def describe_ingress_async(
        self,
        request: sae_20190506_models.DescribeIngressRequest,
    ) -> sae_20190506_models.DescribeIngressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_ingress_with_options_async(request, headers, runtime)

    def describe_instance_log_with_options(
        self,
        request: sae_20190506_models.DescribeInstanceLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeInstanceLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceLog',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/instance/describeInstanceLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeInstanceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_log_with_options_async(
        self,
        request: sae_20190506_models.DescribeInstanceLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeInstanceLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceLog',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/instance/describeInstanceLog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeInstanceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_log(
        self,
        request: sae_20190506_models.DescribeInstanceLogRequest,
    ) -> sae_20190506_models.DescribeInstanceLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_log_with_options(request, headers, runtime)

    async def describe_instance_log_async(
        self,
        request: sae_20190506_models.DescribeInstanceLogRequest,
    ) -> sae_20190506_models.DescribeInstanceLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_instance_log_with_options_async(request, headers, runtime)

    def describe_instance_specifications_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeInstanceSpecificationsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecifications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/quota/instanceSpecifications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeInstanceSpecificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_specifications_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeInstanceSpecificationsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecifications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/quota/instanceSpecifications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeInstanceSpecificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_specifications(self) -> sae_20190506_models.DescribeInstanceSpecificationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_specifications_with_options(headers, runtime)

    async def describe_instance_specifications_async(self) -> sae_20190506_models.DescribeInstanceSpecificationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_instance_specifications_with_options_async(headers, runtime)

    def describe_job_with_options(
        self,
        request: sae_20190506_models.DescribeJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/describeJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_with_options_async(
        self,
        request: sae_20190506_models.DescribeJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/describeJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job(
        self,
        request: sae_20190506_models.DescribeJobRequest,
    ) -> sae_20190506_models.DescribeJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_job_with_options(request, headers, runtime)

    async def describe_job_async(
        self,
        request: sae_20190506_models.DescribeJobRequest,
    ) -> sae_20190506_models.DescribeJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_job_with_options_async(request, headers, runtime)

    def describe_job_history_with_options(
        self,
        request: sae_20190506_models.DescribeJobHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeJobHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobHistory',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/describeJobHistory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_history_with_options_async(
        self,
        request: sae_20190506_models.DescribeJobHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeJobHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobHistory',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/describeJobHistory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_history(
        self,
        request: sae_20190506_models.DescribeJobHistoryRequest,
    ) -> sae_20190506_models.DescribeJobHistoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_job_history_with_options(request, headers, runtime)

    async def describe_job_history_async(
        self,
        request: sae_20190506_models.DescribeJobHistoryRequest,
    ) -> sae_20190506_models.DescribeJobHistoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_job_history_with_options_async(request, headers, runtime)

    def describe_job_status_with_options(
        self,
        request: sae_20190506_models.DescribeJobStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobStatus',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/describeJobStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_status_with_options_async(
        self,
        request: sae_20190506_models.DescribeJobStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobStatus',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/describeJobStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_status(
        self,
        request: sae_20190506_models.DescribeJobStatusRequest,
    ) -> sae_20190506_models.DescribeJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_job_status_with_options(request, headers, runtime)

    async def describe_job_status_async(
        self,
        request: sae_20190506_models.DescribeJobStatusRequest,
    ) -> sae_20190506_models.DescribeJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_job_status_with_options_async(request, headers, runtime)

    def describe_namespace_with_options(
        self,
        request: sae_20190506_models.DescribeNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_with_options_async(
        self,
        request: sae_20190506_models.DescribeNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace(
        self,
        request: sae_20190506_models.DescribeNamespaceRequest,
    ) -> sae_20190506_models.DescribeNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespace_with_options(request, headers, runtime)

    async def describe_namespace_async(
        self,
        request: sae_20190506_models.DescribeNamespaceRequest,
    ) -> sae_20190506_models.DescribeNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespace_with_options_async(request, headers, runtime)

    def describe_namespace_list_with_options(
        self,
        request: sae_20190506_models.DescribeNamespaceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespaceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contain_custom):
            query['ContainCustom'] = request.contain_custom
        if not UtilClient.is_unset(request.hybrid_cloud_exclude):
            query['HybridCloudExclude'] = request.hybrid_cloud_exclude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceList',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/namespace/describeNamespaceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_list_with_options_async(
        self,
        request: sae_20190506_models.DescribeNamespaceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespaceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contain_custom):
            query['ContainCustom'] = request.contain_custom
        if not UtilClient.is_unset(request.hybrid_cloud_exclude):
            query['HybridCloudExclude'] = request.hybrid_cloud_exclude
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceList',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/namespace/describeNamespaceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace_list(
        self,
        request: sae_20190506_models.DescribeNamespaceListRequest,
    ) -> sae_20190506_models.DescribeNamespaceListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespace_list_with_options(request, headers, runtime)

    async def describe_namespace_list_async(
        self,
        request: sae_20190506_models.DescribeNamespaceListRequest,
    ) -> sae_20190506_models.DescribeNamespaceListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespace_list_with_options_async(request, headers, runtime)

    def describe_namespace_resources_with_options(
        self,
        request: sae_20190506_models.DescribeNamespaceResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespaceResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/namespace/describeNamespaceResources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_resources_with_options_async(
        self,
        request: sae_20190506_models.DescribeNamespaceResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespaceResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/namespace/describeNamespaceResources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespaceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace_resources(
        self,
        request: sae_20190506_models.DescribeNamespaceResourcesRequest,
    ) -> sae_20190506_models.DescribeNamespaceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespace_resources_with_options(request, headers, runtime)

    async def describe_namespace_resources_async(
        self,
        request: sae_20190506_models.DescribeNamespaceResourcesRequest,
    ) -> sae_20190506_models.DescribeNamespaceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespace_resources_with_options_async(request, headers, runtime)

    def describe_namespaces_with_options(
        self,
        request: sae_20190506_models.DescribeNamespacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaces',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespaces_with_options_async(
        self,
        request: sae_20190506_models.DescribeNamespacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeNamespacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaces',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespaces(
        self,
        request: sae_20190506_models.DescribeNamespacesRequest,
    ) -> sae_20190506_models.DescribeNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_namespaces_with_options(request, headers, runtime)

    async def describe_namespaces_async(
        self,
        request: sae_20190506_models.DescribeNamespacesRequest,
    ) -> sae_20190506_models.DescribeNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_namespaces_with_options_async(request, headers, runtime)

    def describe_pipeline_with_options(
        self,
        request: sae_20190506_models.DescribePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribePipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePipeline',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/DescribePipeline',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pipeline_with_options_async(
        self,
        request: sae_20190506_models.DescribePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribePipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePipeline',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/DescribePipeline',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pipeline(
        self,
        request: sae_20190506_models.DescribePipelineRequest,
    ) -> sae_20190506_models.DescribePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_pipeline_with_options(request, headers, runtime)

    async def describe_pipeline_async(
        self,
        request: sae_20190506_models.DescribePipelineRequest,
    ) -> sae_20190506_models.DescribePipelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_pipeline_with_options_async(request, headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/regionConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/regionConfig',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> sae_20190506_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> sae_20190506_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(headers, runtime)

    def describe_secret_with_options(
        self,
        request: sae_20190506_models.DescribeSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_secret_with_options_async(
        self,
        request: sae_20190506_models.DescribeSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DescribeSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DescribeSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_secret(
        self,
        request: sae_20190506_models.DescribeSecretRequest,
    ) -> sae_20190506_models.DescribeSecretResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_secret_with_options(request, headers, runtime)

    async def describe_secret_async(
        self,
        request: sae_20190506_models.DescribeSecretRequest,
    ) -> sae_20190506_models.DescribeSecretResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_secret_with_options_async(request, headers, runtime)

    def disable_application_scaling_rule_with_options(
        self,
        request: sae_20190506_models.DisableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DisableApplicationScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/disableApplicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DisableApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_scaling_rule_with_options_async(
        self,
        request: sae_20190506_models.DisableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.DisableApplicationScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/disableApplicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.DisableApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_scaling_rule(
        self,
        request: sae_20190506_models.DisableApplicationScalingRuleRequest,
    ) -> sae_20190506_models.DisableApplicationScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_application_scaling_rule_with_options(request, headers, runtime)

    async def disable_application_scaling_rule_async(
        self,
        request: sae_20190506_models.DisableApplicationScalingRuleRequest,
    ) -> sae_20190506_models.DisableApplicationScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_application_scaling_rule_with_options_async(request, headers, runtime)

    def enable_application_scaling_rule_with_options(
        self,
        request: sae_20190506_models.EnableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.EnableApplicationScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/enableApplicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.EnableApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_scaling_rule_with_options_async(
        self,
        request: sae_20190506_models.EnableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.EnableApplicationScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/enableApplicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.EnableApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_scaling_rule(
        self,
        request: sae_20190506_models.EnableApplicationScalingRuleRequest,
    ) -> sae_20190506_models.EnableApplicationScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_application_scaling_rule_with_options(request, headers, runtime)

    async def enable_application_scaling_rule_async(
        self,
        request: sae_20190506_models.EnableApplicationScalingRuleRequest,
    ) -> sae_20190506_models.EnableApplicationScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_application_scaling_rule_with_options_async(request, headers, runtime)

    def exec_job_with_options(
        self,
        request: sae_20190506_models.ExecJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ExecJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/execJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ExecJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_job_with_options_async(
        self,
        request: sae_20190506_models.ExecJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ExecJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.time):
            query['Time'] = request.time
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/execJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ExecJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_job(
        self,
        request: sae_20190506_models.ExecJobRequest,
    ) -> sae_20190506_models.ExecJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.exec_job_with_options(request, headers, runtime)

    async def exec_job_async(
        self,
        request: sae_20190506_models.ExecJobRequest,
    ) -> sae_20190506_models.ExecJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.exec_job_with_options_async(request, headers, runtime)

    def list_app_events_with_options(
        self,
        request: sae_20190506_models.ListAppEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.object_kind):
            query['ObjectKind'] = request.object_kind
        if not UtilClient.is_unset(request.object_name):
            query['ObjectName'] = request.object_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppEvents',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/listAppEvents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_events_with_options_async(
        self,
        request: sae_20190506_models.ListAppEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.object_kind):
            query['ObjectKind'] = request.object_kind
        if not UtilClient.is_unset(request.object_name):
            query['ObjectName'] = request.object_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppEvents',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/listAppEvents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_events(
        self,
        request: sae_20190506_models.ListAppEventsRequest,
    ) -> sae_20190506_models.ListAppEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_events_with_options(request, headers, runtime)

    async def list_app_events_async(
        self,
        request: sae_20190506_models.ListAppEventsRequest,
    ) -> sae_20190506_models.ListAppEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_app_events_with_options_async(request, headers, runtime)

    def list_app_services_page_with_options(
        self,
        request: sae_20190506_models.ListAppServicesPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppServicesPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppServicesPage',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listAppServicesPage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppServicesPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_services_page_with_options_async(
        self,
        request: sae_20190506_models.ListAppServicesPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppServicesPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppServicesPage',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listAppServicesPage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppServicesPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_services_page(
        self,
        request: sae_20190506_models.ListAppServicesPageRequest,
    ) -> sae_20190506_models.ListAppServicesPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_services_page_with_options(request, headers, runtime)

    async def list_app_services_page_async(
        self,
        request: sae_20190506_models.ListAppServicesPageRequest,
    ) -> sae_20190506_models.ListAppServicesPageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_app_services_page_with_options_async(request, headers, runtime)

    def list_app_versions_with_options(
        self,
        request: sae_20190506_models.ListAppVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppVersions',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/listAppVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_versions_with_options_async(
        self,
        request: sae_20190506_models.ListAppVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListAppVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppVersions',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/listAppVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListAppVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_versions(
        self,
        request: sae_20190506_models.ListAppVersionsRequest,
    ) -> sae_20190506_models.ListAppVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_app_versions_with_options(request, headers, runtime)

    async def list_app_versions_async(
        self,
        request: sae_20190506_models.ListAppVersionsRequest,
    ) -> sae_20190506_models.ListAppVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_app_versions_with_options_async(request, headers, runtime)

    def list_applications_with_options(
        self,
        request: sae_20190506_models.ListApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListApplicationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_type):
            query['FieldType'] = request.field_type
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/listApplications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        request: sae_20190506_models.ListApplicationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListApplicationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_type):
            query['FieldType'] = request.field_type
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/listApplications',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(
        self,
        request: sae_20190506_models.ListApplicationsRequest,
    ) -> sae_20190506_models.ListApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_applications_with_options(request, headers, runtime)

    async def list_applications_async(
        self,
        request: sae_20190506_models.ListApplicationsRequest,
    ) -> sae_20190506_models.ListApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_applications_with_options_async(request, headers, runtime)

    def list_change_orders_with_options(
        self,
        request: sae_20190506_models.ListChangeOrdersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListChangeOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.co_status):
            query['CoStatus'] = request.co_status
        if not UtilClient.is_unset(request.co_type):
            query['CoType'] = request.co_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChangeOrders',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/ListChangeOrders',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListChangeOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_change_orders_with_options_async(
        self,
        request: sae_20190506_models.ListChangeOrdersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListChangeOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.co_status):
            query['CoStatus'] = request.co_status
        if not UtilClient.is_unset(request.co_type):
            query['CoType'] = request.co_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChangeOrders',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/ListChangeOrders',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListChangeOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_change_orders(
        self,
        request: sae_20190506_models.ListChangeOrdersRequest,
    ) -> sae_20190506_models.ListChangeOrdersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_change_orders_with_options(request, headers, runtime)

    async def list_change_orders_async(
        self,
        request: sae_20190506_models.ListChangeOrdersRequest,
    ) -> sae_20190506_models.ListChangeOrdersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_change_orders_with_options_async(request, headers, runtime)

    def list_consumed_services_with_options(
        self,
        request: sae_20190506_models.ListConsumedServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListConsumedServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConsumedServices',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listConsumedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListConsumedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumed_services_with_options_async(
        self,
        request: sae_20190506_models.ListConsumedServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListConsumedServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConsumedServices',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listConsumedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListConsumedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumed_services(
        self,
        request: sae_20190506_models.ListConsumedServicesRequest,
    ) -> sae_20190506_models.ListConsumedServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumed_services_with_options(request, headers, runtime)

    async def list_consumed_services_async(
        self,
        request: sae_20190506_models.ListConsumedServicesRequest,
    ) -> sae_20190506_models.ListConsumedServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_consumed_services_with_options_async(request, headers, runtime)

    def list_grey_tag_route_with_options(
        self,
        request: sae_20190506_models.ListGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListGreyTagRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRouteList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_grey_tag_route_with_options_async(
        self,
        request: sae_20190506_models.ListGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListGreyTagRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRouteList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_grey_tag_route(
        self,
        request: sae_20190506_models.ListGreyTagRouteRequest,
    ) -> sae_20190506_models.ListGreyTagRouteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_grey_tag_route_with_options(request, headers, runtime)

    async def list_grey_tag_route_async(
        self,
        request: sae_20190506_models.ListGreyTagRouteRequest,
    ) -> sae_20190506_models.ListGreyTagRouteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_grey_tag_route_with_options_async(request, headers, runtime)

    def list_ingresses_with_options(
        self,
        request: sae_20190506_models.ListIngressesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListIngressesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIngresses',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/IngressList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListIngressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ingresses_with_options_async(
        self,
        request: sae_20190506_models.ListIngressesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListIngressesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIngresses',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/IngressList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListIngressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ingresses(
        self,
        request: sae_20190506_models.ListIngressesRequest,
    ) -> sae_20190506_models.ListIngressesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ingresses_with_options(request, headers, runtime)

    async def list_ingresses_async(
        self,
        request: sae_20190506_models.ListIngressesRequest,
    ) -> sae_20190506_models.ListIngressesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ingresses_with_options_async(request, headers, runtime)

    def list_jobs_with_options(
        self,
        request: sae_20190506_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_type):
            query['FieldType'] = request.field_type
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/listJobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: sae_20190506_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.field_type):
            query['FieldType'] = request.field_type
        if not UtilClient.is_unset(request.field_value):
            query['FieldValue'] = request.field_value
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.workload):
            query['Workload'] = request.workload
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/listJobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: sae_20190506_models.ListJobsRequest,
    ) -> sae_20190506_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(request, headers, runtime)

    async def list_jobs_async(
        self,
        request: sae_20190506_models.ListJobsRequest,
    ) -> sae_20190506_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(request, headers, runtime)

    def list_log_configs_with_options(
        self,
        request: sae_20190506_models.ListLogConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListLogConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogConfigs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/log/listLogConfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListLogConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_log_configs_with_options_async(
        self,
        request: sae_20190506_models.ListLogConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListLogConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogConfigs',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/log/listLogConfigs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListLogConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_log_configs(
        self,
        request: sae_20190506_models.ListLogConfigsRequest,
    ) -> sae_20190506_models.ListLogConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_log_configs_with_options(request, headers, runtime)

    async def list_log_configs_async(
        self,
        request: sae_20190506_models.ListLogConfigsRequest,
    ) -> sae_20190506_models.ListLogConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_log_configs_with_options_async(request, headers, runtime)

    def list_namespace_change_orders_with_options(
        self,
        request: sae_20190506_models.ListNamespaceChangeOrdersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListNamespaceChangeOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.co_status):
            query['CoStatus'] = request.co_status
        if not UtilClient.is_unset(request.co_type):
            query['CoType'] = request.co_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaceChangeOrders',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/listNamespaceChangeOrders',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListNamespaceChangeOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespace_change_orders_with_options_async(
        self,
        request: sae_20190506_models.ListNamespaceChangeOrdersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListNamespaceChangeOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.co_status):
            query['CoStatus'] = request.co_status
        if not UtilClient.is_unset(request.co_type):
            query['CoType'] = request.co_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaceChangeOrders',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/changeorder/listNamespaceChangeOrders',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListNamespaceChangeOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespace_change_orders(
        self,
        request: sae_20190506_models.ListNamespaceChangeOrdersRequest,
    ) -> sae_20190506_models.ListNamespaceChangeOrdersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_namespace_change_orders_with_options(request, headers, runtime)

    async def list_namespace_change_orders_async(
        self,
        request: sae_20190506_models.ListNamespaceChangeOrdersRequest,
    ) -> sae_20190506_models.ListNamespaceChangeOrdersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_namespace_change_orders_with_options_async(request, headers, runtime)

    def list_namespaced_config_maps_with_options(
        self,
        request: sae_20190506_models.ListNamespacedConfigMapsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListNamespacedConfigMapsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespacedConfigMaps',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/listNamespacedConfigMaps',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListNamespacedConfigMapsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespaced_config_maps_with_options_async(
        self,
        request: sae_20190506_models.ListNamespacedConfigMapsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListNamespacedConfigMapsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespacedConfigMaps',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/listNamespacedConfigMaps',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListNamespacedConfigMapsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespaced_config_maps(
        self,
        request: sae_20190506_models.ListNamespacedConfigMapsRequest,
    ) -> sae_20190506_models.ListNamespacedConfigMapsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_namespaced_config_maps_with_options(request, headers, runtime)

    async def list_namespaced_config_maps_async(
        self,
        request: sae_20190506_models.ListNamespacedConfigMapsRequest,
    ) -> sae_20190506_models.ListNamespacedConfigMapsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_namespaced_config_maps_with_options_async(request, headers, runtime)

    def list_published_services_with_options(
        self,
        request: sae_20190506_models.ListPublishedServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListPublishedServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedServices',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listPublishedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListPublishedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_published_services_with_options_async(
        self,
        request: sae_20190506_models.ListPublishedServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListPublishedServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedServices',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/service/listPublishedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListPublishedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_published_services(
        self,
        request: sae_20190506_models.ListPublishedServicesRequest,
    ) -> sae_20190506_models.ListPublishedServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_published_services_with_options(request, headers, runtime)

    async def list_published_services_async(
        self,
        request: sae_20190506_models.ListPublishedServicesRequest,
    ) -> sae_20190506_models.ListPublishedServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_published_services_with_options_async(request, headers, runtime)

    def list_secrets_with_options(
        self,
        request: sae_20190506_models.ListSecretsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListSecretsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecrets',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secrets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secrets_with_options_async(
        self,
        request: sae_20190506_models.ListSecretsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListSecretsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSecrets',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secrets',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secrets(
        self,
        request: sae_20190506_models.ListSecretsRequest,
    ) -> sae_20190506_models.ListSecretsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_secrets_with_options(request, headers, runtime)

    async def list_secrets_async(
        self,
        request: sae_20190506_models.ListSecretsRequest,
    ) -> sae_20190506_models.ListSecretsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_secrets_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        request: sae_20190506_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: sae_20190506_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: sae_20190506_models.ListTagResourcesRequest,
    ) -> sae_20190506_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: sae_20190506_models.ListTagResourcesRequest,
    ) -> sae_20190506_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def open_sae_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.OpenSaeServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OpenSaeService',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/service/open',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.OpenSaeServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_sae_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.OpenSaeServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OpenSaeService',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/service/open',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.OpenSaeServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_sae_service(self) -> sae_20190506_models.OpenSaeServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_sae_service_with_options(headers, runtime)

    async def open_sae_service_async(self) -> sae_20190506_models.OpenSaeServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.open_sae_service_with_options_async(headers, runtime)

    def query_resource_statics_with_options(
        self,
        request: sae_20190506_models.QueryResourceStaticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.QueryResourceStaticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResourceStatics',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/quota/queryResourceStatics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.QueryResourceStaticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_resource_statics_with_options_async(
        self,
        request: sae_20190506_models.QueryResourceStaticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.QueryResourceStaticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResourceStatics',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/quota/queryResourceStatics',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.QueryResourceStaticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_resource_statics(
        self,
        request: sae_20190506_models.QueryResourceStaticsRequest,
    ) -> sae_20190506_models.QueryResourceStaticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_resource_statics_with_options(request, headers, runtime)

    async def query_resource_statics_async(
        self,
        request: sae_20190506_models.QueryResourceStaticsRequest,
    ) -> sae_20190506_models.QueryResourceStaticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_resource_statics_with_options_async(request, headers, runtime)

    def reduce_application_capacity_by_instance_ids_with_options(
        self,
        request: sae_20190506_models.ReduceApplicationCapacityByInstanceIdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReduceApplicationCapacityByInstanceIds',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/ScaleInApplicationWithInstanceIds',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def reduce_application_capacity_by_instance_ids_with_options_async(
        self,
        request: sae_20190506_models.ReduceApplicationCapacityByInstanceIdsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReduceApplicationCapacityByInstanceIds',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/ScaleInApplicationWithInstanceIds',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reduce_application_capacity_by_instance_ids(
        self,
        request: sae_20190506_models.ReduceApplicationCapacityByInstanceIdsRequest,
    ) -> sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reduce_application_capacity_by_instance_ids_with_options(request, headers, runtime)

    async def reduce_application_capacity_by_instance_ids_async(
        self,
        request: sae_20190506_models.ReduceApplicationCapacityByInstanceIdsRequest,
    ) -> sae_20190506_models.ReduceApplicationCapacityByInstanceIdsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reduce_application_capacity_by_instance_ids_with_options_async(request, headers, runtime)

    def rescale_application_with_options(
        self,
        request: sae_20190506_models.RescaleApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RescaleApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RescaleApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/rescaleApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RescaleApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def rescale_application_with_options_async(
        self,
        request: sae_20190506_models.RescaleApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RescaleApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RescaleApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/rescaleApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RescaleApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rescale_application(
        self,
        request: sae_20190506_models.RescaleApplicationRequest,
    ) -> sae_20190506_models.RescaleApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rescale_application_with_options(request, headers, runtime)

    async def rescale_application_async(
        self,
        request: sae_20190506_models.RescaleApplicationRequest,
    ) -> sae_20190506_models.RescaleApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rescale_application_with_options_async(request, headers, runtime)

    def rescale_application_vertically_with_options(
        self,
        request: sae_20190506_models.RescaleApplicationVerticallyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RescaleApplicationVerticallyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RescaleApplicationVertically',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/rescaleApplicationVertically',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RescaleApplicationVerticallyResponse(),
            self.call_api(params, req, runtime)
        )

    async def rescale_application_vertically_with_options_async(
        self,
        request: sae_20190506_models.RescaleApplicationVerticallyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RescaleApplicationVerticallyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RescaleApplicationVertically',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/rescaleApplicationVertically',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RescaleApplicationVerticallyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rescale_application_vertically(
        self,
        request: sae_20190506_models.RescaleApplicationVerticallyRequest,
    ) -> sae_20190506_models.RescaleApplicationVerticallyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rescale_application_vertically_with_options(request, headers, runtime)

    async def rescale_application_vertically_async(
        self,
        request: sae_20190506_models.RescaleApplicationVerticallyRequest,
    ) -> sae_20190506_models.RescaleApplicationVerticallyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rescale_application_vertically_with_options_async(request, headers, runtime)

    def restart_application_with_options(
        self,
        request: sae_20190506_models.RestartApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RestartApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/restartApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RestartApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_application_with_options_async(
        self,
        request: sae_20190506_models.RestartApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RestartApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/restartApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RestartApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_application(
        self,
        request: sae_20190506_models.RestartApplicationRequest,
    ) -> sae_20190506_models.RestartApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_application_with_options(request, headers, runtime)

    async def restart_application_async(
        self,
        request: sae_20190506_models.RestartApplicationRequest,
    ) -> sae_20190506_models.RestartApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_application_with_options_async(request, headers, runtime)

    def restart_instances_with_options(
        self,
        request: sae_20190506_models.RestartInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RestartInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstances',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/restartInstances',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RestartInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instances_with_options_async(
        self,
        request: sae_20190506_models.RestartInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RestartInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstances',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/restartInstances',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RestartInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instances(
        self,
        request: sae_20190506_models.RestartInstancesRequest,
    ) -> sae_20190506_models.RestartInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_instances_with_options(request, headers, runtime)

    async def restart_instances_async(
        self,
        request: sae_20190506_models.RestartInstancesRequest,
    ) -> sae_20190506_models.RestartInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_instances_with_options_async(request, headers, runtime)

    def rollback_application_with_options(
        self,
        request: sae_20190506_models.RollbackApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RollbackApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/rollbackApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RollbackApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_application_with_options_async(
        self,
        request: sae_20190506_models.RollbackApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.RollbackApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_enable_application_scaling_rule):
            query['AutoEnableApplicationScalingRule'] = request.auto_enable_application_scaling_rule
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/rollbackApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.RollbackApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_application(
        self,
        request: sae_20190506_models.RollbackApplicationRequest,
    ) -> sae_20190506_models.RollbackApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rollback_application_with_options(request, headers, runtime)

    async def rollback_application_async(
        self,
        request: sae_20190506_models.RollbackApplicationRequest,
    ) -> sae_20190506_models.RollbackApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rollback_application_with_options_async(request, headers, runtime)

    def start_application_with_options(
        self,
        request: sae_20190506_models.StartApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.StartApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/startApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StartApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_application_with_options_async(
        self,
        request: sae_20190506_models.StartApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.StartApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/startApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StartApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_application(
        self,
        request: sae_20190506_models.StartApplicationRequest,
    ) -> sae_20190506_models.StartApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_application_with_options(request, headers, runtime)

    async def start_application_async(
        self,
        request: sae_20190506_models.StartApplicationRequest,
    ) -> sae_20190506_models.StartApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_application_with_options_async(request, headers, runtime)

    def stop_application_with_options(
        self,
        request: sae_20190506_models.StopApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.StopApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/stopApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StopApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_application_with_options_async(
        self,
        request: sae_20190506_models.StopApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.StopApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopApplication',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/stopApplication',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.StopApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_application(
        self,
        request: sae_20190506_models.StopApplicationRequest,
    ) -> sae_20190506_models.StopApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_application_with_options(request, headers, runtime)

    async def stop_application_async(
        self,
        request: sae_20190506_models.StopApplicationRequest,
    ) -> sae_20190506_models.StopApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_application_with_options_async(request, headers, runtime)

    def suspend_job_with_options(
        self,
        request: sae_20190506_models.SuspendJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.SuspendJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.suspend):
            query['Suspend'] = request.suspend
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/suspendJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.SuspendJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_job_with_options_async(
        self,
        request: sae_20190506_models.SuspendJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.SuspendJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.suspend):
            query['Suspend'] = request.suspend
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/suspendJob',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.SuspendJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_job(
        self,
        request: sae_20190506_models.SuspendJobRequest,
    ) -> sae_20190506_models.SuspendJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.suspend_job_with_options(request, headers, runtime)

    async def suspend_job_async(
        self,
        request: sae_20190506_models.SuspendJobRequest,
    ) -> sae_20190506_models.SuspendJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.suspend_job_with_options_async(request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: sae_20190506_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: sae_20190506_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: sae_20190506_models.TagResourcesRequest,
    ) -> sae_20190506_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: sae_20190506_models.TagResourcesRequest,
    ) -> sae_20190506_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def unbind_slb_with_options(
        self,
        request: sae_20190506_models.UnbindSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UnbindSlbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.internet):
            query['Internet'] = request.internet
        if not UtilClient.is_unset(request.intranet):
            query['Intranet'] = request.intranet
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSlb',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/slb',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UnbindSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_slb_with_options_async(
        self,
        request: sae_20190506_models.UnbindSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UnbindSlbResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.internet):
            query['Internet'] = request.internet
        if not UtilClient.is_unset(request.intranet):
            query['Intranet'] = request.intranet
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSlb',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/slb',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UnbindSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_slb(
        self,
        request: sae_20190506_models.UnbindSlbRequest,
    ) -> sae_20190506_models.UnbindSlbResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_slb_with_options(request, headers, runtime)

    async def unbind_slb_async(
        self,
        request: sae_20190506_models.UnbindSlbRequest,
    ) -> sae_20190506_models.UnbindSlbResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.unbind_slb_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        request: sae_20190506_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: sae_20190506_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: sae_20190506_models.UntagResourcesRequest,
    ) -> sae_20190506_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: sae_20190506_models.UntagResourcesRequest,
    ) -> sae_20190506_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_app_security_group_with_options(
        self,
        request: sae_20190506_models.UpdateAppSecurityGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateAppSecurityGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppSecurityGroup',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/updateAppSecurityGroup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateAppSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_security_group_with_options_async(
        self,
        request: sae_20190506_models.UpdateAppSecurityGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateAppSecurityGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppSecurityGroup',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/updateAppSecurityGroup',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateAppSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_security_group(
        self,
        request: sae_20190506_models.UpdateAppSecurityGroupRequest,
    ) -> sae_20190506_models.UpdateAppSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_security_group_with_options(request, headers, runtime)

    async def update_app_security_group_async(
        self,
        request: sae_20190506_models.UpdateAppSecurityGroupRequest,
    ) -> sae_20190506_models.UpdateAppSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_app_security_group_with_options_async(request, headers, runtime)

    def update_application_description_with_options(
        self,
        request: sae_20190506_models.UpdateApplicationDescriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateApplicationDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationDescription',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/updateAppDescription',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_description_with_options_async(
        self,
        request: sae_20190506_models.UpdateApplicationDescriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateApplicationDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_description):
            query['AppDescription'] = request.app_description
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationDescription',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/updateAppDescription',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_description(
        self,
        request: sae_20190506_models.UpdateApplicationDescriptionRequest,
    ) -> sae_20190506_models.UpdateApplicationDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_description_with_options(request, headers, runtime)

    async def update_application_description_async(
        self,
        request: sae_20190506_models.UpdateApplicationDescriptionRequest,
    ) -> sae_20190506_models.UpdateApplicationDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_application_description_with_options_async(request, headers, runtime)

    def update_application_scaling_rule_with_options(
        self,
        request: sae_20190506_models.UpdateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateApplicationScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_scaling_rule_with_options_async(
        self,
        request: sae_20190506_models.UpdateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateApplicationScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.min_ready_instance_ratio):
            query['MinReadyInstanceRatio'] = request.min_ready_instance_ratio
        if not UtilClient.is_unset(request.min_ready_instances):
            query['MinReadyInstances'] = request.min_ready_instances
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationScalingRule',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/scale/applicationScalingRule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_scaling_rule(
        self,
        request: sae_20190506_models.UpdateApplicationScalingRuleRequest,
    ) -> sae_20190506_models.UpdateApplicationScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_scaling_rule_with_options(request, headers, runtime)

    async def update_application_scaling_rule_async(
        self,
        request: sae_20190506_models.UpdateApplicationScalingRuleRequest,
    ) -> sae_20190506_models.UpdateApplicationScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_application_scaling_rule_with_options_async(request, headers, runtime)

    def update_application_vswitches_with_options(
        self,
        request: sae_20190506_models.UpdateApplicationVswitchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateApplicationVswitchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationVswitches',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/updateAppVswitches',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationVswitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_vswitches_with_options_async(
        self,
        request: sae_20190506_models.UpdateApplicationVswitchesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateApplicationVswitchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationVswitches',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/app/updateAppVswitches',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateApplicationVswitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_vswitches(
        self,
        request: sae_20190506_models.UpdateApplicationVswitchesRequest,
    ) -> sae_20190506_models.UpdateApplicationVswitchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_vswitches_with_options(request, headers, runtime)

    async def update_application_vswitches_async(
        self,
        request: sae_20190506_models.UpdateApplicationVswitchesRequest,
    ) -> sae_20190506_models.UpdateApplicationVswitchesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_application_vswitches_with_options_async(request, headers, runtime)

    def update_config_map_with_options(
        self,
        request: sae_20190506_models.UpdateConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateConfigMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_map_with_options_async(
        self,
        request: sae_20190506_models.UpdateConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateConfigMapResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_map_id):
            query['ConfigMapId'] = request.config_map_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigMap',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/configmap/configMap',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config_map(
        self,
        request: sae_20190506_models.UpdateConfigMapRequest,
    ) -> sae_20190506_models.UpdateConfigMapResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_config_map_with_options(request, headers, runtime)

    async def update_config_map_async(
        self,
        request: sae_20190506_models.UpdateConfigMapRequest,
    ) -> sae_20190506_models.UpdateConfigMapResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_config_map_with_options_async(request, headers, runtime)

    def update_grey_tag_route_with_options(
        self,
        request: sae_20190506_models.UpdateGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateGreyTagRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_rules):
            query['AlbRules'] = request.alb_rules
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        if not UtilClient.is_unset(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateGreyTagRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_grey_tag_route_with_options_async(
        self,
        request: sae_20190506_models.UpdateGreyTagRouteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateGreyTagRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_rules):
            query['AlbRules'] = request.alb_rules
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dubbo_rules):
            query['DubboRules'] = request.dubbo_rules
        if not UtilClient.is_unset(request.grey_tag_route_id):
            query['GreyTagRouteId'] = request.grey_tag_route_id
        if not UtilClient.is_unset(request.sc_rules):
            query['ScRules'] = request.sc_rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGreyTagRoute',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/tagroute/greyTagRoute',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateGreyTagRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_grey_tag_route(
        self,
        request: sae_20190506_models.UpdateGreyTagRouteRequest,
    ) -> sae_20190506_models.UpdateGreyTagRouteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_grey_tag_route_with_options(request, headers, runtime)

    async def update_grey_tag_route_async(
        self,
        request: sae_20190506_models.UpdateGreyTagRouteRequest,
    ) -> sae_20190506_models.UpdateGreyTagRouteResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_grey_tag_route_with_options_async(request, headers, runtime)

    def update_ingress_with_options(
        self,
        request: sae_20190506_models.UpdateIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateIngressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        body = {}
        if not UtilClient.is_unset(request.rules):
            body['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateIngressResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ingress_with_options_async(
        self,
        request: sae_20190506_models.UpdateIngressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateIngressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not UtilClient.is_unset(request.default_rule):
            query['DefaultRule'] = request.default_rule
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ingress_id):
            query['IngressId'] = request.ingress_id
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balance_type):
            query['LoadBalanceType'] = request.load_balance_type
        body = {}
        if not UtilClient.is_unset(request.rules):
            body['Rules'] = request.rules
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIngress',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/ingress/Ingress',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateIngressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ingress(
        self,
        request: sae_20190506_models.UpdateIngressRequest,
    ) -> sae_20190506_models.UpdateIngressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_ingress_with_options(request, headers, runtime)

    async def update_ingress_async(
        self,
        request: sae_20190506_models.UpdateIngressRequest,
    ) -> sae_20190506_models.UpdateIngressResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_ingress_with_options_async(request, headers, runtime)

    def update_job_with_options(
        self,
        request: sae_20190506_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.backoff_limit):
            query['BackoffLimit'] = request.backoff_limit
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.concurrency_policy):
            query['ConcurrencyPolicy'] = request.concurrency_policy
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.ref_app_id):
            query['RefAppId'] = request.ref_app_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.slice):
            query['Slice'] = request.slice
        if not UtilClient.is_unset(request.slice_envs):
            query['SliceEnvs'] = request.slice_envs
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.trigger_config):
            query['TriggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.enable_image_accl):
            body['EnableImageAccl'] = request.enable_image_accl
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php):
            body['Php'] = request.php
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/updateJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_with_options_async(
        self,
        request: sae_20190506_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_assume_role_arn):
            query['AcrAssumeRoleArn'] = request.acr_assume_role_arn
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.backoff_limit):
            query['BackoffLimit'] = request.backoff_limit
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.concurrency_policy):
            query['ConcurrencyPolicy'] = request.concurrency_policy
        if not UtilClient.is_unset(request.custom_host_alias):
            query['CustomHostAlias'] = request.custom_host_alias
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_pull_secrets):
            query['ImagePullSecrets'] = request.image_pull_secrets
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.jar_start_args):
            query['JarStartArgs'] = request.jar_start_args
        if not UtilClient.is_unset(request.jar_start_options):
            query['JarStartOptions'] = request.jar_start_options
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.mount_desc):
            query['MountDesc'] = request.mount_desc
        if not UtilClient.is_unset(request.mount_host):
            query['MountHost'] = request.mount_host
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.php_config_location):
            query['PhpConfigLocation'] = request.php_config_location
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.programming_language):
            query['ProgrammingLanguage'] = request.programming_language
        if not UtilClient.is_unset(request.python):
            query['Python'] = request.python
        if not UtilClient.is_unset(request.python_modules):
            query['PythonModules'] = request.python_modules
        if not UtilClient.is_unset(request.ref_app_id):
            query['RefAppId'] = request.ref_app_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.slice):
            query['Slice'] = request.slice
        if not UtilClient.is_unset(request.slice_envs):
            query['SliceEnvs'] = request.slice_envs
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timezone):
            query['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.tomcat_config):
            query['TomcatConfig'] = request.tomcat_config
        if not UtilClient.is_unset(request.trigger_config):
            query['TriggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.war_start_options):
            query['WarStartOptions'] = request.war_start_options
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        body = {}
        if not UtilClient.is_unset(request.acr_instance_id):
            body['AcrInstanceId'] = request.acr_instance_id
        if not UtilClient.is_unset(request.config_map_mount_desc):
            body['ConfigMapMountDesc'] = request.config_map_mount_desc
        if not UtilClient.is_unset(request.enable_image_accl):
            body['EnableImageAccl'] = request.enable_image_accl
        if not UtilClient.is_unset(request.oss_ak_id):
            body['OssAkId'] = request.oss_ak_id
        if not UtilClient.is_unset(request.oss_ak_secret):
            body['OssAkSecret'] = request.oss_ak_secret
        if not UtilClient.is_unset(request.oss_mount_descs):
            body['OssMountDescs'] = request.oss_mount_descs
        if not UtilClient.is_unset(request.php):
            body['Php'] = request.php
        if not UtilClient.is_unset(request.php_config):
            body['PhpConfig'] = request.php_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/job/updateJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job(
        self,
        request: sae_20190506_models.UpdateJobRequest,
    ) -> sae_20190506_models.UpdateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_job_with_options(request, headers, runtime)

    async def update_job_async(
        self,
        request: sae_20190506_models.UpdateJobRequest,
    ) -> sae_20190506_models.UpdateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_job_with_options_async(request, headers, runtime)

    def update_namespace_with_options(
        self,
        request: sae_20190506_models.UpdateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_with_options_async(
        self,
        request: sae_20190506_models.UpdateNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_description):
            query['NamespaceDescription'] = request.namespace_description
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespace',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/paas/namespace',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace(
        self,
        request: sae_20190506_models.UpdateNamespaceRequest,
    ) -> sae_20190506_models.UpdateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_namespace_with_options(request, headers, runtime)

    async def update_namespace_async(
        self,
        request: sae_20190506_models.UpdateNamespaceRequest,
    ) -> sae_20190506_models.UpdateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_namespace_with_options_async(request, headers, runtime)

    def update_namespace_vpc_with_options(
        self,
        request: sae_20190506_models.UpdateNamespaceVpcRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateNamespaceVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespaceVpc',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/namespace/updateNamespaceVpc',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateNamespaceVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_vpc_with_options_async(
        self,
        request: sae_20190506_models.UpdateNamespaceVpcRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateNamespaceVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_space_short_id):
            query['NameSpaceShortId'] = request.name_space_short_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNamespaceVpc',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/namespace/updateNamespaceVpc',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateNamespaceVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace_vpc(
        self,
        request: sae_20190506_models.UpdateNamespaceVpcRequest,
    ) -> sae_20190506_models.UpdateNamespaceVpcResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_namespace_vpc_with_options(request, headers, runtime)

    async def update_namespace_vpc_async(
        self,
        request: sae_20190506_models.UpdateNamespaceVpcRequest,
    ) -> sae_20190506_models.UpdateNamespaceVpcResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_namespace_vpc_with_options_async(request, headers, runtime)

    def update_secret_with_options(
        self,
        request: sae_20190506_models.UpdateSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        body = {}
        if not UtilClient.is_unset(request.secret_data):
            body['SecretData'] = request.secret_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_secret_with_options_async(
        self,
        request: sae_20190506_models.UpdateSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> sae_20190506_models.UpdateSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        body = {}
        if not UtilClient.is_unset(request.secret_data):
            body['SecretData'] = request.secret_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSecret',
            version='2019-05-06',
            protocol='HTTPS',
            pathname=f'/pop/v1/sam/secret/secret',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sae_20190506_models.UpdateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_secret(
        self,
        request: sae_20190506_models.UpdateSecretRequest,
    ) -> sae_20190506_models.UpdateSecretResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_secret_with_options(request, headers, runtime)

    async def update_secret_async(
        self,
        request: sae_20190506_models.UpdateSecretRequest,
    ) -> sae_20190506_models.UpdateSecretResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_secret_with_options_async(request, headers, runtime)
