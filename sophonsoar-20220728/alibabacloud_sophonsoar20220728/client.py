# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sophonsoar20220728 import models as sophonsoar_20220728_models
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
        self._endpoint = self.get_endpoint('sophonsoar', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_modify_instance_status_with_options(
        self,
        request: sophonsoar_20220728_models.BatchModifyInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.BatchModifyInstanceStatusResponse:
        """
        @summary Modifies the statuses of playbooks at a time.
        
        @param request: BatchModifyInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchModifyInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchModifyInstanceStatus',
            version='2022-07-28',
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
                sophonsoar_20220728_models.BatchModifyInstanceStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.BatchModifyInstanceStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def batch_modify_instance_status_with_options_async(
        self,
        request: sophonsoar_20220728_models.BatchModifyInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.BatchModifyInstanceStatusResponse:
        """
        @summary Modifies the statuses of playbooks at a time.
        
        @param request: BatchModifyInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchModifyInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchModifyInstanceStatus',
            version='2022-07-28',
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
                sophonsoar_20220728_models.BatchModifyInstanceStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.BatchModifyInstanceStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def batch_modify_instance_status(
        self,
        request: sophonsoar_20220728_models.BatchModifyInstanceStatusRequest,
    ) -> sophonsoar_20220728_models.BatchModifyInstanceStatusResponse:
        """
        @summary Modifies the statuses of playbooks at a time.
        
        @param request: BatchModifyInstanceStatusRequest
        @return: BatchModifyInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_modify_instance_status_with_options(request, runtime)

    async def batch_modify_instance_status_async(
        self,
        request: sophonsoar_20220728_models.BatchModifyInstanceStatusRequest,
    ) -> sophonsoar_20220728_models.BatchModifyInstanceStatusResponse:
        """
        @summary Modifies the statuses of playbooks at a time.
        
        @param request: BatchModifyInstanceStatusRequest
        @return: BatchModifyInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_modify_instance_status_with_options_async(request, runtime)

    def compare_playbooks_with_options(
        self,
        request: sophonsoar_20220728_models.ComparePlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ComparePlaybooksResponse:
        """
        @summary Compares configurations between two versions of a published playbook.
        
        @param request: ComparePlaybooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ComparePlaybooksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_playbook_release_id):
            query['NewPlaybookReleaseId'] = request.new_playbook_release_id
        if not UtilClient.is_unset(request.old_playbook_release_id):
            query['OldPlaybookReleaseId'] = request.old_playbook_release_id
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ComparePlaybooks',
            version='2022-07-28',
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
                sophonsoar_20220728_models.ComparePlaybooksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.ComparePlaybooksResponse(),
                self.execute(params, req, runtime)
            )

    async def compare_playbooks_with_options_async(
        self,
        request: sophonsoar_20220728_models.ComparePlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ComparePlaybooksResponse:
        """
        @summary Compares configurations between two versions of a published playbook.
        
        @param request: ComparePlaybooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ComparePlaybooksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_playbook_release_id):
            query['NewPlaybookReleaseId'] = request.new_playbook_release_id
        if not UtilClient.is_unset(request.old_playbook_release_id):
            query['OldPlaybookReleaseId'] = request.old_playbook_release_id
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ComparePlaybooks',
            version='2022-07-28',
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
                sophonsoar_20220728_models.ComparePlaybooksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.ComparePlaybooksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def compare_playbooks(
        self,
        request: sophonsoar_20220728_models.ComparePlaybooksRequest,
    ) -> sophonsoar_20220728_models.ComparePlaybooksResponse:
        """
        @summary Compares configurations between two versions of a published playbook.
        
        @param request: ComparePlaybooksRequest
        @return: ComparePlaybooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.compare_playbooks_with_options(request, runtime)

    async def compare_playbooks_async(
        self,
        request: sophonsoar_20220728_models.ComparePlaybooksRequest,
    ) -> sophonsoar_20220728_models.ComparePlaybooksResponse:
        """
        @summary Compares configurations between two versions of a published playbook.
        
        @param request: ComparePlaybooksRequest
        @return: ComparePlaybooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.compare_playbooks_with_options_async(request, runtime)

    def convert_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.ConvertPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ConvertPlaybookResponse:
        """
        @summary Convert XML configuration.
        
        @description Please ensure that you fully understand the billing method and [pricing](https://www.aliyun.com/price/product#/sas/detail/sas) of the orchestration product before using this interface.
        
        @param request: ConvertPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertPlaybookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.role_for):
            query['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        body = {}
        if not UtilClient.is_unset(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.ConvertPlaybookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.ConvertPlaybookResponse(),
                self.execute(params, req, runtime)
            )

    async def convert_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.ConvertPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ConvertPlaybookResponse:
        """
        @summary Convert XML configuration.
        
        @description Please ensure that you fully understand the billing method and [pricing](https://www.aliyun.com/price/product#/sas/detail/sas) of the orchestration product before using this interface.
        
        @param request: ConvertPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertPlaybookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.role_for):
            query['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        body = {}
        if not UtilClient.is_unset(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.ConvertPlaybookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.ConvertPlaybookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def convert_playbook(
        self,
        request: sophonsoar_20220728_models.ConvertPlaybookRequest,
    ) -> sophonsoar_20220728_models.ConvertPlaybookResponse:
        """
        @summary Convert XML configuration.
        
        @description Please ensure that you fully understand the billing method and [pricing](https://www.aliyun.com/price/product#/sas/detail/sas) of the orchestration product before using this interface.
        
        @param request: ConvertPlaybookRequest
        @return: ConvertPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.convert_playbook_with_options(request, runtime)

    async def convert_playbook_async(
        self,
        request: sophonsoar_20220728_models.ConvertPlaybookRequest,
    ) -> sophonsoar_20220728_models.ConvertPlaybookResponse:
        """
        @summary Convert XML configuration.
        
        @description Please ensure that you fully understand the billing method and [pricing](https://www.aliyun.com/price/product#/sas/detail/sas) of the orchestration product before using this interface.
        
        @param request: ConvertPlaybookRequest
        @return: ConvertPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.convert_playbook_with_options_async(request, runtime)

    def copy_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.CopyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.CopyPlaybookResponse:
        """
        @summary 剧本复制
        
        @param request: CopyPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyPlaybookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.role_for):
            query['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.release_version):
            body['ReleaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.source_playbook_uuid):
            body['SourcePlaybookUuid'] = request.source_playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.CopyPlaybookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.CopyPlaybookResponse(),
                self.execute(params, req, runtime)
            )

    async def copy_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.CopyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.CopyPlaybookResponse:
        """
        @summary 剧本复制
        
        @param request: CopyPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyPlaybookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.role_for):
            query['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.release_version):
            body['ReleaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.source_playbook_uuid):
            body['SourcePlaybookUuid'] = request.source_playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.CopyPlaybookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.CopyPlaybookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def copy_playbook(
        self,
        request: sophonsoar_20220728_models.CopyPlaybookRequest,
    ) -> sophonsoar_20220728_models.CopyPlaybookResponse:
        """
        @summary 剧本复制
        
        @param request: CopyPlaybookRequest
        @return: CopyPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_playbook_with_options(request, runtime)

    async def copy_playbook_async(
        self,
        request: sophonsoar_20220728_models.CopyPlaybookRequest,
    ) -> sophonsoar_20220728_models.CopyPlaybookResponse:
        """
        @summary 剧本复制
        
        @param request: CopyPlaybookRequest
        @return: CopyPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.copy_playbook_with_options_async(request, runtime)

    def create_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.CreatePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.CreatePlaybookResponse:
        """
        @summary New Playbook.
        
        @description Create Playbook.
        
        @param request: CreatePlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.taskflow_type):
            body['TaskflowType'] = request.taskflow_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.CreatePlaybookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.CreatePlaybookResponse(),
                self.execute(params, req, runtime)
            )

    async def create_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.CreatePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.CreatePlaybookResponse:
        """
        @summary New Playbook.
        
        @description Create Playbook.
        
        @param request: CreatePlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.taskflow_type):
            body['TaskflowType'] = request.taskflow_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.CreatePlaybookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.CreatePlaybookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_playbook(
        self,
        request: sophonsoar_20220728_models.CreatePlaybookRequest,
    ) -> sophonsoar_20220728_models.CreatePlaybookResponse:
        """
        @summary New Playbook.
        
        @description Create Playbook.
        
        @param request: CreatePlaybookRequest
        @return: CreatePlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_playbook_with_options(request, runtime)

    async def create_playbook_async(
        self,
        request: sophonsoar_20220728_models.CreatePlaybookRequest,
    ) -> sophonsoar_20220728_models.CreatePlaybookResponse:
        """
        @summary New Playbook.
        
        @description Create Playbook.
        
        @param request: CreatePlaybookRequest
        @return: CreatePlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_playbook_with_options_async(request, runtime)

    def debug_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.DebugPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DebugPlaybookResponse:
        """
        @summary Debugs a playbook.
        
        @param request: DebugPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DebugPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.record):
            body['Record'] = request.record
        if not UtilClient.is_unset(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DebugPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DebugPlaybookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DebugPlaybookResponse(),
                self.execute(params, req, runtime)
            )

    async def debug_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.DebugPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DebugPlaybookResponse:
        """
        @summary Debugs a playbook.
        
        @param request: DebugPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DebugPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.record):
            body['Record'] = request.record
        if not UtilClient.is_unset(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DebugPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DebugPlaybookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DebugPlaybookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def debug_playbook(
        self,
        request: sophonsoar_20220728_models.DebugPlaybookRequest,
    ) -> sophonsoar_20220728_models.DebugPlaybookResponse:
        """
        @summary Debugs a playbook.
        
        @param request: DebugPlaybookRequest
        @return: DebugPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.debug_playbook_with_options(request, runtime)

    async def debug_playbook_async(
        self,
        request: sophonsoar_20220728_models.DebugPlaybookRequest,
    ) -> sophonsoar_20220728_models.DebugPlaybookResponse:
        """
        @summary Debugs a playbook.
        
        @param request: DebugPlaybookRequest
        @return: DebugPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.debug_playbook_with_options_async(request, runtime)

    def delete_component_asset_with_options(
        self,
        request: sophonsoar_20220728_models.DeleteComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DeleteComponentAssetResponse:
        """
        @summary Deletes the assets in a component.
        
        @param request: DeleteComponentAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteComponentAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteComponentAsset',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DeleteComponentAssetResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DeleteComponentAssetResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_component_asset_with_options_async(
        self,
        request: sophonsoar_20220728_models.DeleteComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DeleteComponentAssetResponse:
        """
        @summary Deletes the assets in a component.
        
        @param request: DeleteComponentAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteComponentAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteComponentAsset',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DeleteComponentAssetResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DeleteComponentAssetResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_component_asset(
        self,
        request: sophonsoar_20220728_models.DeleteComponentAssetRequest,
    ) -> sophonsoar_20220728_models.DeleteComponentAssetResponse:
        """
        @summary Deletes the assets in a component.
        
        @param request: DeleteComponentAssetRequest
        @return: DeleteComponentAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_component_asset_with_options(request, runtime)

    async def delete_component_asset_async(
        self,
        request: sophonsoar_20220728_models.DeleteComponentAssetRequest,
    ) -> sophonsoar_20220728_models.DeleteComponentAssetResponse:
        """
        @summary Deletes the assets in a component.
        
        @param request: DeleteComponentAssetRequest
        @return: DeleteComponentAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_component_asset_with_options_async(request, runtime)

    def delete_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.DeletePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DeletePlaybookResponse:
        """
        @summary Deletes a custom playbook.
        
        @param request: DeletePlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DeletePlaybookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DeletePlaybookResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.DeletePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DeletePlaybookResponse:
        """
        @summary Deletes a custom playbook.
        
        @param request: DeletePlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DeletePlaybookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DeletePlaybookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_playbook(
        self,
        request: sophonsoar_20220728_models.DeletePlaybookRequest,
    ) -> sophonsoar_20220728_models.DeletePlaybookResponse:
        """
        @summary Deletes a custom playbook.
        
        @param request: DeletePlaybookRequest
        @return: DeletePlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_playbook_with_options(request, runtime)

    async def delete_playbook_async(
        self,
        request: sophonsoar_20220728_models.DeletePlaybookRequest,
    ) -> sophonsoar_20220728_models.DeletePlaybookResponse:
        """
        @summary Deletes a custom playbook.
        
        @param request: DeletePlaybookRequest
        @return: DeletePlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_playbook_with_options_async(request, runtime)

    def describe_component_asset_form_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetFormResponse:
        """
        @summary Queries the metadata of assets in a component. The metadata of an asset refers to the fields that describe the asset.
        
        @param request: DescribeComponentAssetFormRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentAssetFormResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentAssetForm',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeComponentAssetFormResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeComponentAssetFormResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_component_asset_form_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetFormResponse:
        """
        @summary Queries the metadata of assets in a component. The metadata of an asset refers to the fields that describe the asset.
        
        @param request: DescribeComponentAssetFormRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentAssetFormResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentAssetForm',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeComponentAssetFormResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeComponentAssetFormResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_component_asset_form(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetFormRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetFormResponse:
        """
        @summary Queries the metadata of assets in a component. The metadata of an asset refers to the fields that describe the asset.
        
        @param request: DescribeComponentAssetFormRequest
        @return: DescribeComponentAssetFormResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_component_asset_form_with_options(request, runtime)

    async def describe_component_asset_form_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetFormRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetFormResponse:
        """
        @summary Queries the metadata of assets in a component. The metadata of an asset refers to the fields that describe the asset.
        
        @param request: DescribeComponentAssetFormRequest
        @return: DescribeComponentAssetFormResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_component_asset_form_with_options_async(request, runtime)

    def describe_component_assets_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetsResponse:
        """
        @summary Queries a list of assets in a component.
        
        @param request: DescribeComponentAssetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentAssetsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentAssets',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeComponentAssetsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeComponentAssetsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_component_assets_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetsResponse:
        """
        @summary Queries a list of assets in a component.
        
        @param request: DescribeComponentAssetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentAssetsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentAssets',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeComponentAssetsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeComponentAssetsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_component_assets(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetsRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetsResponse:
        """
        @summary Queries a list of assets in a component.
        
        @param request: DescribeComponentAssetsRequest
        @return: DescribeComponentAssetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_component_assets_with_options(request, runtime)

    async def describe_component_assets_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentAssetsRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentAssetsResponse:
        """
        @summary Queries a list of assets in a component.
        
        @param request: DescribeComponentAssetsRequest
        @return: DescribeComponentAssetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_component_assets_with_options_async(request, runtime)

    def describe_component_list_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeComponentListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentListResponse:
        """
        @summary Queries a list of common components that are available.
        
        @param request: DescribeComponentListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentList',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeComponentListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeComponentListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_component_list_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentListResponse:
        """
        @summary Queries a list of common components that are available.
        
        @param request: DescribeComponentListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentList',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeComponentListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeComponentListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_component_list(
        self,
        request: sophonsoar_20220728_models.DescribeComponentListRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentListResponse:
        """
        @summary Queries a list of common components that are available.
        
        @param request: DescribeComponentListRequest
        @return: DescribeComponentListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_component_list_with_options(request, runtime)

    async def describe_component_list_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentListRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentListResponse:
        """
        @summary Queries a list of common components that are available.
        
        @param request: DescribeComponentListRequest
        @return: DescribeComponentListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_component_list_with_options_async(request, runtime)

    def describe_component_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeComponentPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentPlaybookResponse:
        """
        @summary Queries a list of predefined components that are available.
        
        @param request: DescribeComponentPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentPlaybookResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeComponentPlaybookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeComponentPlaybookResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_component_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentPlaybookResponse:
        """
        @summary Queries a list of predefined components that are available.
        
        @param request: DescribeComponentPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentPlaybookResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeComponentPlaybookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeComponentPlaybookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_component_playbook(
        self,
        request: sophonsoar_20220728_models.DescribeComponentPlaybookRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentPlaybookResponse:
        """
        @summary Queries a list of predefined components that are available.
        
        @param request: DescribeComponentPlaybookRequest
        @return: DescribeComponentPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_component_playbook_with_options(request, runtime)

    async def describe_component_playbook_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentPlaybookRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentPlaybookResponse:
        """
        @summary Queries a list of predefined components that are available.
        
        @param request: DescribeComponentPlaybookRequest
        @return: DescribeComponentPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_component_playbook_with_options_async(request, runtime)

    def describe_components_js_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeComponentsJsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentsJsResponse:
        """
        @summary Queries the JavaScript file of a component. The component uses the returned JavaScript file for page rendering.
        
        @param request: DescribeComponentsJsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentsJsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentsJs',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeComponentsJsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeComponentsJsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_components_js_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentsJsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeComponentsJsResponse:
        """
        @summary Queries the JavaScript file of a component. The component uses the returned JavaScript file for page rendering.
        
        @param request: DescribeComponentsJsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeComponentsJsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComponentsJs',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeComponentsJsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeComponentsJsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_components_js(
        self,
        request: sophonsoar_20220728_models.DescribeComponentsJsRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentsJsResponse:
        """
        @summary Queries the JavaScript file of a component. The component uses the returned JavaScript file for page rendering.
        
        @param request: DescribeComponentsJsRequest
        @return: DescribeComponentsJsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_components_js_with_options(request, runtime)

    async def describe_components_js_async(
        self,
        request: sophonsoar_20220728_models.DescribeComponentsJsRequest,
    ) -> sophonsoar_20220728_models.DescribeComponentsJsResponse:
        """
        @summary Queries the JavaScript file of a component. The component uses the returned JavaScript file for page rendering.
        
        @param request: DescribeComponentsJsRequest
        @return: DescribeComponentsJsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_components_js_with_options_async(request, runtime)

    def describe_distinct_releases_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeDistinctReleasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeDistinctReleasesResponse:
        """
        @summary Queries the information about the published versions of a playbook after deduplication.
        
        @param request: DescribeDistinctReleasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDistinctReleasesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDistinctReleases',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeDistinctReleasesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeDistinctReleasesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_distinct_releases_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeDistinctReleasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeDistinctReleasesResponse:
        """
        @summary Queries the information about the published versions of a playbook after deduplication.
        
        @param request: DescribeDistinctReleasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDistinctReleasesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDistinctReleases',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeDistinctReleasesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeDistinctReleasesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_distinct_releases(
        self,
        request: sophonsoar_20220728_models.DescribeDistinctReleasesRequest,
    ) -> sophonsoar_20220728_models.DescribeDistinctReleasesResponse:
        """
        @summary Queries the information about the published versions of a playbook after deduplication.
        
        @param request: DescribeDistinctReleasesRequest
        @return: DescribeDistinctReleasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_distinct_releases_with_options(request, runtime)

    async def describe_distinct_releases_async(
        self,
        request: sophonsoar_20220728_models.DescribeDistinctReleasesRequest,
    ) -> sophonsoar_20220728_models.DescribeDistinctReleasesResponse:
        """
        @summary Queries the information about the published versions of a playbook after deduplication.
        
        @param request: DescribeDistinctReleasesRequest
        @return: DescribeDistinctReleasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_distinct_releases_with_options_async(request, runtime)

    def describe_enum_items_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeEnumItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeEnumItemsResponse:
        """
        @summary Queries enumeration items that are required by a cloud service.
        
        @param request: DescribeEnumItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEnumItemsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnumItems',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeEnumItemsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeEnumItemsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_enum_items_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeEnumItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeEnumItemsResponse:
        """
        @summary Queries enumeration items that are required by a cloud service.
        
        @param request: DescribeEnumItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEnumItemsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnumItems',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeEnumItemsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeEnumItemsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_enum_items(
        self,
        request: sophonsoar_20220728_models.DescribeEnumItemsRequest,
    ) -> sophonsoar_20220728_models.DescribeEnumItemsResponse:
        """
        @summary Queries enumeration items that are required by a cloud service.
        
        @param request: DescribeEnumItemsRequest
        @return: DescribeEnumItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_enum_items_with_options(request, runtime)

    async def describe_enum_items_async(
        self,
        request: sophonsoar_20220728_models.DescribeEnumItemsRequest,
    ) -> sophonsoar_20220728_models.DescribeEnumItemsResponse:
        """
        @summary Queries enumeration items that are required by a cloud service.
        
        @param request: DescribeEnumItemsRequest
        @return: DescribeEnumItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_enum_items_with_options_async(request, runtime)

    def describe_execute_playbooks_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeExecutePlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeExecutePlaybooksResponse:
        """
        @summary Queries the playbooks that are available for an automatic response plan.
        
        @param request: DescribeExecutePlaybooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExecutePlaybooksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExecutePlaybooks',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeExecutePlaybooksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeExecutePlaybooksResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_execute_playbooks_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeExecutePlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeExecutePlaybooksResponse:
        """
        @summary Queries the playbooks that are available for an automatic response plan.
        
        @param request: DescribeExecutePlaybooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExecutePlaybooksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExecutePlaybooks',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeExecutePlaybooksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeExecutePlaybooksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_execute_playbooks(
        self,
        request: sophonsoar_20220728_models.DescribeExecutePlaybooksRequest,
    ) -> sophonsoar_20220728_models.DescribeExecutePlaybooksResponse:
        """
        @summary Queries the playbooks that are available for an automatic response plan.
        
        @param request: DescribeExecutePlaybooksRequest
        @return: DescribeExecutePlaybooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_execute_playbooks_with_options(request, runtime)

    async def describe_execute_playbooks_async(
        self,
        request: sophonsoar_20220728_models.DescribeExecutePlaybooksRequest,
    ) -> sophonsoar_20220728_models.DescribeExecutePlaybooksResponse:
        """
        @summary Queries the playbooks that are available for an automatic response plan.
        
        @param request: DescribeExecutePlaybooksRequest
        @return: DescribeExecutePlaybooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_execute_playbooks_with_options_async(request, runtime)

    def describe_field_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeFieldResponse:
        """
        @summary Queries the global configuration information about a cloud service.
        
        @param request: DescribeFieldRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFieldResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeField',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeFieldResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeFieldResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_field_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeFieldResponse:
        """
        @summary Queries the global configuration information about a cloud service.
        
        @param request: DescribeFieldRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFieldResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeField',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeFieldResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeFieldResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_field(
        self,
        request: sophonsoar_20220728_models.DescribeFieldRequest,
    ) -> sophonsoar_20220728_models.DescribeFieldResponse:
        """
        @summary Queries the global configuration information about a cloud service.
        
        @param request: DescribeFieldRequest
        @return: DescribeFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_field_with_options(request, runtime)

    async def describe_field_async(
        self,
        request: sophonsoar_20220728_models.DescribeFieldRequest,
    ) -> sophonsoar_20220728_models.DescribeFieldResponse:
        """
        @summary Queries the global configuration information about a cloud service.
        
        @param request: DescribeFieldRequest
        @return: DescribeFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_field_with_options_async(request, runtime)

    def describe_group_productions_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeGroupProductionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeGroupProductionsResponse:
        """
        @summary 获取OpenAPI的产品列表
        
        @param request: DescribeGroupProductionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGroupProductionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupProductions',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeGroupProductionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeGroupProductionsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_group_productions_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeGroupProductionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeGroupProductionsResponse:
        """
        @summary 获取OpenAPI的产品列表
        
        @param request: DescribeGroupProductionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGroupProductionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupProductions',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeGroupProductionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeGroupProductionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_group_productions(
        self,
        request: sophonsoar_20220728_models.DescribeGroupProductionsRequest,
    ) -> sophonsoar_20220728_models.DescribeGroupProductionsResponse:
        """
        @summary 获取OpenAPI的产品列表
        
        @param request: DescribeGroupProductionsRequest
        @return: DescribeGroupProductionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_group_productions_with_options(request, runtime)

    async def describe_group_productions_async(
        self,
        request: sophonsoar_20220728_models.DescribeGroupProductionsRequest,
    ) -> sophonsoar_20220728_models.DescribeGroupProductionsResponse:
        """
        @summary 获取OpenAPI的产品列表
        
        @param request: DescribeGroupProductionsRequest
        @return: DescribeGroupProductionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_group_productions_with_options_async(request, runtime)

    def describe_latest_record_schema_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeLatestRecordSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse:
        """
        @summary Queries the output structure information of each node in a playbook based on the most recent running record of the playbook.
        
        @param request: DescribeLatestRecordSchemaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLatestRecordSchemaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLatestRecordSchema',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_latest_record_schema_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeLatestRecordSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse:
        """
        @summary Queries the output structure information of each node in a playbook based on the most recent running record of the playbook.
        
        @param request: DescribeLatestRecordSchemaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLatestRecordSchemaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLatestRecordSchema',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_latest_record_schema(
        self,
        request: sophonsoar_20220728_models.DescribeLatestRecordSchemaRequest,
    ) -> sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse:
        """
        @summary Queries the output structure information of each node in a playbook based on the most recent running record of the playbook.
        
        @param request: DescribeLatestRecordSchemaRequest
        @return: DescribeLatestRecordSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_latest_record_schema_with_options(request, runtime)

    async def describe_latest_record_schema_async(
        self,
        request: sophonsoar_20220728_models.DescribeLatestRecordSchemaRequest,
    ) -> sophonsoar_20220728_models.DescribeLatestRecordSchemaResponse:
        """
        @summary Queries the output structure information of each node in a playbook based on the most recent running record of the playbook.
        
        @param request: DescribeLatestRecordSchemaRequest
        @return: DescribeLatestRecordSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_latest_record_schema_with_options_async(request, runtime)

    def describe_node_param_tags_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeNodeParamTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeNodeParamTagsResponse:
        """
        @summary Queries recommended dynamic input parameters of a component for playbook orchestration.
        
        @param request: DescribeNodeParamTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeParamTagsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeParamTags',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeNodeParamTagsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeNodeParamTagsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_node_param_tags_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeNodeParamTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeNodeParamTagsResponse:
        """
        @summary Queries recommended dynamic input parameters of a component for playbook orchestration.
        
        @param request: DescribeNodeParamTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeParamTagsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeParamTags',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeNodeParamTagsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeNodeParamTagsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_node_param_tags(
        self,
        request: sophonsoar_20220728_models.DescribeNodeParamTagsRequest,
    ) -> sophonsoar_20220728_models.DescribeNodeParamTagsResponse:
        """
        @summary Queries recommended dynamic input parameters of a component for playbook orchestration.
        
        @param request: DescribeNodeParamTagsRequest
        @return: DescribeNodeParamTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_node_param_tags_with_options(request, runtime)

    async def describe_node_param_tags_async(
        self,
        request: sophonsoar_20220728_models.DescribeNodeParamTagsRequest,
    ) -> sophonsoar_20220728_models.DescribeNodeParamTagsResponse:
        """
        @summary Queries recommended dynamic input parameters of a component for playbook orchestration.
        
        @param request: DescribeNodeParamTagsRequest
        @return: DescribeNodeParamTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_param_tags_with_options_async(request, runtime)

    def describe_node_used_infos_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeNodeUsedInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeNodeUsedInfosResponse:
        """
        @summary Queries the nodes that reference the same node in a playbook.
        
        @param request: DescribeNodeUsedInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeUsedInfosResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeUsedInfos',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeNodeUsedInfosResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeNodeUsedInfosResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_node_used_infos_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeNodeUsedInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeNodeUsedInfosResponse:
        """
        @summary Queries the nodes that reference the same node in a playbook.
        
        @param request: DescribeNodeUsedInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeUsedInfosResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeUsedInfos',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeNodeUsedInfosResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeNodeUsedInfosResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_node_used_infos(
        self,
        request: sophonsoar_20220728_models.DescribeNodeUsedInfosRequest,
    ) -> sophonsoar_20220728_models.DescribeNodeUsedInfosResponse:
        """
        @summary Queries the nodes that reference the same node in a playbook.
        
        @param request: DescribeNodeUsedInfosRequest
        @return: DescribeNodeUsedInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_node_used_infos_with_options(request, runtime)

    async def describe_node_used_infos_async(
        self,
        request: sophonsoar_20220728_models.DescribeNodeUsedInfosRequest,
    ) -> sophonsoar_20220728_models.DescribeNodeUsedInfosResponse:
        """
        @summary Queries the nodes that reference the same node in a playbook.
        
        @param request: DescribeNodeUsedInfosRequest
        @return: DescribeNodeUsedInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_used_infos_with_options_async(request, runtime)

    def describe_notify_template_list_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeNotifyTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeNotifyTemplateListResponse:
        """
        @summary 查询通知消息模版列表
        
        @param request: DescribeNotifyTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNotifyTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotifyTemplateList',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeNotifyTemplateListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeNotifyTemplateListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_notify_template_list_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeNotifyTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeNotifyTemplateListResponse:
        """
        @summary 查询通知消息模版列表
        
        @param request: DescribeNotifyTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNotifyTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotifyTemplateList',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeNotifyTemplateListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeNotifyTemplateListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_notify_template_list(
        self,
        request: sophonsoar_20220728_models.DescribeNotifyTemplateListRequest,
    ) -> sophonsoar_20220728_models.DescribeNotifyTemplateListResponse:
        """
        @summary 查询通知消息模版列表
        
        @param request: DescribeNotifyTemplateListRequest
        @return: DescribeNotifyTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_notify_template_list_with_options(request, runtime)

    async def describe_notify_template_list_async(
        self,
        request: sophonsoar_20220728_models.DescribeNotifyTemplateListRequest,
    ) -> sophonsoar_20220728_models.DescribeNotifyTemplateListResponse:
        """
        @summary 查询通知消息模版列表
        
        @param request: DescribeNotifyTemplateListRequest
        @return: DescribeNotifyTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_notify_template_list_with_options_async(request, runtime)

    def describe_open_api_info_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeOpenApiInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeOpenApiInfoResponse:
        """
        @summary 获取产品接口的详情
        
        @param request: DescribeOpenApiInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOpenApiInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpenApiInfo',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeOpenApiInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeOpenApiInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_open_api_info_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeOpenApiInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeOpenApiInfoResponse:
        """
        @summary 获取产品接口的详情
        
        @param request: DescribeOpenApiInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOpenApiInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpenApiInfo',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeOpenApiInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeOpenApiInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_open_api_info(
        self,
        request: sophonsoar_20220728_models.DescribeOpenApiInfoRequest,
    ) -> sophonsoar_20220728_models.DescribeOpenApiInfoResponse:
        """
        @summary 获取产品接口的详情
        
        @param request: DescribeOpenApiInfoRequest
        @return: DescribeOpenApiInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_open_api_info_with_options(request, runtime)

    async def describe_open_api_info_async(
        self,
        request: sophonsoar_20220728_models.DescribeOpenApiInfoRequest,
    ) -> sophonsoar_20220728_models.DescribeOpenApiInfoResponse:
        """
        @summary 获取产品接口的详情
        
        @param request: DescribeOpenApiInfoRequest
        @return: DescribeOpenApiInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_open_api_info_with_options_async(request, runtime)

    def describe_open_api_list_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeOpenApiListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeOpenApiListResponse:
        """
        @summary 获取产品的接口列表
        
        @param request: DescribeOpenApiListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOpenApiListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpenApiList',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeOpenApiListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeOpenApiListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_open_api_list_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeOpenApiListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeOpenApiListResponse:
        """
        @summary 获取产品的接口列表
        
        @param request: DescribeOpenApiListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOpenApiListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpenApiList',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeOpenApiListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeOpenApiListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_open_api_list(
        self,
        request: sophonsoar_20220728_models.DescribeOpenApiListRequest,
    ) -> sophonsoar_20220728_models.DescribeOpenApiListResponse:
        """
        @summary 获取产品的接口列表
        
        @param request: DescribeOpenApiListRequest
        @return: DescribeOpenApiListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_open_api_list_with_options(request, runtime)

    async def describe_open_api_list_async(
        self,
        request: sophonsoar_20220728_models.DescribeOpenApiListRequest,
    ) -> sophonsoar_20220728_models.DescribeOpenApiListResponse:
        """
        @summary 获取产品的接口列表
        
        @param request: DescribeOpenApiListRequest
        @return: DescribeOpenApiListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_open_api_list_with_options_async(request, runtime)

    def describe_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookResponse:
        """
        @summary Queries the XML configuration of a playbook.
        
        @param request: DescribePlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybookResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybookResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookResponse:
        """
        @summary Queries the XML configuration of a playbook.
        
        @param request: DescribePlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybookResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_playbook(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookResponse:
        """
        @summary Queries the XML configuration of a playbook.
        
        @param request: DescribePlaybookRequest
        @return: DescribePlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_with_options(request, runtime)

    async def describe_playbook_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookResponse:
        """
        @summary Queries the XML configuration of a playbook.
        
        @param request: DescribePlaybookRequest
        @return: DescribePlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbook_with_options_async(request, runtime)

    def describe_playbook_input_output_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookInputOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookInputOutputResponse:
        """
        @summary Queries the input and output parameter configurations of a playbook.
        
        @param request: DescribePlaybookInputOutputRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybookInputOutputResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookInputOutput',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybookInputOutputResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybookInputOutputResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_playbook_input_output_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookInputOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookInputOutputResponse:
        """
        @summary Queries the input and output parameter configurations of a playbook.
        
        @param request: DescribePlaybookInputOutputRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybookInputOutputResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookInputOutput',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybookInputOutputResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybookInputOutputResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_playbook_input_output(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookInputOutputRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookInputOutputResponse:
        """
        @summary Queries the input and output parameter configurations of a playbook.
        
        @param request: DescribePlaybookInputOutputRequest
        @return: DescribePlaybookInputOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_input_output_with_options(request, runtime)

    async def describe_playbook_input_output_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookInputOutputRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookInputOutputResponse:
        """
        @summary Queries the input and output parameter configurations of a playbook.
        
        @param request: DescribePlaybookInputOutputRequest
        @return: DescribePlaybookInputOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbook_input_output_with_options_async(request, runtime)

    def describe_playbook_metrics_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookMetricsResponse:
        """
        @summary Queries the metrics of a playbook. The metrics include the playbook name, playbook description, the number of times that the playbook is run, and the failure rate of the playbook.
        
        @param request: DescribePlaybookMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybookMetricsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookMetrics',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybookMetricsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybookMetricsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_playbook_metrics_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookMetricsResponse:
        """
        @summary Queries the metrics of a playbook. The metrics include the playbook name, playbook description, the number of times that the playbook is run, and the failure rate of the playbook.
        
        @param request: DescribePlaybookMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybookMetricsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookMetrics',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybookMetricsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybookMetricsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_playbook_metrics(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookMetricsRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookMetricsResponse:
        """
        @summary Queries the metrics of a playbook. The metrics include the playbook name, playbook description, the number of times that the playbook is run, and the failure rate of the playbook.
        
        @param request: DescribePlaybookMetricsRequest
        @return: DescribePlaybookMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_metrics_with_options(request, runtime)

    async def describe_playbook_metrics_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookMetricsRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookMetricsResponse:
        """
        @summary Queries the metrics of a playbook. The metrics include the playbook name, playbook description, the number of times that the playbook is run, and the failure rate of the playbook.
        
        @param request: DescribePlaybookMetricsRequest
        @return: DescribePlaybookMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbook_metrics_with_options_async(request, runtime)

    def describe_playbook_nodes_output_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNodesOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse:
        """
        @summary Queries the historical output data of a component node.
        
        @param request: DescribePlaybookNodesOutputRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybookNodesOutputResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookNodesOutput',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_playbook_nodes_output_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNodesOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse:
        """
        @summary Queries the historical output data of a component node.
        
        @param request: DescribePlaybookNodesOutputRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybookNodesOutputResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookNodesOutput',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_playbook_nodes_output(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNodesOutputRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse:
        """
        @summary Queries the historical output data of a component node.
        
        @param request: DescribePlaybookNodesOutputRequest
        @return: DescribePlaybookNodesOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_nodes_output_with_options(request, runtime)

    async def describe_playbook_nodes_output_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNodesOutputRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookNodesOutputResponse:
        """
        @summary Queries the historical output data of a component node.
        
        @param request: DescribePlaybookNodesOutputRequest
        @return: DescribePlaybookNodesOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbook_nodes_output_with_options_async(request, runtime)

    def describe_playbook_number_metrics_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNumberMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse:
        """
        @summary Queries the statistics of Security Orchestration Automation Response (SOAR), such as the numbers of created and enabled playbooks.
        
        @param request: DescribePlaybookNumberMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybookNumberMetricsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookNumberMetrics',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_playbook_number_metrics_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNumberMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse:
        """
        @summary Queries the statistics of Security Orchestration Automation Response (SOAR), such as the numbers of created and enabled playbooks.
        
        @param request: DescribePlaybookNumberMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybookNumberMetricsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookNumberMetrics',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_playbook_number_metrics(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNumberMetricsRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse:
        """
        @summary Queries the statistics of Security Orchestration Automation Response (SOAR), such as the numbers of created and enabled playbooks.
        
        @param request: DescribePlaybookNumberMetricsRequest
        @return: DescribePlaybookNumberMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_number_metrics_with_options(request, runtime)

    async def describe_playbook_number_metrics_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookNumberMetricsRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookNumberMetricsResponse:
        """
        @summary Queries the statistics of Security Orchestration Automation Response (SOAR), such as the numbers of created and enabled playbooks.
        
        @param request: DescribePlaybookNumberMetricsRequest
        @return: DescribePlaybookNumberMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbook_number_metrics_with_options_async(request, runtime)

    def describe_playbook_releases_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookReleasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookReleasesResponse:
        """
        @summary Queries the information about the published versions of a playbook.
        
        @param request: DescribePlaybookReleasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybookReleasesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookReleases',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybookReleasesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybookReleasesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_playbook_releases_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookReleasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybookReleasesResponse:
        """
        @summary Queries the information about the published versions of a playbook.
        
        @param request: DescribePlaybookReleasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybookReleasesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybookReleases',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybookReleasesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybookReleasesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_playbook_releases(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookReleasesRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookReleasesResponse:
        """
        @summary Queries the information about the published versions of a playbook.
        
        @param request: DescribePlaybookReleasesRequest
        @return: DescribePlaybookReleasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_playbook_releases_with_options(request, runtime)

    async def describe_playbook_releases_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybookReleasesRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybookReleasesResponse:
        """
        @summary Queries the information about the published versions of a playbook.
        
        @param request: DescribePlaybookReleasesRequest
        @return: DescribePlaybookReleasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbook_releases_with_options_async(request, runtime)

    def describe_playbooks_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybooksResponse:
        """
        @summary Retrieve the list of playbooks.
        
        @param request: DescribePlaybooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybooksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybooks',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybooksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybooksResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_playbooks_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePlaybooksResponse:
        """
        @summary Retrieve the list of playbooks.
        
        @param request: DescribePlaybooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePlaybooksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlaybooks',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePlaybooksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePlaybooksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_playbooks(
        self,
        request: sophonsoar_20220728_models.DescribePlaybooksRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybooksResponse:
        """
        @summary Retrieve the list of playbooks.
        
        @param request: DescribePlaybooksRequest
        @return: DescribePlaybooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_playbooks_with_options(request, runtime)

    async def describe_playbooks_async(
        self,
        request: sophonsoar_20220728_models.DescribePlaybooksRequest,
    ) -> sophonsoar_20220728_models.DescribePlaybooksResponse:
        """
        @summary Retrieve the list of playbooks.
        
        @param request: DescribePlaybooksRequest
        @return: DescribePlaybooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_playbooks_with_options_async(request, runtime)

    def describe_pop_api_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePopApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePopApiResponse:
        """
        @summary Queries the details of an API operation.
        
        @param request: DescribePopApiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePopApiResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApi',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePopApiResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePopApiResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_pop_api_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePopApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePopApiResponse:
        """
        @summary Queries the details of an API operation.
        
        @param request: DescribePopApiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePopApiResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApi',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePopApiResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePopApiResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_pop_api(
        self,
        request: sophonsoar_20220728_models.DescribePopApiRequest,
    ) -> sophonsoar_20220728_models.DescribePopApiResponse:
        """
        @summary Queries the details of an API operation.
        
        @param request: DescribePopApiRequest
        @return: DescribePopApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pop_api_with_options(request, runtime)

    async def describe_pop_api_async(
        self,
        request: sophonsoar_20220728_models.DescribePopApiRequest,
    ) -> sophonsoar_20220728_models.DescribePopApiResponse:
        """
        @summary Queries the details of an API operation.
        
        @param request: DescribePopApiRequest
        @return: DescribePopApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pop_api_with_options_async(request, runtime)

    def describe_pop_api_item_list_with_options(
        self,
        request: sophonsoar_20220728_models.DescribePopApiItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePopApiItemListResponse:
        """
        @summary Queries a list of API operations for an Alibaba Cloud service.
        
        @param request: DescribePopApiItemListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePopApiItemListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApiItemList',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePopApiItemListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePopApiItemListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_pop_api_item_list_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribePopApiItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribePopApiItemListResponse:
        """
        @summary Queries a list of API operations for an Alibaba Cloud service.
        
        @param request: DescribePopApiItemListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePopApiItemListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePopApiItemList',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribePopApiItemListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribePopApiItemListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_pop_api_item_list(
        self,
        request: sophonsoar_20220728_models.DescribePopApiItemListRequest,
    ) -> sophonsoar_20220728_models.DescribePopApiItemListResponse:
        """
        @summary Queries a list of API operations for an Alibaba Cloud service.
        
        @param request: DescribePopApiItemListRequest
        @return: DescribePopApiItemListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pop_api_item_list_with_options(request, runtime)

    async def describe_pop_api_item_list_async(
        self,
        request: sophonsoar_20220728_models.DescribePopApiItemListRequest,
    ) -> sophonsoar_20220728_models.DescribePopApiItemListResponse:
        """
        @summary Queries a list of API operations for an Alibaba Cloud service.
        
        @param request: DescribePopApiItemListRequest
        @return: DescribePopApiItemListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pop_api_item_list_with_options_async(request, runtime)

    def describe_process_statistics_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeProcessStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeProcessStatisticsResponse:
        """
        @summary 获取统计信息
        
        @param request: DescribeProcessStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessStatistics',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeProcessStatisticsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeProcessStatisticsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_process_statistics_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeProcessStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeProcessStatisticsResponse:
        """
        @summary 获取统计信息
        
        @param request: DescribeProcessStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessStatistics',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeProcessStatisticsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeProcessStatisticsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_process_statistics(
        self,
        request: sophonsoar_20220728_models.DescribeProcessStatisticsRequest,
    ) -> sophonsoar_20220728_models.DescribeProcessStatisticsResponse:
        """
        @summary 获取统计信息
        
        @param request: DescribeProcessStatisticsRequest
        @return: DescribeProcessStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_process_statistics_with_options(request, runtime)

    async def describe_process_statistics_async(
        self,
        request: sophonsoar_20220728_models.DescribeProcessStatisticsRequest,
    ) -> sophonsoar_20220728_models.DescribeProcessStatisticsResponse:
        """
        @summary 获取统计信息
        
        @param request: DescribeProcessStatisticsRequest
        @return: DescribeProcessStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_process_statistics_with_options_async(request, runtime)

    def describe_process_task_count_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeProcessTaskCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeProcessTaskCountResponse:
        """
        @summary Query the number of associated disposal tasks based on the entity UUID.
        
        @param request: DescribeProcessTaskCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessTaskCountResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessTaskCount',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeProcessTaskCountResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeProcessTaskCountResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_process_task_count_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeProcessTaskCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeProcessTaskCountResponse:
        """
        @summary Query the number of associated disposal tasks based on the entity UUID.
        
        @param request: DescribeProcessTaskCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessTaskCountResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessTaskCount',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeProcessTaskCountResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeProcessTaskCountResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_process_task_count(
        self,
        request: sophonsoar_20220728_models.DescribeProcessTaskCountRequest,
    ) -> sophonsoar_20220728_models.DescribeProcessTaskCountResponse:
        """
        @summary Query the number of associated disposal tasks based on the entity UUID.
        
        @param request: DescribeProcessTaskCountRequest
        @return: DescribeProcessTaskCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_process_task_count_with_options(request, runtime)

    async def describe_process_task_count_async(
        self,
        request: sophonsoar_20220728_models.DescribeProcessTaskCountRequest,
    ) -> sophonsoar_20220728_models.DescribeProcessTaskCountResponse:
        """
        @summary Query the number of associated disposal tasks based on the entity UUID.
        
        @param request: DescribeProcessTaskCountRequest
        @return: DescribeProcessTaskCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_process_task_count_with_options_async(request, runtime)

    def describe_process_tasks_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeProcessTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeProcessTasksResponse:
        """
        @summary Queries the information about handling tasks. When you use Security Orchestration Automation Response (SOAR) to handle events, handling tasks are generated in the handling center.
        
        @param request: DescribeProcessTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.entity_uuid):
            query['EntityUuid'] = request.entity_uuid
        if not UtilClient.is_unset(request.event_uuid):
            query['EventUuid'] = request.event_uuid
        if not UtilClient.is_unset(request.order_field):
            query['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.param_content):
            query['ParamContent'] = request.param_content
        if not UtilClient.is_unset(request.process_action_end):
            query['ProcessActionEnd'] = request.process_action_end
        if not UtilClient.is_unset(request.process_action_start):
            query['ProcessActionStart'] = request.process_action_start
        if not UtilClient.is_unset(request.process_remove_end):
            query['ProcessRemoveEnd'] = request.process_remove_end
        if not UtilClient.is_unset(request.process_remove_start):
            query['ProcessRemoveStart'] = request.process_remove_start
        if not UtilClient.is_unset(request.process_strategy_uuid):
            query['ProcessStrategyUuid'] = request.process_strategy_uuid
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.trigger_source):
            query['TriggerSource'] = request.trigger_source
        if not UtilClient.is_unset(request.yun_code):
            query['YunCode'] = request.yun_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessTasks',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeProcessTasksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeProcessTasksResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_process_tasks_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeProcessTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeProcessTasksResponse:
        """
        @summary Queries the information about handling tasks. When you use Security Orchestration Automation Response (SOAR) to handle events, handling tasks are generated in the handling center.
        
        @param request: DescribeProcessTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.entity_uuid):
            query['EntityUuid'] = request.entity_uuid
        if not UtilClient.is_unset(request.event_uuid):
            query['EventUuid'] = request.event_uuid
        if not UtilClient.is_unset(request.order_field):
            query['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.param_content):
            query['ParamContent'] = request.param_content
        if not UtilClient.is_unset(request.process_action_end):
            query['ProcessActionEnd'] = request.process_action_end
        if not UtilClient.is_unset(request.process_action_start):
            query['ProcessActionStart'] = request.process_action_start
        if not UtilClient.is_unset(request.process_remove_end):
            query['ProcessRemoveEnd'] = request.process_remove_end
        if not UtilClient.is_unset(request.process_remove_start):
            query['ProcessRemoveStart'] = request.process_remove_start
        if not UtilClient.is_unset(request.process_strategy_uuid):
            query['ProcessStrategyUuid'] = request.process_strategy_uuid
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.trigger_source):
            query['TriggerSource'] = request.trigger_source
        if not UtilClient.is_unset(request.yun_code):
            query['YunCode'] = request.yun_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessTasks',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeProcessTasksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeProcessTasksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_process_tasks(
        self,
        request: sophonsoar_20220728_models.DescribeProcessTasksRequest,
    ) -> sophonsoar_20220728_models.DescribeProcessTasksResponse:
        """
        @summary Queries the information about handling tasks. When you use Security Orchestration Automation Response (SOAR) to handle events, handling tasks are generated in the handling center.
        
        @param request: DescribeProcessTasksRequest
        @return: DescribeProcessTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_process_tasks_with_options(request, runtime)

    async def describe_process_tasks_async(
        self,
        request: sophonsoar_20220728_models.DescribeProcessTasksRequest,
    ) -> sophonsoar_20220728_models.DescribeProcessTasksResponse:
        """
        @summary Queries the information about handling tasks. When you use Security Orchestration Automation Response (SOAR) to handle events, handling tasks are generated in the handling center.
        
        @param request: DescribeProcessTasksRequest
        @return: DescribeProcessTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_process_tasks_with_options_async(request, runtime)

    def describe_soar_record_action_output_list_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordActionOutputListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse:
        """
        @summary Queries the data that is returned when a component initiates an action in a playbook task.
        
        @param request: DescribeSoarRecordActionOutputListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSoarRecordActionOutputListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecordActionOutputList',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_soar_record_action_output_list_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordActionOutputListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse:
        """
        @summary Queries the data that is returned when a component initiates an action in a playbook task.
        
        @param request: DescribeSoarRecordActionOutputListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSoarRecordActionOutputListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecordActionOutputList',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_soar_record_action_output_list(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordActionOutputListRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse:
        """
        @summary Queries the data that is returned when a component initiates an action in a playbook task.
        
        @param request: DescribeSoarRecordActionOutputListRequest
        @return: DescribeSoarRecordActionOutputListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_soar_record_action_output_list_with_options(request, runtime)

    async def describe_soar_record_action_output_list_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordActionOutputListRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordActionOutputListResponse:
        """
        @summary Queries the data that is returned when a component initiates an action in a playbook task.
        
        @param request: DescribeSoarRecordActionOutputListRequest
        @return: DescribeSoarRecordActionOutputListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_soar_record_action_output_list_with_options_async(request, runtime)

    def describe_soar_record_in_output_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordInOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse:
        """
        @summary Queries the input and output data of a component action. You can call this operation after a playbook is run.
        
        @param request: DescribeSoarRecordInOutputRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSoarRecordInOutputResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecordInOutput',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_soar_record_in_output_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordInOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse:
        """
        @summary Queries the input and output data of a component action. You can call this operation after a playbook is run.
        
        @param request: DescribeSoarRecordInOutputRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSoarRecordInOutputResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecordInOutput',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_soar_record_in_output(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordInOutputRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse:
        """
        @summary Queries the input and output data of a component action. You can call this operation after a playbook is run.
        
        @param request: DescribeSoarRecordInOutputRequest
        @return: DescribeSoarRecordInOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_soar_record_in_output_with_options(request, runtime)

    async def describe_soar_record_in_output_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordInOutputRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordInOutputResponse:
        """
        @summary Queries the input and output data of a component action. You can call this operation after a playbook is run.
        
        @param request: DescribeSoarRecordInOutputRequest
        @return: DescribeSoarRecordInOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_soar_record_in_output_with_options_async(request, runtime)

    def describe_soar_records_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordsResponse:
        """
        @summary Get the execution records of a playbook.
        
        @param request: DescribeSoarRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSoarRecordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecords',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeSoarRecordsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeSoarRecordsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_soar_records_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordsResponse:
        """
        @summary Get the execution records of a playbook.
        
        @param request: DescribeSoarRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSoarRecordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarRecords',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeSoarRecordsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeSoarRecordsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_soar_records(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordsRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordsResponse:
        """
        @summary Get the execution records of a playbook.
        
        @param request: DescribeSoarRecordsRequest
        @return: DescribeSoarRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_soar_records_with_options(request, runtime)

    async def describe_soar_records_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarRecordsRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarRecordsResponse:
        """
        @summary Get the execution records of a playbook.
        
        @param request: DescribeSoarRecordsRequest
        @return: DescribeSoarRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_soar_records_with_options_async(request, runtime)

    def describe_soar_task_and_actions_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeSoarTaskAndActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse:
        """
        @summary Queries the execution records of a component during the running of a playbook.
        
        @param request: DescribeSoarTaskAndActionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSoarTaskAndActionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarTaskAndActions',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_soar_task_and_actions_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarTaskAndActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse:
        """
        @summary Queries the execution records of a component during the running of a playbook.
        
        @param request: DescribeSoarTaskAndActionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSoarTaskAndActionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSoarTaskAndActions',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_soar_task_and_actions(
        self,
        request: sophonsoar_20220728_models.DescribeSoarTaskAndActionsRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse:
        """
        @summary Queries the execution records of a component during the running of a playbook.
        
        @param request: DescribeSoarTaskAndActionsRequest
        @return: DescribeSoarTaskAndActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_soar_task_and_actions_with_options(request, runtime)

    async def describe_soar_task_and_actions_async(
        self,
        request: sophonsoar_20220728_models.DescribeSoarTaskAndActionsRequest,
    ) -> sophonsoar_20220728_models.DescribeSoarTaskAndActionsResponse:
        """
        @summary Queries the execution records of a component during the running of a playbook.
        
        @param request: DescribeSoarTaskAndActionsRequest
        @return: DescribeSoarTaskAndActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_soar_task_and_actions_with_options_async(request, runtime)

    def describe_sophon_commands_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeSophonCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSophonCommandsResponse:
        """
        @summary Queries the commands that can be run to obtain objects.
        
        @param request: DescribeSophonCommandsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSophonCommandsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSophonCommands',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeSophonCommandsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeSophonCommandsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_sophon_commands_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeSophonCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeSophonCommandsResponse:
        """
        @summary Queries the commands that can be run to obtain objects.
        
        @param request: DescribeSophonCommandsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSophonCommandsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSophonCommands',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeSophonCommandsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeSophonCommandsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_sophon_commands(
        self,
        request: sophonsoar_20220728_models.DescribeSophonCommandsRequest,
    ) -> sophonsoar_20220728_models.DescribeSophonCommandsResponse:
        """
        @summary Queries the commands that can be run to obtain objects.
        
        @param request: DescribeSophonCommandsRequest
        @return: DescribeSophonCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_sophon_commands_with_options(request, runtime)

    async def describe_sophon_commands_async(
        self,
        request: sophonsoar_20220728_models.DescribeSophonCommandsRequest,
    ) -> sophonsoar_20220728_models.DescribeSophonCommandsResponse:
        """
        @summary Queries the commands that can be run to obtain objects.
        
        @param request: DescribeSophonCommandsRequest
        @return: DescribeSophonCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_sophon_commands_with_options_async(request, runtime)

    def describe_vendor_api_list_with_options(
        self,
        request: sophonsoar_20220728_models.DescribeVendorApiListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeVendorApiListResponse:
        """
        @summary 查询云厂商OpenApi列表
        
        @param request: DescribeVendorApiListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVendorApiListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.vendor_code):
            query['VendorCode'] = request.vendor_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVendorApiList',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeVendorApiListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeVendorApiListResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_vendor_api_list_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescribeVendorApiListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescribeVendorApiListResponse:
        """
        @summary 查询云厂商OpenApi列表
        
        @param request: DescribeVendorApiListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVendorApiListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.vendor_code):
            query['VendorCode'] = request.vendor_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVendorApiList',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescribeVendorApiListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescribeVendorApiListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_vendor_api_list(
        self,
        request: sophonsoar_20220728_models.DescribeVendorApiListRequest,
    ) -> sophonsoar_20220728_models.DescribeVendorApiListResponse:
        """
        @summary 查询云厂商OpenApi列表
        
        @param request: DescribeVendorApiListRequest
        @return: DescribeVendorApiListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vendor_api_list_with_options(request, runtime)

    async def describe_vendor_api_list_async(
        self,
        request: sophonsoar_20220728_models.DescribeVendorApiListRequest,
    ) -> sophonsoar_20220728_models.DescribeVendorApiListResponse:
        """
        @summary 查询云厂商OpenApi列表
        
        @param request: DescribeVendorApiListRequest
        @return: DescribeVendorApiListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vendor_api_list_with_options_async(request, runtime)

    def describer_python_3script_logs_with_options(
        self,
        request: sophonsoar_20220728_models.DescriberPython3ScriptLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse:
        """
        @summary Queries the operational logs of a Python3 script by using the UUID that is returned when the script is run. The UUID is specified by requestUuid.
        
        @param request: DescriberPython3ScriptLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescriberPython3ScriptLogsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescriberPython3ScriptLogs',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse(),
                self.execute(params, req, runtime)
            )

    async def describer_python_3script_logs_with_options_async(
        self,
        request: sophonsoar_20220728_models.DescriberPython3ScriptLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse:
        """
        @summary Queries the operational logs of a Python3 script by using the UUID that is returned when the script is run. The UUID is specified by requestUuid.
        
        @param request: DescriberPython3ScriptLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescriberPython3ScriptLogsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescriberPython3ScriptLogs',
            version='2022-07-28',
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
                sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describer_python_3script_logs(
        self,
        request: sophonsoar_20220728_models.DescriberPython3ScriptLogsRequest,
    ) -> sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse:
        """
        @summary Queries the operational logs of a Python3 script by using the UUID that is returned when the script is run. The UUID is specified by requestUuid.
        
        @param request: DescriberPython3ScriptLogsRequest
        @return: DescriberPython3ScriptLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describer_python_3script_logs_with_options(request, runtime)

    async def describer_python_3script_logs_async(
        self,
        request: sophonsoar_20220728_models.DescriberPython3ScriptLogsRequest,
    ) -> sophonsoar_20220728_models.DescriberPython3ScriptLogsResponse:
        """
        @summary Queries the operational logs of a Python3 script by using the UUID that is returned when the script is run. The UUID is specified by requestUuid.
        
        @param request: DescriberPython3ScriptLogsRequest
        @return: DescriberPython3ScriptLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describer_python_3script_logs_with_options_async(request, runtime)

    def modify_component_asset_with_options(
        self,
        request: sophonsoar_20220728_models.ModifyComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyComponentAssetResponse:
        """
        @summary Modifies the information about the asset that is configured for a component.
        
        @param request: ModifyComponentAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyComponentAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_config):
            query['AssetConfig'] = request.asset_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyComponentAsset',
            version='2022-07-28',
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
                sophonsoar_20220728_models.ModifyComponentAssetResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.ModifyComponentAssetResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_component_asset_with_options_async(
        self,
        request: sophonsoar_20220728_models.ModifyComponentAssetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyComponentAssetResponse:
        """
        @summary Modifies the information about the asset that is configured for a component.
        
        @param request: ModifyComponentAssetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyComponentAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_config):
            query['AssetConfig'] = request.asset_config
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyComponentAsset',
            version='2022-07-28',
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
                sophonsoar_20220728_models.ModifyComponentAssetResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.ModifyComponentAssetResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_component_asset(
        self,
        request: sophonsoar_20220728_models.ModifyComponentAssetRequest,
    ) -> sophonsoar_20220728_models.ModifyComponentAssetResponse:
        """
        @summary Modifies the information about the asset that is configured for a component.
        
        @param request: ModifyComponentAssetRequest
        @return: ModifyComponentAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_component_asset_with_options(request, runtime)

    async def modify_component_asset_async(
        self,
        request: sophonsoar_20220728_models.ModifyComponentAssetRequest,
    ) -> sophonsoar_20220728_models.ModifyComponentAssetResponse:
        """
        @summary Modifies the information about the asset that is configured for a component.
        
        @param request: ModifyComponentAssetRequest
        @return: ModifyComponentAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_component_asset_with_options_async(request, runtime)

    def modify_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyPlaybookResponse:
        """
        @summary Modifies the configuration of a playbook.
        
        @param request: ModifyPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.ModifyPlaybookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.ModifyPlaybookResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyPlaybookResponse:
        """
        @summary Modifies the configuration of a playbook.
        
        @param request: ModifyPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.taskflow):
            body['Taskflow'] = request.taskflow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.ModifyPlaybookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.ModifyPlaybookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_playbook(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookRequest,
    ) -> sophonsoar_20220728_models.ModifyPlaybookResponse:
        """
        @summary Modifies the configuration of a playbook.
        
        @param request: ModifyPlaybookRequest
        @return: ModifyPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_playbook_with_options(request, runtime)

    async def modify_playbook_async(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookRequest,
    ) -> sophonsoar_20220728_models.ModifyPlaybookResponse:
        """
        @summary Modifies the configuration of a playbook.
        
        @param request: ModifyPlaybookRequest
        @return: ModifyPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_playbook_with_options_async(request, runtime)

    def modify_playbook_input_output_with_options(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInputOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse:
        """
        @summary Modifies the input and output parameters of a playbook.
        
        @param request: ModifyPlaybookInputOutputRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPlaybookInputOutputResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exe_config):
            body['ExeConfig'] = request.exe_config
        if not UtilClient.is_unset(request.input_params):
            body['InputParams'] = request.input_params
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.output_params):
            body['OutputParams'] = request.output_params
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybookInputOutput',
            version='2022-07-28',
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
                sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_playbook_input_output_with_options_async(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInputOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse:
        """
        @summary Modifies the input and output parameters of a playbook.
        
        @param request: ModifyPlaybookInputOutputRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPlaybookInputOutputResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.exe_config):
            body['ExeConfig'] = request.exe_config
        if not UtilClient.is_unset(request.input_params):
            body['InputParams'] = request.input_params
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        if not UtilClient.is_unset(request.output_params):
            body['OutputParams'] = request.output_params
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybookInputOutput',
            version='2022-07-28',
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
                sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_playbook_input_output(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInputOutputRequest,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse:
        """
        @summary Modifies the input and output parameters of a playbook.
        
        @param request: ModifyPlaybookInputOutputRequest
        @return: ModifyPlaybookInputOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_playbook_input_output_with_options(request, runtime)

    async def modify_playbook_input_output_async(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInputOutputRequest,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInputOutputResponse:
        """
        @summary Modifies the input and output parameters of a playbook.
        
        @param request: ModifyPlaybookInputOutputRequest
        @return: ModifyPlaybookInputOutputResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_playbook_input_output_with_options_async(request, runtime)

    def modify_playbook_instance_status_with_options(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse:
        """
        @summary Modifies the status of a playbook.
        
        @param request: ModifyPlaybookInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPlaybookInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybookInstanceStatus',
            version='2022-07-28',
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
                sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_playbook_instance_status_with_options_async(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse:
        """
        @summary Modifies the status of a playbook.
        
        @param request: ModifyPlaybookInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPlaybookInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        body = {}
        if not UtilClient.is_unset(request.active):
            body['Active'] = request.active
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPlaybookInstanceStatus',
            version='2022-07-28',
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
                sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_playbook_instance_status(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInstanceStatusRequest,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse:
        """
        @summary Modifies the status of a playbook.
        
        @param request: ModifyPlaybookInstanceStatusRequest
        @return: ModifyPlaybookInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_playbook_instance_status_with_options(request, runtime)

    async def modify_playbook_instance_status_async(
        self,
        request: sophonsoar_20220728_models.ModifyPlaybookInstanceStatusRequest,
    ) -> sophonsoar_20220728_models.ModifyPlaybookInstanceStatusResponse:
        """
        @summary Modifies the status of a playbook.
        
        @param request: ModifyPlaybookInstanceStatusRequest
        @return: ModifyPlaybookInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_playbook_instance_status_with_options_async(request, runtime)

    def publish_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.PublishPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.PublishPlaybookResponse:
        """
        @summary Publishes the playbook. After the playbook is published, the playbook runs based on the new logic.
        
        @param request: PublishPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.PublishPlaybookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.PublishPlaybookResponse(),
                self.execute(params, req, runtime)
            )

    async def publish_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.PublishPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.PublishPlaybookResponse:
        """
        @summary Publishes the playbook. After the playbook is published, the playbook runs based on the new logic.
        
        @param request: PublishPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.PublishPlaybookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.PublishPlaybookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def publish_playbook(
        self,
        request: sophonsoar_20220728_models.PublishPlaybookRequest,
    ) -> sophonsoar_20220728_models.PublishPlaybookResponse:
        """
        @summary Publishes the playbook. After the playbook is published, the playbook runs based on the new logic.
        
        @param request: PublishPlaybookRequest
        @return: PublishPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_playbook_with_options(request, runtime)

    async def publish_playbook_async(
        self,
        request: sophonsoar_20220728_models.PublishPlaybookRequest,
    ) -> sophonsoar_20220728_models.PublishPlaybookResponse:
        """
        @summary Publishes the playbook. After the playbook is published, the playbook runs based on the new logic.
        
        @param request: PublishPlaybookRequest
        @return: PublishPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_playbook_with_options_async(request, runtime)

    def query_tree_data_with_options(
        self,
        request: sophonsoar_20220728_models.QueryTreeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.QueryTreeDataResponse:
        """
        @summary Queries all playbooks at a time.
        
        @param request: QueryTreeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTreeDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTreeData',
            version='2022-07-28',
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
                sophonsoar_20220728_models.QueryTreeDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.QueryTreeDataResponse(),
                self.execute(params, req, runtime)
            )

    async def query_tree_data_with_options_async(
        self,
        request: sophonsoar_20220728_models.QueryTreeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.QueryTreeDataResponse:
        """
        @summary Queries all playbooks at a time.
        
        @param request: QueryTreeDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTreeDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTreeData',
            version='2022-07-28',
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
                sophonsoar_20220728_models.QueryTreeDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.QueryTreeDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_tree_data(
        self,
        request: sophonsoar_20220728_models.QueryTreeDataRequest,
    ) -> sophonsoar_20220728_models.QueryTreeDataResponse:
        """
        @summary Queries all playbooks at a time.
        
        @param request: QueryTreeDataRequest
        @return: QueryTreeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_tree_data_with_options(request, runtime)

    async def query_tree_data_async(
        self,
        request: sophonsoar_20220728_models.QueryTreeDataRequest,
    ) -> sophonsoar_20220728_models.QueryTreeDataResponse:
        """
        @summary Queries all playbooks at a time.
        
        @param request: QueryTreeDataRequest
        @return: QueryTreeDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_tree_data_with_options_async(request, runtime)

    def rename_playbook_node_with_options(
        self,
        request: sophonsoar_20220728_models.RenamePlaybookNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RenamePlaybookNodeResponse:
        """
        @summary Changes the name of a node in a playbook. You can call this operation during playbook orchestration. After the name of the node is changed, the reference path of the node also changes.
        
        @param request: RenamePlaybookNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenamePlaybookNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_node_name):
            query['NewNodeName'] = request.new_node_name
        if not UtilClient.is_unset(request.old_node_name):
            query['OldNodeName'] = request.old_node_name
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenamePlaybookNode',
            version='2022-07-28',
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
                sophonsoar_20220728_models.RenamePlaybookNodeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.RenamePlaybookNodeResponse(),
                self.execute(params, req, runtime)
            )

    async def rename_playbook_node_with_options_async(
        self,
        request: sophonsoar_20220728_models.RenamePlaybookNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RenamePlaybookNodeResponse:
        """
        @summary Changes the name of a node in a playbook. You can call this operation during playbook orchestration. After the name of the node is changed, the reference path of the node also changes.
        
        @param request: RenamePlaybookNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenamePlaybookNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_node_name):
            query['NewNodeName'] = request.new_node_name
        if not UtilClient.is_unset(request.old_node_name):
            query['OldNodeName'] = request.old_node_name
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenamePlaybookNode',
            version='2022-07-28',
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
                sophonsoar_20220728_models.RenamePlaybookNodeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.RenamePlaybookNodeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def rename_playbook_node(
        self,
        request: sophonsoar_20220728_models.RenamePlaybookNodeRequest,
    ) -> sophonsoar_20220728_models.RenamePlaybookNodeResponse:
        """
        @summary Changes the name of a node in a playbook. You can call this operation during playbook orchestration. After the name of the node is changed, the reference path of the node also changes.
        
        @param request: RenamePlaybookNodeRequest
        @return: RenamePlaybookNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rename_playbook_node_with_options(request, runtime)

    async def rename_playbook_node_async(
        self,
        request: sophonsoar_20220728_models.RenamePlaybookNodeRequest,
    ) -> sophonsoar_20220728_models.RenamePlaybookNodeResponse:
        """
        @summary Changes the name of a node in a playbook. You can call this operation during playbook orchestration. After the name of the node is changed, the reference path of the node also changes.
        
        @param request: RenamePlaybookNodeRequest
        @return: RenamePlaybookNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rename_playbook_node_with_options_async(request, runtime)

    def revert_playbook_release_with_options(
        self,
        request: sophonsoar_20220728_models.RevertPlaybookReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RevertPlaybookReleaseResponse:
        """
        @summary Rolls back a playbook to a specific version. You can determine whether to publish the new playbook version during the rollback.
        
        @param request: RevertPlaybookReleaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevertPlaybookReleaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_publish):
            body['IsPublish'] = request.is_publish
        if not UtilClient.is_unset(request.play_release_id):
            body['PlayReleaseId'] = request.play_release_id
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevertPlaybookRelease',
            version='2022-07-28',
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
                sophonsoar_20220728_models.RevertPlaybookReleaseResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.RevertPlaybookReleaseResponse(),
                self.execute(params, req, runtime)
            )

    async def revert_playbook_release_with_options_async(
        self,
        request: sophonsoar_20220728_models.RevertPlaybookReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RevertPlaybookReleaseResponse:
        """
        @summary Rolls back a playbook to a specific version. You can determine whether to publish the new playbook version during the rollback.
        
        @param request: RevertPlaybookReleaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevertPlaybookReleaseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_publish):
            body['IsPublish'] = request.is_publish
        if not UtilClient.is_unset(request.play_release_id):
            body['PlayReleaseId'] = request.play_release_id
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevertPlaybookRelease',
            version='2022-07-28',
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
                sophonsoar_20220728_models.RevertPlaybookReleaseResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.RevertPlaybookReleaseResponse(),
                await self.execute_async(params, req, runtime)
            )

    def revert_playbook_release(
        self,
        request: sophonsoar_20220728_models.RevertPlaybookReleaseRequest,
    ) -> sophonsoar_20220728_models.RevertPlaybookReleaseResponse:
        """
        @summary Rolls back a playbook to a specific version. You can determine whether to publish the new playbook version during the rollback.
        
        @param request: RevertPlaybookReleaseRequest
        @return: RevertPlaybookReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revert_playbook_release_with_options(request, runtime)

    async def revert_playbook_release_async(
        self,
        request: sophonsoar_20220728_models.RevertPlaybookReleaseRequest,
    ) -> sophonsoar_20220728_models.RevertPlaybookReleaseResponse:
        """
        @summary Rolls back a playbook to a specific version. You can determine whether to publish the new playbook version during the rollback.
        
        @param request: RevertPlaybookReleaseRequest
        @return: RevertPlaybookReleaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revert_playbook_release_with_options_async(request, runtime)

    def run_notify_component_with_email_with_options(
        self,
        request: sophonsoar_20220728_models.RunNotifyComponentWithEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RunNotifyComponentWithEmailResponse:
        """
        @summary 执行通知组件-email发送消息
        
        @param request: RunNotifyComponentWithEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunNotifyComponentWithEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.receivers):
            query['Receivers'] = request.receivers
        if not UtilClient.is_unset(request.role_for):
            query['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunNotifyComponentWithEmail',
            version='2022-07-28',
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
                sophonsoar_20220728_models.RunNotifyComponentWithEmailResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.RunNotifyComponentWithEmailResponse(),
                self.execute(params, req, runtime)
            )

    async def run_notify_component_with_email_with_options_async(
        self,
        request: sophonsoar_20220728_models.RunNotifyComponentWithEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RunNotifyComponentWithEmailResponse:
        """
        @summary 执行通知组件-email发送消息
        
        @param request: RunNotifyComponentWithEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunNotifyComponentWithEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.receivers):
            query['Receivers'] = request.receivers
        if not UtilClient.is_unset(request.role_for):
            query['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.subject):
            query['Subject'] = request.subject
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunNotifyComponentWithEmail',
            version='2022-07-28',
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
                sophonsoar_20220728_models.RunNotifyComponentWithEmailResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.RunNotifyComponentWithEmailResponse(),
                await self.execute_async(params, req, runtime)
            )

    def run_notify_component_with_email(
        self,
        request: sophonsoar_20220728_models.RunNotifyComponentWithEmailRequest,
    ) -> sophonsoar_20220728_models.RunNotifyComponentWithEmailResponse:
        """
        @summary 执行通知组件-email发送消息
        
        @param request: RunNotifyComponentWithEmailRequest
        @return: RunNotifyComponentWithEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_notify_component_with_email_with_options(request, runtime)

    async def run_notify_component_with_email_async(
        self,
        request: sophonsoar_20220728_models.RunNotifyComponentWithEmailRequest,
    ) -> sophonsoar_20220728_models.RunNotifyComponentWithEmailResponse:
        """
        @summary 执行通知组件-email发送消息
        
        @param request: RunNotifyComponentWithEmailRequest
        @return: RunNotifyComponentWithEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_notify_component_with_email_with_options_async(request, runtime)

    def run_notify_component_with_message_center_with_options(
        self,
        request: sophonsoar_20220728_models.RunNotifyComponentWithMessageCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RunNotifyComponentWithMessageCenterResponse:
        """
        @summary 执行通知组件-消息中心发送消息
        
        @param request: RunNotifyComponentWithMessageCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunNotifyComponentWithMessageCenterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.aliuid):
            query['Aliuid'] = request.aliuid
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.channel_type_list):
            query['ChannelTypeList'] = request.channel_type_list
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.role_for):
            query['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunNotifyComponentWithMessageCenter',
            version='2022-07-28',
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
                sophonsoar_20220728_models.RunNotifyComponentWithMessageCenterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.RunNotifyComponentWithMessageCenterResponse(),
                self.execute(params, req, runtime)
            )

    async def run_notify_component_with_message_center_with_options_async(
        self,
        request: sophonsoar_20220728_models.RunNotifyComponentWithMessageCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RunNotifyComponentWithMessageCenterResponse:
        """
        @summary 执行通知组件-消息中心发送消息
        
        @param request: RunNotifyComponentWithMessageCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunNotifyComponentWithMessageCenterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.aliuid):
            query['Aliuid'] = request.aliuid
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.channel_type_list):
            query['ChannelTypeList'] = request.channel_type_list
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.role_for):
            query['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunNotifyComponentWithMessageCenter',
            version='2022-07-28',
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
                sophonsoar_20220728_models.RunNotifyComponentWithMessageCenterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.RunNotifyComponentWithMessageCenterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def run_notify_component_with_message_center(
        self,
        request: sophonsoar_20220728_models.RunNotifyComponentWithMessageCenterRequest,
    ) -> sophonsoar_20220728_models.RunNotifyComponentWithMessageCenterResponse:
        """
        @summary 执行通知组件-消息中心发送消息
        
        @param request: RunNotifyComponentWithMessageCenterRequest
        @return: RunNotifyComponentWithMessageCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_notify_component_with_message_center_with_options(request, runtime)

    async def run_notify_component_with_message_center_async(
        self,
        request: sophonsoar_20220728_models.RunNotifyComponentWithMessageCenterRequest,
    ) -> sophonsoar_20220728_models.RunNotifyComponentWithMessageCenterResponse:
        """
        @summary 执行通知组件-消息中心发送消息
        
        @param request: RunNotifyComponentWithMessageCenterRequest
        @return: RunNotifyComponentWithMessageCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_notify_component_with_message_center_with_options_async(request, runtime)

    def run_notify_component_with_webhook_with_options(
        self,
        request: sophonsoar_20220728_models.RunNotifyComponentWithWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RunNotifyComponentWithWebhookResponse:
        """
        @summary 执行通知组件-webhook发送消息
        
        @param request: RunNotifyComponentWithWebhookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunNotifyComponentWithWebhookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.msg_type):
            query['MsgType'] = request.msg_type
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.role_for):
            query['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.secret):
            query['Secret'] = request.secret
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunNotifyComponentWithWebhook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.RunNotifyComponentWithWebhookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.RunNotifyComponentWithWebhookResponse(),
                self.execute(params, req, runtime)
            )

    async def run_notify_component_with_webhook_with_options_async(
        self,
        request: sophonsoar_20220728_models.RunNotifyComponentWithWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RunNotifyComponentWithWebhookResponse:
        """
        @summary 执行通知组件-webhook发送消息
        
        @param request: RunNotifyComponentWithWebhookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunNotifyComponentWithWebhookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.msg_type):
            query['MsgType'] = request.msg_type
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.playbook_uuid):
            query['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.role_for):
            query['RoleFor'] = request.role_for
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.secret):
            query['Secret'] = request.secret
        if not UtilClient.is_unset(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunNotifyComponentWithWebhook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.RunNotifyComponentWithWebhookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.RunNotifyComponentWithWebhookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def run_notify_component_with_webhook(
        self,
        request: sophonsoar_20220728_models.RunNotifyComponentWithWebhookRequest,
    ) -> sophonsoar_20220728_models.RunNotifyComponentWithWebhookResponse:
        """
        @summary 执行通知组件-webhook发送消息
        
        @param request: RunNotifyComponentWithWebhookRequest
        @return: RunNotifyComponentWithWebhookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_notify_component_with_webhook_with_options(request, runtime)

    async def run_notify_component_with_webhook_async(
        self,
        request: sophonsoar_20220728_models.RunNotifyComponentWithWebhookRequest,
    ) -> sophonsoar_20220728_models.RunNotifyComponentWithWebhookResponse:
        """
        @summary 执行通知组件-webhook发送消息
        
        @param request: RunNotifyComponentWithWebhookRequest
        @return: RunNotifyComponentWithWebhookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_notify_component_with_webhook_with_options_async(request, runtime)

    def run_python_3script_with_options(
        self,
        request: sophonsoar_20220728_models.RunPython3ScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RunPython3ScriptResponse:
        """
        @summary Submits and runs a Python3 script. You can call this operation only for data processing.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.alibabacloud.com/en/pricing-calculator?_p_lc=1&spm=openapi-amp.newDocPublishment.0.0.4c41281fWhbdPa#/commodity/vm_intl).
        
        @param request: RunPython3ScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunPython3ScriptResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.python_script):
            body['PythonScript'] = request.python_script
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunPython3Script',
            version='2022-07-28',
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
                sophonsoar_20220728_models.RunPython3ScriptResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.RunPython3ScriptResponse(),
                self.execute(params, req, runtime)
            )

    async def run_python_3script_with_options_async(
        self,
        request: sophonsoar_20220728_models.RunPython3ScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.RunPython3ScriptResponse:
        """
        @summary Submits and runs a Python3 script. You can call this operation only for data processing.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.alibabacloud.com/en/pricing-calculator?_p_lc=1&spm=openapi-amp.newDocPublishment.0.0.4c41281fWhbdPa#/commodity/vm_intl).
        
        @param request: RunPython3ScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunPython3ScriptResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_name):
            body['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.python_script):
            body['PythonScript'] = request.python_script
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunPython3Script',
            version='2022-07-28',
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
                sophonsoar_20220728_models.RunPython3ScriptResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.RunPython3ScriptResponse(),
                await self.execute_async(params, req, runtime)
            )

    def run_python_3script(
        self,
        request: sophonsoar_20220728_models.RunPython3ScriptRequest,
    ) -> sophonsoar_20220728_models.RunPython3ScriptResponse:
        """
        @summary Submits and runs a Python3 script. You can call this operation only for data processing.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.alibabacloud.com/en/pricing-calculator?_p_lc=1&spm=openapi-amp.newDocPublishment.0.0.4c41281fWhbdPa#/commodity/vm_intl).
        
        @param request: RunPython3ScriptRequest
        @return: RunPython3ScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_python_3script_with_options(request, runtime)

    async def run_python_3script_async(
        self,
        request: sophonsoar_20220728_models.RunPython3ScriptRequest,
    ) -> sophonsoar_20220728_models.RunPython3ScriptResponse:
        """
        @summary Submits and runs a Python3 script. You can call this operation only for data processing.
        
        @description Before you call this operation, make sure that you understand the billing method and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.alibabacloud.com/en/pricing-calculator?_p_lc=1&spm=openapi-amp.newDocPublishment.0.0.4c41281fWhbdPa#/commodity/vm_intl).
        
        @param request: RunPython3ScriptRequest
        @return: RunPython3ScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_python_3script_with_options_async(request, runtime)

    def trigger_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.TriggerPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.TriggerPlaybookResponse:
        """
        @summary Triggers an enabled custom playbook or a predefined playbook.
        
        @description Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.alibabacloud.com/en/pricing-calculator?_p_lc=1&spm=a2796.7960336.3034855210.1.7adab91arMeIx2#/commodity/vm_intl).
        
        @param request: TriggerPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input_param):
            body['InputParam'] = request.input_param
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.TriggerPlaybookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.TriggerPlaybookResponse(),
                self.execute(params, req, runtime)
            )

    async def trigger_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.TriggerPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.TriggerPlaybookResponse:
        """
        @summary Triggers an enabled custom playbook or a predefined playbook.
        
        @description Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.alibabacloud.com/en/pricing-calculator?_p_lc=1&spm=a2796.7960336.3034855210.1.7adab91arMeIx2#/commodity/vm_intl).
        
        @param request: TriggerPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input_param):
            body['InputParam'] = request.input_param
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.TriggerPlaybookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.TriggerPlaybookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def trigger_playbook(
        self,
        request: sophonsoar_20220728_models.TriggerPlaybookRequest,
    ) -> sophonsoar_20220728_models.TriggerPlaybookResponse:
        """
        @summary Triggers an enabled custom playbook or a predefined playbook.
        
        @description Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.alibabacloud.com/en/pricing-calculator?_p_lc=1&spm=a2796.7960336.3034855210.1.7adab91arMeIx2#/commodity/vm_intl).
        
        @param request: TriggerPlaybookRequest
        @return: TriggerPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.trigger_playbook_with_options(request, runtime)

    async def trigger_playbook_async(
        self,
        request: sophonsoar_20220728_models.TriggerPlaybookRequest,
    ) -> sophonsoar_20220728_models.TriggerPlaybookResponse:
        """
        @summary Triggers an enabled custom playbook or a predefined playbook.
        
        @description Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.alibabacloud.com/en/pricing-calculator?_p_lc=1&spm=a2796.7960336.3034855210.1.7adab91arMeIx2#/commodity/vm_intl).
        
        @param request: TriggerPlaybookRequest
        @return: TriggerPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.trigger_playbook_with_options_async(request, runtime)

    def trigger_process_task_with_options(
        self,
        request: sophonsoar_20220728_models.TriggerProcessTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.TriggerProcessTaskResponse:
        """
        @summary Performs an action on a handling task that is generated by the handling center when an event is handled by using Security Orchestration Automation Response (SOAR). For example, you can call this operation to cancel blocking or isolation, or retry blocking.
        
        @param request: TriggerProcessTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerProcessTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerProcessTask',
            version='2022-07-28',
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
                sophonsoar_20220728_models.TriggerProcessTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.TriggerProcessTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def trigger_process_task_with_options_async(
        self,
        request: sophonsoar_20220728_models.TriggerProcessTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.TriggerProcessTaskResponse:
        """
        @summary Performs an action on a handling task that is generated by the handling center when an event is handled by using Security Orchestration Automation Response (SOAR). For example, you can call this operation to cancel blocking or isolation, or retry blocking.
        
        @param request: TriggerProcessTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerProcessTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TriggerProcessTask',
            version='2022-07-28',
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
                sophonsoar_20220728_models.TriggerProcessTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.TriggerProcessTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def trigger_process_task(
        self,
        request: sophonsoar_20220728_models.TriggerProcessTaskRequest,
    ) -> sophonsoar_20220728_models.TriggerProcessTaskResponse:
        """
        @summary Performs an action on a handling task that is generated by the handling center when an event is handled by using Security Orchestration Automation Response (SOAR). For example, you can call this operation to cancel blocking or isolation, or retry blocking.
        
        @param request: TriggerProcessTaskRequest
        @return: TriggerProcessTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.trigger_process_task_with_options(request, runtime)

    async def trigger_process_task_async(
        self,
        request: sophonsoar_20220728_models.TriggerProcessTaskRequest,
    ) -> sophonsoar_20220728_models.TriggerProcessTaskResponse:
        """
        @summary Performs an action on a handling task that is generated by the handling center when an event is handled by using Security Orchestration Automation Response (SOAR). For example, you can call this operation to cancel blocking or isolation, or retry blocking.
        
        @param request: TriggerProcessTaskRequest
        @return: TriggerProcessTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.trigger_process_task_with_options_async(request, runtime)

    def trigger_sophon_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.TriggerSophonPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.TriggerSophonPlaybookResponse:
        """
        @summary Triggers a playbook or a command.
        
        @description Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.alibabacloud.com/en/pricing-calculator?_p_lc=1&spm=a2796.7960336.3034855210.1.7adab91arMeIx2#/commodity/vm_intl).
        
        @param request: TriggerSophonPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerSophonPlaybookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_name):
            query['CommandName'] = request.command_name
        if not UtilClient.is_unset(request.input_params):
            query['InputParams'] = request.input_params
        if not UtilClient.is_unset(request.sophon_task_id):
            query['SophonTaskId'] = request.sophon_task_id
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerSophonPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.TriggerSophonPlaybookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.TriggerSophonPlaybookResponse(),
                self.execute(params, req, runtime)
            )

    async def trigger_sophon_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.TriggerSophonPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.TriggerSophonPlaybookResponse:
        """
        @summary Triggers a playbook or a command.
        
        @description Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.alibabacloud.com/en/pricing-calculator?_p_lc=1&spm=a2796.7960336.3034855210.1.7adab91arMeIx2#/commodity/vm_intl).
        
        @param request: TriggerSophonPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TriggerSophonPlaybookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_name):
            query['CommandName'] = request.command_name
        if not UtilClient.is_unset(request.input_params):
            query['InputParams'] = request.input_params
        if not UtilClient.is_unset(request.sophon_task_id):
            query['SophonTaskId'] = request.sophon_task_id
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerSophonPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.TriggerSophonPlaybookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.TriggerSophonPlaybookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def trigger_sophon_playbook(
        self,
        request: sophonsoar_20220728_models.TriggerSophonPlaybookRequest,
    ) -> sophonsoar_20220728_models.TriggerSophonPlaybookResponse:
        """
        @summary Triggers a playbook or a command.
        
        @description Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.alibabacloud.com/en/pricing-calculator?_p_lc=1&spm=a2796.7960336.3034855210.1.7adab91arMeIx2#/commodity/vm_intl).
        
        @param request: TriggerSophonPlaybookRequest
        @return: TriggerSophonPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.trigger_sophon_playbook_with_options(request, runtime)

    async def trigger_sophon_playbook_async(
        self,
        request: sophonsoar_20220728_models.TriggerSophonPlaybookRequest,
    ) -> sophonsoar_20220728_models.TriggerSophonPlaybookResponse:
        """
        @summary Triggers a playbook or a command.
        
        @description Before you call this operation, make sure that you understand the billing methods and pricing of Security Orchestration Automation Response (SOAR). For more information, see [Pricing](https://www.alibabacloud.com/en/pricing-calculator?_p_lc=1&spm=a2796.7960336.3034855210.1.7adab91arMeIx2#/commodity/vm_intl).
        
        @param request: TriggerSophonPlaybookRequest
        @return: TriggerSophonPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.trigger_sophon_playbook_with_options_async(request, runtime)

    def verify_playbook_with_options(
        self,
        request: sophonsoar_20220728_models.VerifyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.VerifyPlaybookResponse:
        """
        @summary Checks whether the configuration of the playbook is correct and whether the logic of the orchestration is reasonable.
        
        @param request: VerifyPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.task_flow):
            body['TaskFlow'] = request.task_flow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.VerifyPlaybookResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.VerifyPlaybookResponse(),
                self.execute(params, req, runtime)
            )

    async def verify_playbook_with_options_async(
        self,
        request: sophonsoar_20220728_models.VerifyPlaybookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.VerifyPlaybookResponse:
        """
        @summary Checks whether the configuration of the playbook is correct and whether the logic of the orchestration is reasonable.
        
        @param request: VerifyPlaybookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyPlaybookResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not UtilClient.is_unset(request.task_flow):
            body['TaskFlow'] = request.task_flow
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyPlaybook',
            version='2022-07-28',
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
                sophonsoar_20220728_models.VerifyPlaybookResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.VerifyPlaybookResponse(),
                await self.execute_async(params, req, runtime)
            )

    def verify_playbook(
        self,
        request: sophonsoar_20220728_models.VerifyPlaybookRequest,
    ) -> sophonsoar_20220728_models.VerifyPlaybookResponse:
        """
        @summary Checks whether the configuration of the playbook is correct and whether the logic of the orchestration is reasonable.
        
        @param request: VerifyPlaybookRequest
        @return: VerifyPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_playbook_with_options(request, runtime)

    async def verify_playbook_async(
        self,
        request: sophonsoar_20220728_models.VerifyPlaybookRequest,
    ) -> sophonsoar_20220728_models.VerifyPlaybookResponse:
        """
        @summary Checks whether the configuration of the playbook is correct and whether the logic of the orchestration is reasonable.
        
        @param request: VerifyPlaybookRequest
        @return: VerifyPlaybookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_playbook_with_options_async(request, runtime)

    def verify_python_file_with_options(
        self,
        request: sophonsoar_20220728_models.VerifyPythonFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.VerifyPythonFileResponse:
        """
        @summary Checks whether the syntax of a Python code snippet is correct.
        
        @param request: VerifyPythonFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyPythonFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyPythonFile',
            version='2022-07-28',
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
                sophonsoar_20220728_models.VerifyPythonFileResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.VerifyPythonFileResponse(),
                self.execute(params, req, runtime)
            )

    async def verify_python_file_with_options_async(
        self,
        request: sophonsoar_20220728_models.VerifyPythonFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sophonsoar_20220728_models.VerifyPythonFileResponse:
        """
        @summary Checks whether the syntax of a Python code snippet is correct.
        
        @param request: VerifyPythonFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyPythonFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyPythonFile',
            version='2022-07-28',
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
                sophonsoar_20220728_models.VerifyPythonFileResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                sophonsoar_20220728_models.VerifyPythonFileResponse(),
                await self.execute_async(params, req, runtime)
            )

    def verify_python_file(
        self,
        request: sophonsoar_20220728_models.VerifyPythonFileRequest,
    ) -> sophonsoar_20220728_models.VerifyPythonFileResponse:
        """
        @summary Checks whether the syntax of a Python code snippet is correct.
        
        @param request: VerifyPythonFileRequest
        @return: VerifyPythonFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_python_file_with_options(request, runtime)

    async def verify_python_file_async(
        self,
        request: sophonsoar_20220728_models.VerifyPythonFileRequest,
    ) -> sophonsoar_20220728_models.VerifyPythonFileResponse:
        """
        @summary Checks whether the syntax of a Python code snippet is correct.
        
        @param request: VerifyPythonFileRequest
        @return: VerifyPythonFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_python_file_with_options_async(request, runtime)
