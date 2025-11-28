# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_lto20210707 import models as lto_20210707_models
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
        self._endpoint = self.get_endpoint('lto', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_baa_sant_chain_biz_chain_with_options(
        self,
        request: lto_20210707_models.AddBaaSAntChainBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddBaaSAntChainBizChainResponse:
        """
        @param request: AddBaaSAntChainBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddBaaSAntChainBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baa_sant_chain_chain_id):
            query['BaaSAntChainChainId'] = request.baa_sant_chain_chain_id
        if not UtilClient.is_unset(request.baa_sant_chain_consortium_id):
            query['BaaSAntChainConsortiumId'] = request.baa_sant_chain_consortium_id
        if not UtilClient.is_unset(request.ca_cert):
            query['CaCert'] = request.ca_cert
        if not UtilClient.is_unset(request.ca_cert_password):
            query['CaCertPassword'] = request.ca_cert_password
        if not UtilClient.is_unset(request.client_cert):
            query['ClientCert'] = request.client_cert
        if not UtilClient.is_unset(request.client_key):
            query['ClientKey'] = request.client_key
        if not UtilClient.is_unset(request.client_key_password):
            query['ClientKeyPassword'] = request.client_key_password
        if not UtilClient.is_unset(request.contract_template_id_list):
            query['ContractTemplateIdList'] = request.contract_template_id_list
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.node_name_list):
            query['NodeNameList'] = request.node_name_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_key):
            query['UserKey'] = request.user_key
        if not UtilClient.is_unset(request.user_key_password):
            query['UserKeyPassword'] = request.user_key_password
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBaaSAntChainBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddBaaSAntChainBizChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_baa_sant_chain_biz_chain_with_options_async(
        self,
        request: lto_20210707_models.AddBaaSAntChainBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddBaaSAntChainBizChainResponse:
        """
        @param request: AddBaaSAntChainBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddBaaSAntChainBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baa_sant_chain_chain_id):
            query['BaaSAntChainChainId'] = request.baa_sant_chain_chain_id
        if not UtilClient.is_unset(request.baa_sant_chain_consortium_id):
            query['BaaSAntChainConsortiumId'] = request.baa_sant_chain_consortium_id
        if not UtilClient.is_unset(request.ca_cert):
            query['CaCert'] = request.ca_cert
        if not UtilClient.is_unset(request.ca_cert_password):
            query['CaCertPassword'] = request.ca_cert_password
        if not UtilClient.is_unset(request.client_cert):
            query['ClientCert'] = request.client_cert
        if not UtilClient.is_unset(request.client_key):
            query['ClientKey'] = request.client_key
        if not UtilClient.is_unset(request.client_key_password):
            query['ClientKeyPassword'] = request.client_key_password
        if not UtilClient.is_unset(request.contract_template_id_list):
            query['ContractTemplateIdList'] = request.contract_template_id_list
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.node_name_list):
            query['NodeNameList'] = request.node_name_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_key):
            query['UserKey'] = request.user_key
        if not UtilClient.is_unset(request.user_key_password):
            query['UserKeyPassword'] = request.user_key_password
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBaaSAntChainBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddBaaSAntChainBizChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_baa_sant_chain_biz_chain(
        self,
        request: lto_20210707_models.AddBaaSAntChainBizChainRequest,
    ) -> lto_20210707_models.AddBaaSAntChainBizChainResponse:
        """
        @param request: AddBaaSAntChainBizChainRequest
        @return: AddBaaSAntChainBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_baa_sant_chain_biz_chain_with_options(request, runtime)

    async def add_baa_sant_chain_biz_chain_async(
        self,
        request: lto_20210707_models.AddBaaSAntChainBizChainRequest,
    ) -> lto_20210707_models.AddBaaSAntChainBizChainResponse:
        """
        @param request: AddBaaSAntChainBizChainRequest
        @return: AddBaaSAntChainBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_baa_sant_chain_biz_chain_with_options_async(request, runtime)

    def add_baa_sfabric_biz_chain_with_options(
        self,
        request: lto_20210707_models.AddBaaSFabricBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddBaaSFabricBizChainResponse:
        """
        @param request: AddBaaSFabricBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddBaaSFabricBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baa_sfabric_channel_id):
            query['BaaSFabricChannelId'] = request.baa_sfabric_channel_id
        if not UtilClient.is_unset(request.baa_sfabric_consortium_id):
            query['BaaSFabricConsortiumId'] = request.baa_sfabric_consortium_id
        if not UtilClient.is_unset(request.baa_sfabric_organization_id):
            query['BaaSFabricOrganizationId'] = request.baa_sfabric_organization_id
        if not UtilClient.is_unset(request.contract_template_id_list):
            query['ContractTemplateIdList'] = request.contract_template_id_list
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBaaSFabricBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddBaaSFabricBizChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_baa_sfabric_biz_chain_with_options_async(
        self,
        request: lto_20210707_models.AddBaaSFabricBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddBaaSFabricBizChainResponse:
        """
        @param request: AddBaaSFabricBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddBaaSFabricBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baa_sfabric_channel_id):
            query['BaaSFabricChannelId'] = request.baa_sfabric_channel_id
        if not UtilClient.is_unset(request.baa_sfabric_consortium_id):
            query['BaaSFabricConsortiumId'] = request.baa_sfabric_consortium_id
        if not UtilClient.is_unset(request.baa_sfabric_organization_id):
            query['BaaSFabricOrganizationId'] = request.baa_sfabric_organization_id
        if not UtilClient.is_unset(request.contract_template_id_list):
            query['ContractTemplateIdList'] = request.contract_template_id_list
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBaaSFabricBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddBaaSFabricBizChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_baa_sfabric_biz_chain(
        self,
        request: lto_20210707_models.AddBaaSFabricBizChainRequest,
    ) -> lto_20210707_models.AddBaaSFabricBizChainResponse:
        """
        @param request: AddBaaSFabricBizChainRequest
        @return: AddBaaSFabricBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_baa_sfabric_biz_chain_with_options(request, runtime)

    async def add_baa_sfabric_biz_chain_async(
        self,
        request: lto_20210707_models.AddBaaSFabricBizChainRequest,
    ) -> lto_20210707_models.AddBaaSFabricBizChainResponse:
        """
        @param request: AddBaaSFabricBizChainRequest
        @return: AddBaaSFabricBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_baa_sfabric_biz_chain_with_options_async(request, runtime)

    def add_bsn_fabric_biz_chain_with_options(
        self,
        request: lto_20210707_models.AddBsnFabricBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddBsnFabricBizChainResponse:
        """
        @param request: AddBsnFabricBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddBsnFabricBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.node_list):
            query['NodeList'] = request.node_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_code):
            query['UserCode'] = request.user_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBsnFabricBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddBsnFabricBizChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_bsn_fabric_biz_chain_with_options_async(
        self,
        request: lto_20210707_models.AddBsnFabricBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddBsnFabricBizChainResponse:
        """
        @param request: AddBsnFabricBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddBsnFabricBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.node_list):
            query['NodeList'] = request.node_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.user_code):
            query['UserCode'] = request.user_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBsnFabricBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddBsnFabricBizChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_bsn_fabric_biz_chain(
        self,
        request: lto_20210707_models.AddBsnFabricBizChainRequest,
    ) -> lto_20210707_models.AddBsnFabricBizChainResponse:
        """
        @param request: AddBsnFabricBizChainRequest
        @return: AddBsnFabricBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_bsn_fabric_biz_chain_with_options(request, runtime)

    async def add_bsn_fabric_biz_chain_async(
        self,
        request: lto_20210707_models.AddBsnFabricBizChainRequest,
    ) -> lto_20210707_models.AddBsnFabricBizChainResponse:
        """
        @param request: AddBsnFabricBizChainRequest
        @return: AddBsnFabricBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_bsn_fabric_biz_chain_with_options_async(request, runtime)

    def add_device_group_with_options(
        self,
        request: lto_20210707_models.AddDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddDeviceGroupResponse:
        """
        @summary 添加设备组
        
        @param request: AddDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorized_count):
            query['AuthorizedCount'] = request.authorized_count
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDeviceGroup',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_device_group_with_options_async(
        self,
        request: lto_20210707_models.AddDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddDeviceGroupResponse:
        """
        @summary 添加设备组
        
        @param request: AddDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorized_count):
            query['AuthorizedCount'] = request.authorized_count
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDeviceGroup',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_device_group(
        self,
        request: lto_20210707_models.AddDeviceGroupRequest,
    ) -> lto_20210707_models.AddDeviceGroupResponse:
        """
        @summary 添加设备组
        
        @param request: AddDeviceGroupRequest
        @return: AddDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_device_group_with_options(request, runtime)

    async def add_device_group_async(
        self,
        request: lto_20210707_models.AddDeviceGroupRequest,
    ) -> lto_20210707_models.AddDeviceGroupResponse:
        """
        @summary 添加设备组
        
        @param request: AddDeviceGroupRequest
        @return: AddDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_device_group_with_options_async(request, runtime)

    def add_member_with_options(
        self,
        request: lto_20210707_models.AddMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddMemberResponse:
        """
        @summary 添加成员
        
        @param request: AddMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorized_count):
            query['AuthorizedCount'] = request.authorized_count
        if not UtilClient.is_unset(request.authorized_device_count):
            query['AuthorizedDeviceCount'] = request.authorized_device_count
        if not UtilClient.is_unset(request.contactor):
            query['Contactor'] = request.contactor
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.telephony):
            query['Telephony'] = request.telephony
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_member_with_options_async(
        self,
        request: lto_20210707_models.AddMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddMemberResponse:
        """
        @summary 添加成员
        
        @param request: AddMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorized_count):
            query['AuthorizedCount'] = request.authorized_count
        if not UtilClient.is_unset(request.authorized_device_count):
            query['AuthorizedDeviceCount'] = request.authorized_device_count
        if not UtilClient.is_unset(request.contactor):
            query['Contactor'] = request.contactor
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.telephony):
            query['Telephony'] = request.telephony
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_member(
        self,
        request: lto_20210707_models.AddMemberRequest,
    ) -> lto_20210707_models.AddMemberResponse:
        """
        @summary 添加成员
        
        @param request: AddMemberRequest
        @return: AddMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_member_with_options(request, runtime)

    async def add_member_async(
        self,
        request: lto_20210707_models.AddMemberRequest,
    ) -> lto_20210707_models.AddMemberResponse:
        """
        @summary 添加成员
        
        @param request: AddMemberRequest
        @return: AddMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_member_with_options_async(request, runtime)

    def add_privacy_rule_with_options(
        self,
        request: lto_20210707_models.AddPrivacyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddPrivacyRuleResponse:
        """
        @param request: AddPrivacyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPrivacyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alg_impl):
            query['AlgImpl'] = request.alg_impl
        if not UtilClient.is_unset(request.alg_type):
            query['AlgType'] = request.alg_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrivacyRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddPrivacyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_privacy_rule_with_options_async(
        self,
        request: lto_20210707_models.AddPrivacyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddPrivacyRuleResponse:
        """
        @param request: AddPrivacyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPrivacyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alg_impl):
            query['AlgImpl'] = request.alg_impl
        if not UtilClient.is_unset(request.alg_type):
            query['AlgType'] = request.alg_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrivacyRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddPrivacyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_privacy_rule(
        self,
        request: lto_20210707_models.AddPrivacyRuleRequest,
    ) -> lto_20210707_models.AddPrivacyRuleResponse:
        """
        @param request: AddPrivacyRuleRequest
        @return: AddPrivacyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_privacy_rule_with_options(request, runtime)

    async def add_privacy_rule_async(
        self,
        request: lto_20210707_models.AddPrivacyRuleRequest,
    ) -> lto_20210707_models.AddPrivacyRuleResponse:
        """
        @param request: AddPrivacyRuleRequest
        @return: AddPrivacyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_privacy_rule_with_options_async(request, runtime)

    def add_route_rule_with_options(
        self,
        request: lto_20210707_models.AddRouteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddRouteRuleResponse:
        """
        @param request: AddRouteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddRouteRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.chain_up_mode):
            query['ChainUpMode'] = request.chain_up_mode
        if not UtilClient.is_unset(request.contract_name):
            query['ContractName'] = request.contract_name
        if not UtilClient.is_unset(request.contract_template_id):
            query['ContractTemplateId'] = request.contract_template_id
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.invoke_type):
            query['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.privacy_rule_id):
            query['PrivacyRuleId'] = request.privacy_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRouteRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_route_rule_with_options_async(
        self,
        request: lto_20210707_models.AddRouteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AddRouteRuleResponse:
        """
        @param request: AddRouteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddRouteRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.chain_up_mode):
            query['ChainUpMode'] = request.chain_up_mode
        if not UtilClient.is_unset(request.contract_name):
            query['ContractName'] = request.contract_name
        if not UtilClient.is_unset(request.contract_template_id):
            query['ContractTemplateId'] = request.contract_template_id
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.invoke_type):
            query['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.privacy_rule_id):
            query['PrivacyRuleId'] = request.privacy_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRouteRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AddRouteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_route_rule(
        self,
        request: lto_20210707_models.AddRouteRuleRequest,
    ) -> lto_20210707_models.AddRouteRuleResponse:
        """
        @param request: AddRouteRuleRequest
        @return: AddRouteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_route_rule_with_options(request, runtime)

    async def add_route_rule_async(
        self,
        request: lto_20210707_models.AddRouteRuleRequest,
    ) -> lto_20210707_models.AddRouteRuleResponse:
        """
        @param request: AddRouteRuleRequest
        @return: AddRouteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_route_rule_with_options_async(request, runtime)

    def agree_member_access_with_options(
        self,
        request: lto_20210707_models.AgreeMemberAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AgreeMemberAccessResponse:
        """
        @summary 成员同意接入
        
        @param request: AgreeMemberAccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AgreeMemberAccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AgreeMemberAccess',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AgreeMemberAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def agree_member_access_with_options_async(
        self,
        request: lto_20210707_models.AgreeMemberAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AgreeMemberAccessResponse:
        """
        @summary 成员同意接入
        
        @param request: AgreeMemberAccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AgreeMemberAccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AgreeMemberAccess',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AgreeMemberAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def agree_member_access(
        self,
        request: lto_20210707_models.AgreeMemberAccessRequest,
    ) -> lto_20210707_models.AgreeMemberAccessResponse:
        """
        @summary 成员同意接入
        
        @param request: AgreeMemberAccessRequest
        @return: AgreeMemberAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.agree_member_access_with_options(request, runtime)

    async def agree_member_access_async(
        self,
        request: lto_20210707_models.AgreeMemberAccessRequest,
    ) -> lto_20210707_models.AgreeMemberAccessResponse:
        """
        @summary 成员同意接入
        
        @param request: AgreeMemberAccessRequest
        @return: AgreeMemberAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.agree_member_access_with_options_async(request, runtime)

    def authorize_baa_swith_options(
        self,
        request: lto_20210707_models.AuthorizeBaaSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AuthorizeBaaSResponse:
        """
        @param request: AuthorizeBaaSRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeBaaSResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeBaaS',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AuthorizeBaaSResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_baa_swith_options_async(
        self,
        request: lto_20210707_models.AuthorizeBaaSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AuthorizeBaaSResponse:
        """
        @param request: AuthorizeBaaSRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeBaaSResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeBaaS',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AuthorizeBaaSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_baa_s(
        self,
        request: lto_20210707_models.AuthorizeBaaSRequest,
    ) -> lto_20210707_models.AuthorizeBaaSResponse:
        """
        @param request: AuthorizeBaaSRequest
        @return: AuthorizeBaaSResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.authorize_baa_swith_options(request, runtime)

    async def authorize_baa_s_async(
        self,
        request: lto_20210707_models.AuthorizeBaaSRequest,
    ) -> lto_20210707_models.AuthorizeBaaSResponse:
        """
        @param request: AuthorizeBaaSRequest
        @return: AuthorizeBaaSResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.authorize_baa_swith_options_async(request, runtime)

    def authorize_device_group_biz_chain_with_options(
        self,
        request: lto_20210707_models.AuthorizeDeviceGroupBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AuthorizeDeviceGroupBizChainResponse:
        """
        @param request: AuthorizeDeviceGroupBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeDeviceGroupBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id_list):
            query['BizChainIdList'] = request.biz_chain_id_list
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeDeviceGroupBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AuthorizeDeviceGroupBizChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_device_group_biz_chain_with_options_async(
        self,
        request: lto_20210707_models.AuthorizeDeviceGroupBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AuthorizeDeviceGroupBizChainResponse:
        """
        @param request: AuthorizeDeviceGroupBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeDeviceGroupBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id_list):
            query['BizChainIdList'] = request.biz_chain_id_list
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeDeviceGroupBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AuthorizeDeviceGroupBizChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_device_group_biz_chain(
        self,
        request: lto_20210707_models.AuthorizeDeviceGroupBizChainRequest,
    ) -> lto_20210707_models.AuthorizeDeviceGroupBizChainResponse:
        """
        @param request: AuthorizeDeviceGroupBizChainRequest
        @return: AuthorizeDeviceGroupBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.authorize_device_group_biz_chain_with_options(request, runtime)

    async def authorize_device_group_biz_chain_async(
        self,
        request: lto_20210707_models.AuthorizeDeviceGroupBizChainRequest,
    ) -> lto_20210707_models.AuthorizeDeviceGroupBizChainResponse:
        """
        @param request: AuthorizeDeviceGroupBizChainRequest
        @return: AuthorizeDeviceGroupBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.authorize_device_group_biz_chain_with_options_async(request, runtime)

    def authorize_member_biz_chain_with_options(
        self,
        request: lto_20210707_models.AuthorizeMemberBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AuthorizeMemberBizChainResponse:
        """
        @param request: AuthorizeMemberBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeMemberBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_info):
            query['BizChainInfo'] = request.biz_chain_info
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeMemberBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AuthorizeMemberBizChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_member_biz_chain_with_options_async(
        self,
        request: lto_20210707_models.AuthorizeMemberBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.AuthorizeMemberBizChainResponse:
        """
        @param request: AuthorizeMemberBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeMemberBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_info):
            query['BizChainInfo'] = request.biz_chain_info
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeMemberBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.AuthorizeMemberBizChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_member_biz_chain(
        self,
        request: lto_20210707_models.AuthorizeMemberBizChainRequest,
    ) -> lto_20210707_models.AuthorizeMemberBizChainResponse:
        """
        @param request: AuthorizeMemberBizChainRequest
        @return: AuthorizeMemberBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.authorize_member_biz_chain_with_options(request, runtime)

    async def authorize_member_biz_chain_async(
        self,
        request: lto_20210707_models.AuthorizeMemberBizChainRequest,
    ) -> lto_20210707_models.AuthorizeMemberBizChainResponse:
        """
        @param request: AuthorizeMemberBizChainRequest
        @return: AuthorizeMemberBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.authorize_member_biz_chain_with_options_async(request, runtime)

    def delete_privacy_rule_with_options(
        self,
        request: lto_20210707_models.DeletePrivacyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DeletePrivacyRuleResponse:
        """
        @param request: DeletePrivacyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrivacyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.privacy_rule_id):
            query['PrivacyRuleId'] = request.privacy_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrivacyRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DeletePrivacyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_privacy_rule_with_options_async(
        self,
        request: lto_20210707_models.DeletePrivacyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DeletePrivacyRuleResponse:
        """
        @param request: DeletePrivacyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrivacyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.privacy_rule_id):
            query['PrivacyRuleId'] = request.privacy_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrivacyRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DeletePrivacyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_privacy_rule(
        self,
        request: lto_20210707_models.DeletePrivacyRuleRequest,
    ) -> lto_20210707_models.DeletePrivacyRuleResponse:
        """
        @param request: DeletePrivacyRuleRequest
        @return: DeletePrivacyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_privacy_rule_with_options(request, runtime)

    async def delete_privacy_rule_async(
        self,
        request: lto_20210707_models.DeletePrivacyRuleRequest,
    ) -> lto_20210707_models.DeletePrivacyRuleResponse:
        """
        @param request: DeletePrivacyRuleRequest
        @return: DeletePrivacyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_privacy_rule_with_options_async(request, runtime)

    def delete_route_rule_with_options(
        self,
        request: lto_20210707_models.DeleteRouteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DeleteRouteRuleResponse:
        """
        @param request: DeleteRouteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRouteRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_rule_id):
            query['RouteRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRouteRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DeleteRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_route_rule_with_options_async(
        self,
        request: lto_20210707_models.DeleteRouteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DeleteRouteRuleResponse:
        """
        @param request: DeleteRouteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRouteRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_rule_id):
            query['RouteRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRouteRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DeleteRouteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_route_rule(
        self,
        request: lto_20210707_models.DeleteRouteRuleRequest,
    ) -> lto_20210707_models.DeleteRouteRuleResponse:
        """
        @param request: DeleteRouteRuleRequest
        @return: DeleteRouteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_route_rule_with_options(request, runtime)

    async def delete_route_rule_async(
        self,
        request: lto_20210707_models.DeleteRouteRuleRequest,
    ) -> lto_20210707_models.DeleteRouteRuleResponse:
        """
        @param request: DeleteRouteRuleRequest
        @return: DeleteRouteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_route_rule_with_options_async(request, runtime)

    def denied_member_access_with_options(
        self,
        request: lto_20210707_models.DeniedMemberAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DeniedMemberAccessResponse:
        """
        @summary 成员拒绝接入
        
        @param request: DeniedMemberAccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeniedMemberAccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeniedMemberAccess',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DeniedMemberAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def denied_member_access_with_options_async(
        self,
        request: lto_20210707_models.DeniedMemberAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DeniedMemberAccessResponse:
        """
        @summary 成员拒绝接入
        
        @param request: DeniedMemberAccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeniedMemberAccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_account_id):
            query['MemberAccountId'] = request.member_account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeniedMemberAccess',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DeniedMemberAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def denied_member_access(
        self,
        request: lto_20210707_models.DeniedMemberAccessRequest,
    ) -> lto_20210707_models.DeniedMemberAccessResponse:
        """
        @summary 成员拒绝接入
        
        @param request: DeniedMemberAccessRequest
        @return: DeniedMemberAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.denied_member_access_with_options(request, runtime)

    async def denied_member_access_async(
        self,
        request: lto_20210707_models.DeniedMemberAccessRequest,
    ) -> lto_20210707_models.DeniedMemberAccessResponse:
        """
        @summary 成员拒绝接入
        
        @param request: DeniedMemberAccessRequest
        @return: DeniedMemberAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.denied_member_access_with_options_async(request, runtime)

    def describe_account_role_with_options(
        self,
        request: lto_20210707_models.DescribeAccountRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeAccountRoleResponse:
        """
        @param request: DescribeAccountRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountRole',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeAccountRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_role_with_options_async(
        self,
        request: lto_20210707_models.DescribeAccountRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeAccountRoleResponse:
        """
        @param request: DescribeAccountRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountRole',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeAccountRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_role(
        self,
        request: lto_20210707_models.DescribeAccountRoleRequest,
    ) -> lto_20210707_models.DescribeAccountRoleResponse:
        """
        @param request: DescribeAccountRoleRequest
        @return: DescribeAccountRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_role_with_options(request, runtime)

    async def describe_account_role_async(
        self,
        request: lto_20210707_models.DescribeAccountRoleRequest,
    ) -> lto_20210707_models.DescribeAccountRoleResponse:
        """
        @param request: DescribeAccountRoleRequest
        @return: DescribeAccountRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_role_with_options_async(request, runtime)

    def describe_admin_info_with_options(
        self,
        request: lto_20210707_models.DescribeAdminInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeAdminInfoResponse:
        """
        @summary 查询管理方信息
        
        @param request: DescribeAdminInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdminInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdminInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeAdminInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_admin_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeAdminInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeAdminInfoResponse:
        """
        @summary 查询管理方信息
        
        @param request: DescribeAdminInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdminInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdminInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeAdminInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_admin_info(
        self,
        request: lto_20210707_models.DescribeAdminInfoRequest,
    ) -> lto_20210707_models.DescribeAdminInfoResponse:
        """
        @summary 查询管理方信息
        
        @param request: DescribeAdminInfoRequest
        @return: DescribeAdminInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_admin_info_with_options(request, runtime)

    async def describe_admin_info_async(
        self,
        request: lto_20210707_models.DescribeAdminInfoRequest,
    ) -> lto_20210707_models.DescribeAdminInfoResponse:
        """
        @summary 查询管理方信息
        
        @param request: DescribeAdminInfoRequest
        @return: DescribeAdminInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_admin_info_with_options_async(request, runtime)

    def describe_biz_chain_stat_info_with_options(
        self,
        request: lto_20210707_models.DescribeBizChainStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeBizChainStatInfoResponse:
        """
        @param request: DescribeBizChainStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBizChainStatInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizChainStatInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeBizChainStatInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_biz_chain_stat_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeBizChainStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeBizChainStatInfoResponse:
        """
        @param request: DescribeBizChainStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBizChainStatInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBizChainStatInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeBizChainStatInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_biz_chain_stat_info(
        self,
        request: lto_20210707_models.DescribeBizChainStatInfoRequest,
    ) -> lto_20210707_models.DescribeBizChainStatInfoResponse:
        """
        @param request: DescribeBizChainStatInfoRequest
        @return: DescribeBizChainStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_chain_stat_info_with_options(request, runtime)

    async def describe_biz_chain_stat_info_async(
        self,
        request: lto_20210707_models.DescribeBizChainStatInfoRequest,
    ) -> lto_20210707_models.DescribeBizChainStatInfoResponse:
        """
        @param request: DescribeBizChainStatInfoRequest
        @return: DescribeBizChainStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_biz_chain_stat_info_with_options_async(request, runtime)

    def describe_dashboard_api_info_with_options(
        self,
        request: lto_20210707_models.DescribeDashboardApiInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeDashboardApiInfoResponse:
        """
        @summary 查询概览API信息
        
        @param request: DescribeDashboardApiInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDashboardApiInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboardApiInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeDashboardApiInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dashboard_api_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeDashboardApiInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeDashboardApiInfoResponse:
        """
        @summary 查询概览API信息
        
        @param request: DescribeDashboardApiInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDashboardApiInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboardApiInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeDashboardApiInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dashboard_api_info(
        self,
        request: lto_20210707_models.DescribeDashboardApiInfoRequest,
    ) -> lto_20210707_models.DescribeDashboardApiInfoResponse:
        """
        @summary 查询概览API信息
        
        @param request: DescribeDashboardApiInfoRequest
        @return: DescribeDashboardApiInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dashboard_api_info_with_options(request, runtime)

    async def describe_dashboard_api_info_async(
        self,
        request: lto_20210707_models.DescribeDashboardApiInfoRequest,
    ) -> lto_20210707_models.DescribeDashboardApiInfoResponse:
        """
        @summary 查询概览API信息
        
        @param request: DescribeDashboardApiInfoRequest
        @return: DescribeDashboardApiInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dashboard_api_info_with_options_async(request, runtime)

    def describe_dashboard_base_info_with_options(
        self,
        request: lto_20210707_models.DescribeDashboardBaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeDashboardBaseInfoResponse:
        """
        @summary 查询概览信息
        
        @param request: DescribeDashboardBaseInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDashboardBaseInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboardBaseInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeDashboardBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dashboard_base_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeDashboardBaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeDashboardBaseInfoResponse:
        """
        @summary 查询概览信息
        
        @param request: DescribeDashboardBaseInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDashboardBaseInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboardBaseInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeDashboardBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dashboard_base_info(
        self,
        request: lto_20210707_models.DescribeDashboardBaseInfoRequest,
    ) -> lto_20210707_models.DescribeDashboardBaseInfoResponse:
        """
        @summary 查询概览信息
        
        @param request: DescribeDashboardBaseInfoRequest
        @return: DescribeDashboardBaseInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dashboard_base_info_with_options(request, runtime)

    async def describe_dashboard_base_info_async(
        self,
        request: lto_20210707_models.DescribeDashboardBaseInfoRequest,
    ) -> lto_20210707_models.DescribeDashboardBaseInfoResponse:
        """
        @summary 查询概览信息
        
        @param request: DescribeDashboardBaseInfoRequest
        @return: DescribeDashboardBaseInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dashboard_base_info_with_options_async(request, runtime)

    def describe_dashboard_device_info_with_options(
        self,
        request: lto_20210707_models.DescribeDashboardDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeDashboardDeviceInfoResponse:
        """
        @summary 查询概览设备信息
        
        @param request: DescribeDashboardDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDashboardDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboardDeviceInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeDashboardDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dashboard_device_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeDashboardDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeDashboardDeviceInfoResponse:
        """
        @summary 查询概览设备信息
        
        @param request: DescribeDashboardDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDashboardDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboardDeviceInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeDashboardDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dashboard_device_info(
        self,
        request: lto_20210707_models.DescribeDashboardDeviceInfoRequest,
    ) -> lto_20210707_models.DescribeDashboardDeviceInfoResponse:
        """
        @summary 查询概览设备信息
        
        @param request: DescribeDashboardDeviceInfoRequest
        @return: DescribeDashboardDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dashboard_device_info_with_options(request, runtime)

    async def describe_dashboard_device_info_async(
        self,
        request: lto_20210707_models.DescribeDashboardDeviceInfoRequest,
    ) -> lto_20210707_models.DescribeDashboardDeviceInfoResponse:
        """
        @summary 查询概览设备信息
        
        @param request: DescribeDashboardDeviceInfoRequest
        @return: DescribeDashboardDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dashboard_device_info_with_options_async(request, runtime)

    def describe_dashboard_member_api_info_with_options(
        self,
        request: lto_20210707_models.DescribeDashboardMemberApiInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeDashboardMemberApiInfoResponse:
        """
        @summary 查询概览成员API信息
        
        @param request: DescribeDashboardMemberApiInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDashboardMemberApiInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboardMemberApiInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeDashboardMemberApiInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dashboard_member_api_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeDashboardMemberApiInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeDashboardMemberApiInfoResponse:
        """
        @summary 查询概览成员API信息
        
        @param request: DescribeDashboardMemberApiInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDashboardMemberApiInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboardMemberApiInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeDashboardMemberApiInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dashboard_member_api_info(
        self,
        request: lto_20210707_models.DescribeDashboardMemberApiInfoRequest,
    ) -> lto_20210707_models.DescribeDashboardMemberApiInfoResponse:
        """
        @summary 查询概览成员API信息
        
        @param request: DescribeDashboardMemberApiInfoRequest
        @return: DescribeDashboardMemberApiInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dashboard_member_api_info_with_options(request, runtime)

    async def describe_dashboard_member_api_info_async(
        self,
        request: lto_20210707_models.DescribeDashboardMemberApiInfoRequest,
    ) -> lto_20210707_models.DescribeDashboardMemberApiInfoResponse:
        """
        @summary 查询概览成员API信息
        
        @param request: DescribeDashboardMemberApiInfoRequest
        @return: DescribeDashboardMemberApiInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dashboard_member_api_info_with_options_async(request, runtime)

    def describe_dashboard_member_device_info_with_options(
        self,
        request: lto_20210707_models.DescribeDashboardMemberDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeDashboardMemberDeviceInfoResponse:
        """
        @summary 查询概览成员设备信息
        
        @param request: DescribeDashboardMemberDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDashboardMemberDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboardMemberDeviceInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeDashboardMemberDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dashboard_member_device_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeDashboardMemberDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeDashboardMemberDeviceInfoResponse:
        """
        @summary 查询概览成员设备信息
        
        @param request: DescribeDashboardMemberDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDashboardMemberDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDashboardMemberDeviceInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeDashboardMemberDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dashboard_member_device_info(
        self,
        request: lto_20210707_models.DescribeDashboardMemberDeviceInfoRequest,
    ) -> lto_20210707_models.DescribeDashboardMemberDeviceInfoResponse:
        """
        @summary 查询概览成员设备信息
        
        @param request: DescribeDashboardMemberDeviceInfoRequest
        @return: DescribeDashboardMemberDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dashboard_member_device_info_with_options(request, runtime)

    async def describe_dashboard_member_device_info_async(
        self,
        request: lto_20210707_models.DescribeDashboardMemberDeviceInfoRequest,
    ) -> lto_20210707_models.DescribeDashboardMemberDeviceInfoResponse:
        """
        @summary 查询概览成员设备信息
        
        @param request: DescribeDashboardMemberDeviceInfoRequest
        @return: DescribeDashboardMemberDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dashboard_member_device_info_with_options_async(request, runtime)

    def describe_device_info_with_options(
        self,
        request: lto_20210707_models.DescribeDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeDeviceInfoResponse:
        """
        @summary 查询设备信息
        
        @param request: DescribeDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeDeviceInfoResponse:
        """
        @summary 查询设备信息
        
        @param request: DescribeDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_info(
        self,
        request: lto_20210707_models.DescribeDeviceInfoRequest,
    ) -> lto_20210707_models.DescribeDeviceInfoResponse:
        """
        @summary 查询设备信息
        
        @param request: DescribeDeviceInfoRequest
        @return: DescribeDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_device_info_with_options(request, runtime)

    async def describe_device_info_async(
        self,
        request: lto_20210707_models.DescribeDeviceInfoRequest,
    ) -> lto_20210707_models.DescribeDeviceInfoResponse:
        """
        @summary 查询设备信息
        
        @param request: DescribeDeviceInfoRequest
        @return: DescribeDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_info_with_options_async(request, runtime)

    def describe_edge_stat_info_with_options(
        self,
        request: lto_20210707_models.DescribeEdgeStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeEdgeStatInfoResponse:
        """
        @summary 查询边缘一体机统计信息
        
        @param request: DescribeEdgeStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEdgeStatInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edge_dn):
            query['EdgeDn'] = request.edge_dn
        if not UtilClient.is_unset(request.edge_pk):
            query['EdgePk'] = request.edge_pk
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEdgeStatInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeEdgeStatInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_edge_stat_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeEdgeStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeEdgeStatInfoResponse:
        """
        @summary 查询边缘一体机统计信息
        
        @param request: DescribeEdgeStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEdgeStatInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edge_dn):
            query['EdgeDn'] = request.edge_dn
        if not UtilClient.is_unset(request.edge_pk):
            query['EdgePk'] = request.edge_pk
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEdgeStatInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeEdgeStatInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_edge_stat_info(
        self,
        request: lto_20210707_models.DescribeEdgeStatInfoRequest,
    ) -> lto_20210707_models.DescribeEdgeStatInfoResponse:
        """
        @summary 查询边缘一体机统计信息
        
        @param request: DescribeEdgeStatInfoRequest
        @return: DescribeEdgeStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_edge_stat_info_with_options(request, runtime)

    async def describe_edge_stat_info_async(
        self,
        request: lto_20210707_models.DescribeEdgeStatInfoRequest,
    ) -> lto_20210707_models.DescribeEdgeStatInfoResponse:
        """
        @summary 查询边缘一体机统计信息
        
        @param request: DescribeEdgeStatInfoRequest
        @return: DescribeEdgeStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_edge_stat_info_with_options_async(request, runtime)

    def describe_member_biz_chain_stat_info_with_options(
        self,
        request: lto_20210707_models.DescribeMemberBizChainStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeMemberBizChainStatInfoResponse:
        """
        @param request: DescribeMemberBizChainStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMemberBizChainStatInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMemberBizChainStatInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeMemberBizChainStatInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_member_biz_chain_stat_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeMemberBizChainStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeMemberBizChainStatInfoResponse:
        """
        @param request: DescribeMemberBizChainStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMemberBizChainStatInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMemberBizChainStatInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeMemberBizChainStatInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_member_biz_chain_stat_info(
        self,
        request: lto_20210707_models.DescribeMemberBizChainStatInfoRequest,
    ) -> lto_20210707_models.DescribeMemberBizChainStatInfoResponse:
        """
        @param request: DescribeMemberBizChainStatInfoRequest
        @return: DescribeMemberBizChainStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_member_biz_chain_stat_info_with_options(request, runtime)

    async def describe_member_biz_chain_stat_info_async(
        self,
        request: lto_20210707_models.DescribeMemberBizChainStatInfoRequest,
    ) -> lto_20210707_models.DescribeMemberBizChainStatInfoResponse:
        """
        @param request: DescribeMemberBizChainStatInfoRequest
        @return: DescribeMemberBizChainStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_member_biz_chain_stat_info_with_options_async(request, runtime)

    def describe_member_stat_info_with_options(
        self,
        request: lto_20210707_models.DescribeMemberStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeMemberStatInfoResponse:
        """
        @summary 查询统计成员API信息
        
        @param request: DescribeMemberStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMemberStatInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMemberStatInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeMemberStatInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_member_stat_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeMemberStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeMemberStatInfoResponse:
        """
        @summary 查询统计成员API信息
        
        @param request: DescribeMemberStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMemberStatInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMemberStatInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeMemberStatInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_member_stat_info(
        self,
        request: lto_20210707_models.DescribeMemberStatInfoRequest,
    ) -> lto_20210707_models.DescribeMemberStatInfoResponse:
        """
        @summary 查询统计成员API信息
        
        @param request: DescribeMemberStatInfoRequest
        @return: DescribeMemberStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_member_stat_info_with_options(request, runtime)

    async def describe_member_stat_info_async(
        self,
        request: lto_20210707_models.DescribeMemberStatInfoRequest,
    ) -> lto_20210707_models.DescribeMemberStatInfoResponse:
        """
        @summary 查询统计成员API信息
        
        @param request: DescribeMemberStatInfoRequest
        @return: DescribeMemberStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_member_stat_info_with_options_async(request, runtime)

    def describe_member_total_stat_info_with_options(
        self,
        request: lto_20210707_models.DescribeMemberTotalStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeMemberTotalStatInfoResponse:
        """
        @param request: DescribeMemberTotalStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMemberTotalStatInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMemberTotalStatInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeMemberTotalStatInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_member_total_stat_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeMemberTotalStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeMemberTotalStatInfoResponse:
        """
        @param request: DescribeMemberTotalStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMemberTotalStatInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMemberTotalStatInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeMemberTotalStatInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_member_total_stat_info(
        self,
        request: lto_20210707_models.DescribeMemberTotalStatInfoRequest,
    ) -> lto_20210707_models.DescribeMemberTotalStatInfoResponse:
        """
        @param request: DescribeMemberTotalStatInfoRequest
        @return: DescribeMemberTotalStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_member_total_stat_info_with_options(request, runtime)

    async def describe_member_total_stat_info_async(
        self,
        request: lto_20210707_models.DescribeMemberTotalStatInfoRequest,
    ) -> lto_20210707_models.DescribeMemberTotalStatInfoResponse:
        """
        @param request: DescribeMemberTotalStatInfoRequest
        @return: DescribeMemberTotalStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_member_total_stat_info_with_options_async(request, runtime)

    def describe_packge_info_with_options(
        self,
        request: lto_20210707_models.DescribePackgeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribePackgeInfoResponse:
        """
        @param request: DescribePackgeInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePackgeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackgeInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribePackgeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_packge_info_with_options_async(
        self,
        request: lto_20210707_models.DescribePackgeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribePackgeInfoResponse:
        """
        @param request: DescribePackgeInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePackgeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackgeInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribePackgeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_packge_info(
        self,
        request: lto_20210707_models.DescribePackgeInfoRequest,
    ) -> lto_20210707_models.DescribePackgeInfoResponse:
        """
        @param request: DescribePackgeInfoRequest
        @return: DescribePackgeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_packge_info_with_options(request, runtime)

    async def describe_packge_info_async(
        self,
        request: lto_20210707_models.DescribePackgeInfoRequest,
    ) -> lto_20210707_models.DescribePackgeInfoResponse:
        """
        @param request: DescribePackgeInfoRequest
        @return: DescribePackgeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_packge_info_with_options_async(request, runtime)

    def describe_stat_device_info_with_options(
        self,
        request: lto_20210707_models.DescribeStatDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeStatDeviceInfoResponse:
        """
        @summary 查询统计设备信息
        
        @param request: DescribeStatDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStatDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStatDeviceInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeStatDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_stat_device_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeStatDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeStatDeviceInfoResponse:
        """
        @summary 查询统计设备信息
        
        @param request: DescribeStatDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStatDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStatDeviceInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeStatDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_stat_device_info(
        self,
        request: lto_20210707_models.DescribeStatDeviceInfoRequest,
    ) -> lto_20210707_models.DescribeStatDeviceInfoResponse:
        """
        @summary 查询统计设备信息
        
        @param request: DescribeStatDeviceInfoRequest
        @return: DescribeStatDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_stat_device_info_with_options(request, runtime)

    async def describe_stat_device_info_async(
        self,
        request: lto_20210707_models.DescribeStatDeviceInfoRequest,
    ) -> lto_20210707_models.DescribeStatDeviceInfoResponse:
        """
        @summary 查询统计设备信息
        
        @param request: DescribeStatDeviceInfoRequest
        @return: DescribeStatDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_stat_device_info_with_options_async(request, runtime)

    def describe_stat_member_device_info_with_options(
        self,
        request: lto_20210707_models.DescribeStatMemberDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeStatMemberDeviceInfoResponse:
        """
        @summary 查询统计成员设备信息
        
        @param request: DescribeStatMemberDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStatMemberDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStatMemberDeviceInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeStatMemberDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_stat_member_device_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeStatMemberDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeStatMemberDeviceInfoResponse:
        """
        @summary 查询统计成员设备信息
        
        @param request: DescribeStatMemberDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStatMemberDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStatMemberDeviceInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeStatMemberDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_stat_member_device_info(
        self,
        request: lto_20210707_models.DescribeStatMemberDeviceInfoRequest,
    ) -> lto_20210707_models.DescribeStatMemberDeviceInfoResponse:
        """
        @summary 查询统计成员设备信息
        
        @param request: DescribeStatMemberDeviceInfoRequest
        @return: DescribeStatMemberDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_stat_member_device_info_with_options(request, runtime)

    async def describe_stat_member_device_info_async(
        self,
        request: lto_20210707_models.DescribeStatMemberDeviceInfoRequest,
    ) -> lto_20210707_models.DescribeStatMemberDeviceInfoResponse:
        """
        @summary 查询统计成员设备信息
        
        @param request: DescribeStatMemberDeviceInfoRequest
        @return: DescribeStatMemberDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_stat_member_device_info_with_options_async(request, runtime)

    def describe_total_stat_info_with_options(
        self,
        request: lto_20210707_models.DescribeTotalStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeTotalStatInfoResponse:
        """
        @param request: DescribeTotalStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTotalStatInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTotalStatInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeTotalStatInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_total_stat_info_with_options_async(
        self,
        request: lto_20210707_models.DescribeTotalStatInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DescribeTotalStatInfoResponse:
        """
        @param request: DescribeTotalStatInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTotalStatInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTotalStatInfo',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DescribeTotalStatInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_total_stat_info(
        self,
        request: lto_20210707_models.DescribeTotalStatInfoRequest,
    ) -> lto_20210707_models.DescribeTotalStatInfoResponse:
        """
        @param request: DescribeTotalStatInfoRequest
        @return: DescribeTotalStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_total_stat_info_with_options(request, runtime)

    async def describe_total_stat_info_async(
        self,
        request: lto_20210707_models.DescribeTotalStatInfoRequest,
    ) -> lto_20210707_models.DescribeTotalStatInfoResponse:
        """
        @param request: DescribeTotalStatInfoRequest
        @return: DescribeTotalStatInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_total_stat_info_with_options_async(request, runtime)

    def disable_device_with_options(
        self,
        request: lto_20210707_models.DisableDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DisableDeviceResponse:
        """
        @param request: DisableDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDevice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DisableDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_device_with_options_async(
        self,
        request: lto_20210707_models.DisableDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DisableDeviceResponse:
        """
        @param request: DisableDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDevice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DisableDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_device(
        self,
        request: lto_20210707_models.DisableDeviceRequest,
    ) -> lto_20210707_models.DisableDeviceResponse:
        """
        @param request: DisableDeviceRequest
        @return: DisableDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_device_with_options(request, runtime)

    async def disable_device_async(
        self,
        request: lto_20210707_models.DisableDeviceRequest,
    ) -> lto_20210707_models.DisableDeviceResponse:
        """
        @param request: DisableDeviceRequest
        @return: DisableDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_device_with_options_async(request, runtime)

    def disable_device_group_with_options(
        self,
        request: lto_20210707_models.DisableDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DisableDeviceGroupResponse:
        """
        @param request: DisableDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDeviceGroup',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DisableDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_device_group_with_options_async(
        self,
        request: lto_20210707_models.DisableDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DisableDeviceGroupResponse:
        """
        @param request: DisableDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDeviceGroup',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DisableDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_device_group(
        self,
        request: lto_20210707_models.DisableDeviceGroupRequest,
    ) -> lto_20210707_models.DisableDeviceGroupResponse:
        """
        @param request: DisableDeviceGroupRequest
        @return: DisableDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_device_group_with_options(request, runtime)

    async def disable_device_group_async(
        self,
        request: lto_20210707_models.DisableDeviceGroupRequest,
    ) -> lto_20210707_models.DisableDeviceGroupResponse:
        """
        @param request: DisableDeviceGroupRequest
        @return: DisableDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_device_group_with_options_async(request, runtime)

    def download_privacy_key_with_options(
        self,
        request: lto_20210707_models.DownloadPrivacyKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DownloadPrivacyKeyResponse:
        """
        @param request: DownloadPrivacyKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadPrivacyKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadPrivacyKey',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DownloadPrivacyKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_privacy_key_with_options_async(
        self,
        request: lto_20210707_models.DownloadPrivacyKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.DownloadPrivacyKeyResponse:
        """
        @param request: DownloadPrivacyKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DownloadPrivacyKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadPrivacyKey',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.DownloadPrivacyKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_privacy_key(
        self,
        request: lto_20210707_models.DownloadPrivacyKeyRequest,
    ) -> lto_20210707_models.DownloadPrivacyKeyResponse:
        """
        @param request: DownloadPrivacyKeyRequest
        @return: DownloadPrivacyKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.download_privacy_key_with_options(request, runtime)

    async def download_privacy_key_async(
        self,
        request: lto_20210707_models.DownloadPrivacyKeyRequest,
    ) -> lto_20210707_models.DownloadPrivacyKeyResponse:
        """
        @param request: DownloadPrivacyKeyRequest
        @return: DownloadPrivacyKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.download_privacy_key_with_options_async(request, runtime)

    def enable_device_with_options(
        self,
        request: lto_20210707_models.EnableDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.EnableDeviceResponse:
        """
        @param request: EnableDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDevice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.EnableDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_device_with_options_async(
        self,
        request: lto_20210707_models.EnableDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.EnableDeviceResponse:
        """
        @param request: EnableDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDevice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.EnableDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_device(
        self,
        request: lto_20210707_models.EnableDeviceRequest,
    ) -> lto_20210707_models.EnableDeviceResponse:
        """
        @param request: EnableDeviceRequest
        @return: EnableDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_device_with_options(request, runtime)

    async def enable_device_async(
        self,
        request: lto_20210707_models.EnableDeviceRequest,
    ) -> lto_20210707_models.EnableDeviceResponse:
        """
        @param request: EnableDeviceRequest
        @return: EnableDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_device_with_options_async(request, runtime)

    def enable_device_group_with_options(
        self,
        request: lto_20210707_models.EnableDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.EnableDeviceGroupResponse:
        """
        @param request: EnableDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDeviceGroup',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.EnableDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_device_group_with_options_async(
        self,
        request: lto_20210707_models.EnableDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.EnableDeviceGroupResponse:
        """
        @param request: EnableDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDeviceGroup',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.EnableDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_device_group(
        self,
        request: lto_20210707_models.EnableDeviceGroupRequest,
    ) -> lto_20210707_models.EnableDeviceGroupResponse:
        """
        @param request: EnableDeviceGroupRequest
        @return: EnableDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_device_group_with_options(request, runtime)

    async def enable_device_group_async(
        self,
        request: lto_20210707_models.EnableDeviceGroupRequest,
    ) -> lto_20210707_models.EnableDeviceGroupResponse:
        """
        @param request: EnableDeviceGroupRequest
        @return: EnableDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_device_group_with_options_async(request, runtime)

    def freeze_member_with_options(
        self,
        request: lto_20210707_models.FreezeMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.FreezeMemberResponse:
        """
        @param request: FreezeMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FreezeMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FreezeMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.FreezeMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def freeze_member_with_options_async(
        self,
        request: lto_20210707_models.FreezeMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.FreezeMemberResponse:
        """
        @param request: FreezeMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FreezeMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FreezeMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.FreezeMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def freeze_member(
        self,
        request: lto_20210707_models.FreezeMemberRequest,
    ) -> lto_20210707_models.FreezeMemberResponse:
        """
        @param request: FreezeMemberRequest
        @return: FreezeMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.freeze_member_with_options(request, runtime)

    async def freeze_member_async(
        self,
        request: lto_20210707_models.FreezeMemberRequest,
    ) -> lto_20210707_models.FreezeMemberResponse:
        """
        @param request: FreezeMemberRequest
        @return: FreezeMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.freeze_member_with_options_async(request, runtime)

    def get_edge_total_device_count_with_options(
        self,
        request: lto_20210707_models.GetEdgeTotalDeviceCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.GetEdgeTotalDeviceCountResponse:
        """
        @param request: GetEdgeTotalDeviceCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeTotalDeviceCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeTotalDeviceCount',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.GetEdgeTotalDeviceCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_edge_total_device_count_with_options_async(
        self,
        request: lto_20210707_models.GetEdgeTotalDeviceCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.GetEdgeTotalDeviceCountResponse:
        """
        @param request: GetEdgeTotalDeviceCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeTotalDeviceCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeTotalDeviceCount',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.GetEdgeTotalDeviceCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_edge_total_device_count(
        self,
        request: lto_20210707_models.GetEdgeTotalDeviceCountRequest,
    ) -> lto_20210707_models.GetEdgeTotalDeviceCountResponse:
        """
        @param request: GetEdgeTotalDeviceCountRequest
        @return: GetEdgeTotalDeviceCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_edge_total_device_count_with_options(request, runtime)

    async def get_edge_total_device_count_async(
        self,
        request: lto_20210707_models.GetEdgeTotalDeviceCountRequest,
    ) -> lto_20210707_models.GetEdgeTotalDeviceCountResponse:
        """
        @param request: GetEdgeTotalDeviceCountRequest
        @return: GetEdgeTotalDeviceCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_edge_total_device_count_with_options_async(request, runtime)

    def list_all_admin_with_options(
        self,
        request: lto_20210707_models.ListAllAdminRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllAdminResponse:
        """
        @param request: ListAllAdminRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllAdminResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllAdmin',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_admin_with_options_async(
        self,
        request: lto_20210707_models.ListAllAdminRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllAdminResponse:
        """
        @param request: ListAllAdminRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllAdminResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllAdmin',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_admin(
        self,
        request: lto_20210707_models.ListAllAdminRequest,
    ) -> lto_20210707_models.ListAllAdminResponse:
        """
        @param request: ListAllAdminRequest
        @return: ListAllAdminResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_admin_with_options(request, runtime)

    async def list_all_admin_async(
        self,
        request: lto_20210707_models.ListAllAdminRequest,
    ) -> lto_20210707_models.ListAllAdminResponse:
        """
        @param request: ListAllAdminRequest
        @return: ListAllAdminResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_admin_with_options_async(request, runtime)

    def list_all_biz_chain_with_options(
        self,
        request: lto_20210707_models.ListAllBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllBizChainResponse:
        """
        @param request: ListAllBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllBizChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_biz_chain_with_options_async(
        self,
        request: lto_20210707_models.ListAllBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllBizChainResponse:
        """
        @param request: ListAllBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllBizChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_biz_chain(
        self,
        request: lto_20210707_models.ListAllBizChainRequest,
    ) -> lto_20210707_models.ListAllBizChainResponse:
        """
        @param request: ListAllBizChainRequest
        @return: ListAllBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_biz_chain_with_options(request, runtime)

    async def list_all_biz_chain_async(
        self,
        request: lto_20210707_models.ListAllBizChainRequest,
    ) -> lto_20210707_models.ListAllBizChainResponse:
        """
        @param request: ListAllBizChainRequest
        @return: ListAllBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_biz_chain_with_options_async(request, runtime)

    def list_all_biz_chain_contract_with_options(
        self,
        request: lto_20210707_models.ListAllBizChainContractRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllBizChainContractResponse:
        """
        @param request: ListAllBizChainContractRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllBizChainContractResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllBizChainContract',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllBizChainContractResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_biz_chain_contract_with_options_async(
        self,
        request: lto_20210707_models.ListAllBizChainContractRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllBizChainContractResponse:
        """
        @param request: ListAllBizChainContractRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllBizChainContractResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllBizChainContract',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllBizChainContractResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_biz_chain_contract(
        self,
        request: lto_20210707_models.ListAllBizChainContractRequest,
    ) -> lto_20210707_models.ListAllBizChainContractResponse:
        """
        @param request: ListAllBizChainContractRequest
        @return: ListAllBizChainContractResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_biz_chain_contract_with_options(request, runtime)

    async def list_all_biz_chain_contract_async(
        self,
        request: lto_20210707_models.ListAllBizChainContractRequest,
    ) -> lto_20210707_models.ListAllBizChainContractResponse:
        """
        @param request: ListAllBizChainContractRequest
        @return: ListAllBizChainContractResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_biz_chain_contract_with_options_async(request, runtime)

    def list_all_device_group_with_options(
        self,
        request: lto_20210707_models.ListAllDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllDeviceGroupResponse:
        """
        @param request: ListAllDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllDeviceGroup',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_device_group_with_options_async(
        self,
        request: lto_20210707_models.ListAllDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllDeviceGroupResponse:
        """
        @param request: ListAllDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllDeviceGroup',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_device_group(
        self,
        request: lto_20210707_models.ListAllDeviceGroupRequest,
    ) -> lto_20210707_models.ListAllDeviceGroupResponse:
        """
        @param request: ListAllDeviceGroupRequest
        @return: ListAllDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_device_group_with_options(request, runtime)

    async def list_all_device_group_async(
        self,
        request: lto_20210707_models.ListAllDeviceGroupRequest,
    ) -> lto_20210707_models.ListAllDeviceGroupResponse:
        """
        @param request: ListAllDeviceGroupRequest
        @return: ListAllDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_device_group_with_options_async(request, runtime)

    def list_all_member_with_options(
        self,
        request: lto_20210707_models.ListAllMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllMemberResponse:
        """
        @param request: ListAllMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_member_with_options_async(
        self,
        request: lto_20210707_models.ListAllMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllMemberResponse:
        """
        @param request: ListAllMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_member(
        self,
        request: lto_20210707_models.ListAllMemberRequest,
    ) -> lto_20210707_models.ListAllMemberResponse:
        """
        @param request: ListAllMemberRequest
        @return: ListAllMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_member_with_options(request, runtime)

    async def list_all_member_async(
        self,
        request: lto_20210707_models.ListAllMemberRequest,
    ) -> lto_20210707_models.ListAllMemberResponse:
        """
        @param request: ListAllMemberRequest
        @return: ListAllMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_member_with_options_async(request, runtime)

    def list_all_privacy_algorithm_with_options(
        self,
        request: lto_20210707_models.ListAllPrivacyAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllPrivacyAlgorithmResponse:
        """
        @param request: ListAllPrivacyAlgorithmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllPrivacyAlgorithmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllPrivacyAlgorithm',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllPrivacyAlgorithmResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_privacy_algorithm_with_options_async(
        self,
        request: lto_20210707_models.ListAllPrivacyAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllPrivacyAlgorithmResponse:
        """
        @param request: ListAllPrivacyAlgorithmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllPrivacyAlgorithmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllPrivacyAlgorithm',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllPrivacyAlgorithmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_privacy_algorithm(
        self,
        request: lto_20210707_models.ListAllPrivacyAlgorithmRequest,
    ) -> lto_20210707_models.ListAllPrivacyAlgorithmResponse:
        """
        @param request: ListAllPrivacyAlgorithmRequest
        @return: ListAllPrivacyAlgorithmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_privacy_algorithm_with_options(request, runtime)

    async def list_all_privacy_algorithm_async(
        self,
        request: lto_20210707_models.ListAllPrivacyAlgorithmRequest,
    ) -> lto_20210707_models.ListAllPrivacyAlgorithmResponse:
        """
        @param request: ListAllPrivacyAlgorithmRequest
        @return: ListAllPrivacyAlgorithmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_privacy_algorithm_with_options_async(request, runtime)

    def list_all_privacy_rule_with_options(
        self,
        request: lto_20210707_models.ListAllPrivacyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllPrivacyRuleResponse:
        """
        @param request: ListAllPrivacyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllPrivacyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllPrivacyRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllPrivacyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_privacy_rule_with_options_async(
        self,
        request: lto_20210707_models.ListAllPrivacyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllPrivacyRuleResponse:
        """
        @param request: ListAllPrivacyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllPrivacyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllPrivacyRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllPrivacyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_privacy_rule(
        self,
        request: lto_20210707_models.ListAllPrivacyRuleRequest,
    ) -> lto_20210707_models.ListAllPrivacyRuleResponse:
        """
        @param request: ListAllPrivacyRuleRequest
        @return: ListAllPrivacyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_privacy_rule_with_options(request, runtime)

    async def list_all_privacy_rule_async(
        self,
        request: lto_20210707_models.ListAllPrivacyRuleRequest,
    ) -> lto_20210707_models.ListAllPrivacyRuleResponse:
        """
        @param request: ListAllPrivacyRuleRequest
        @return: ListAllPrivacyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_privacy_rule_with_options_async(request, runtime)

    def list_all_product_key_with_options(
        self,
        request: lto_20210707_models.ListAllProductKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllProductKeyResponse:
        """
        @param request: ListAllProductKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllProductKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllProductKey',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllProductKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_product_key_with_options_async(
        self,
        request: lto_20210707_models.ListAllProductKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllProductKeyResponse:
        """
        @param request: ListAllProductKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllProductKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllProductKey',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllProductKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_product_key(
        self,
        request: lto_20210707_models.ListAllProductKeyRequest,
    ) -> lto_20210707_models.ListAllProductKeyResponse:
        """
        @param request: ListAllProductKeyRequest
        @return: ListAllProductKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_product_key_with_options(request, runtime)

    async def list_all_product_key_async(
        self,
        request: lto_20210707_models.ListAllProductKeyRequest,
    ) -> lto_20210707_models.ListAllProductKeyResponse:
        """
        @param request: ListAllProductKeyRequest
        @return: ListAllProductKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_product_key_with_options_async(request, runtime)

    def list_all_system_contract_with_options(
        self,
        request: lto_20210707_models.ListAllSystemContractRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllSystemContractResponse:
        """
        @param request: ListAllSystemContractRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllSystemContractResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_chain_type):
            query['BlockChainType'] = request.block_chain_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllSystemContract',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllSystemContractResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_system_contract_with_options_async(
        self,
        request: lto_20210707_models.ListAllSystemContractRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListAllSystemContractResponse:
        """
        @param request: ListAllSystemContractRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllSystemContractResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.block_chain_type):
            query['BlockChainType'] = request.block_chain_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllSystemContract',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListAllSystemContractResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_system_contract(
        self,
        request: lto_20210707_models.ListAllSystemContractRequest,
    ) -> lto_20210707_models.ListAllSystemContractResponse:
        """
        @param request: ListAllSystemContractRequest
        @return: ListAllSystemContractResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_system_contract_with_options(request, runtime)

    async def list_all_system_contract_async(
        self,
        request: lto_20210707_models.ListAllSystemContractRequest,
    ) -> lto_20210707_models.ListAllSystemContractResponse:
        """
        @param request: ListAllSystemContractRequest
        @return: ListAllSystemContractResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_system_contract_with_options_async(request, runtime)

    def list_baa_sant_chain_with_options(
        self,
        request: lto_20210707_models.ListBaaSAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBaaSAntChainResponse:
        """
        @param request: ListBaaSAntChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBaaSAntChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baa_sant_chain_consortium_id):
            query['BaaSAntChainConsortiumId'] = request.baa_sant_chain_consortium_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBaaSAntChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBaaSAntChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_baa_sant_chain_with_options_async(
        self,
        request: lto_20210707_models.ListBaaSAntChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBaaSAntChainResponse:
        """
        @param request: ListBaaSAntChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBaaSAntChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baa_sant_chain_consortium_id):
            query['BaaSAntChainConsortiumId'] = request.baa_sant_chain_consortium_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBaaSAntChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBaaSAntChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_baa_sant_chain(
        self,
        request: lto_20210707_models.ListBaaSAntChainRequest,
    ) -> lto_20210707_models.ListBaaSAntChainResponse:
        """
        @param request: ListBaaSAntChainRequest
        @return: ListBaaSAntChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_baa_sant_chain_with_options(request, runtime)

    async def list_baa_sant_chain_async(
        self,
        request: lto_20210707_models.ListBaaSAntChainRequest,
    ) -> lto_20210707_models.ListBaaSAntChainResponse:
        """
        @param request: ListBaaSAntChainRequest
        @return: ListBaaSAntChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_baa_sant_chain_with_options_async(request, runtime)

    def list_baa_sant_chain_consortium_with_options(
        self,
        request: lto_20210707_models.ListBaaSAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBaaSAntChainConsortiumResponse:
        """
        @param request: ListBaaSAntChainConsortiumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBaaSAntChainConsortiumResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBaaSAntChainConsortium',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBaaSAntChainConsortiumResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_baa_sant_chain_consortium_with_options_async(
        self,
        request: lto_20210707_models.ListBaaSAntChainConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBaaSAntChainConsortiumResponse:
        """
        @param request: ListBaaSAntChainConsortiumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBaaSAntChainConsortiumResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBaaSAntChainConsortium',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBaaSAntChainConsortiumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_baa_sant_chain_consortium(
        self,
        request: lto_20210707_models.ListBaaSAntChainConsortiumRequest,
    ) -> lto_20210707_models.ListBaaSAntChainConsortiumResponse:
        """
        @param request: ListBaaSAntChainConsortiumRequest
        @return: ListBaaSAntChainConsortiumResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_baa_sant_chain_consortium_with_options(request, runtime)

    async def list_baa_sant_chain_consortium_async(
        self,
        request: lto_20210707_models.ListBaaSAntChainConsortiumRequest,
    ) -> lto_20210707_models.ListBaaSAntChainConsortiumResponse:
        """
        @param request: ListBaaSAntChainConsortiumRequest
        @return: ListBaaSAntChainConsortiumResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_baa_sant_chain_consortium_with_options_async(request, runtime)

    def list_baa_sant_chain_peer_with_options(
        self,
        request: lto_20210707_models.ListBaaSAntChainPeerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBaaSAntChainPeerResponse:
        """
        @param request: ListBaaSAntChainPeerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBaaSAntChainPeerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baa_sant_chain_chain_id):
            query['BaaSAntChainChainId'] = request.baa_sant_chain_chain_id
        if not UtilClient.is_unset(request.baa_sant_chain_consortium_id):
            query['BaaSAntChainConsortiumId'] = request.baa_sant_chain_consortium_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBaaSAntChainPeer',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBaaSAntChainPeerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_baa_sant_chain_peer_with_options_async(
        self,
        request: lto_20210707_models.ListBaaSAntChainPeerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBaaSAntChainPeerResponse:
        """
        @param request: ListBaaSAntChainPeerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBaaSAntChainPeerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baa_sant_chain_chain_id):
            query['BaaSAntChainChainId'] = request.baa_sant_chain_chain_id
        if not UtilClient.is_unset(request.baa_sant_chain_consortium_id):
            query['BaaSAntChainConsortiumId'] = request.baa_sant_chain_consortium_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBaaSAntChainPeer',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBaaSAntChainPeerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_baa_sant_chain_peer(
        self,
        request: lto_20210707_models.ListBaaSAntChainPeerRequest,
    ) -> lto_20210707_models.ListBaaSAntChainPeerResponse:
        """
        @param request: ListBaaSAntChainPeerRequest
        @return: ListBaaSAntChainPeerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_baa_sant_chain_peer_with_options(request, runtime)

    async def list_baa_sant_chain_peer_async(
        self,
        request: lto_20210707_models.ListBaaSAntChainPeerRequest,
    ) -> lto_20210707_models.ListBaaSAntChainPeerResponse:
        """
        @param request: ListBaaSAntChainPeerRequest
        @return: ListBaaSAntChainPeerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_baa_sant_chain_peer_with_options_async(request, runtime)

    def list_baa_sfabric_channel_with_options(
        self,
        request: lto_20210707_models.ListBaaSFabricChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBaaSFabricChannelResponse:
        """
        @param request: ListBaaSFabricChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBaaSFabricChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baa_sfabric_consortium_id):
            query['BaaSFabricConsortiumId'] = request.baa_sfabric_consortium_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBaaSFabricChannel',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBaaSFabricChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_baa_sfabric_channel_with_options_async(
        self,
        request: lto_20210707_models.ListBaaSFabricChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBaaSFabricChannelResponse:
        """
        @param request: ListBaaSFabricChannelRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBaaSFabricChannelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baa_sfabric_consortium_id):
            query['BaaSFabricConsortiumId'] = request.baa_sfabric_consortium_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBaaSFabricChannel',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBaaSFabricChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_baa_sfabric_channel(
        self,
        request: lto_20210707_models.ListBaaSFabricChannelRequest,
    ) -> lto_20210707_models.ListBaaSFabricChannelResponse:
        """
        @param request: ListBaaSFabricChannelRequest
        @return: ListBaaSFabricChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_baa_sfabric_channel_with_options(request, runtime)

    async def list_baa_sfabric_channel_async(
        self,
        request: lto_20210707_models.ListBaaSFabricChannelRequest,
    ) -> lto_20210707_models.ListBaaSFabricChannelResponse:
        """
        @param request: ListBaaSFabricChannelRequest
        @return: ListBaaSFabricChannelResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_baa_sfabric_channel_with_options_async(request, runtime)

    def list_baa_sfabric_consortium_with_options(
        self,
        request: lto_20210707_models.ListBaaSFabricConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBaaSFabricConsortiumResponse:
        """
        @param request: ListBaaSFabricConsortiumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBaaSFabricConsortiumResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBaaSFabricConsortium',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBaaSFabricConsortiumResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_baa_sfabric_consortium_with_options_async(
        self,
        request: lto_20210707_models.ListBaaSFabricConsortiumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBaaSFabricConsortiumResponse:
        """
        @param request: ListBaaSFabricConsortiumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBaaSFabricConsortiumResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBaaSFabricConsortium',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBaaSFabricConsortiumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_baa_sfabric_consortium(
        self,
        request: lto_20210707_models.ListBaaSFabricConsortiumRequest,
    ) -> lto_20210707_models.ListBaaSFabricConsortiumResponse:
        """
        @param request: ListBaaSFabricConsortiumRequest
        @return: ListBaaSFabricConsortiumResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_baa_sfabric_consortium_with_options(request, runtime)

    async def list_baa_sfabric_consortium_async(
        self,
        request: lto_20210707_models.ListBaaSFabricConsortiumRequest,
    ) -> lto_20210707_models.ListBaaSFabricConsortiumResponse:
        """
        @param request: ListBaaSFabricConsortiumRequest
        @return: ListBaaSFabricConsortiumResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_baa_sfabric_consortium_with_options_async(request, runtime)

    def list_baa_sfabric_organization_with_options(
        self,
        request: lto_20210707_models.ListBaaSFabricOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBaaSFabricOrganizationResponse:
        """
        @param request: ListBaaSFabricOrganizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBaaSFabricOrganizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baa_sfabric_channel_id):
            query['BaaSFabricChannelId'] = request.baa_sfabric_channel_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBaaSFabricOrganization',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBaaSFabricOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_baa_sfabric_organization_with_options_async(
        self,
        request: lto_20210707_models.ListBaaSFabricOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBaaSFabricOrganizationResponse:
        """
        @param request: ListBaaSFabricOrganizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBaaSFabricOrganizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baa_sfabric_channel_id):
            query['BaaSFabricChannelId'] = request.baa_sfabric_channel_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBaaSFabricOrganization',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBaaSFabricOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_baa_sfabric_organization(
        self,
        request: lto_20210707_models.ListBaaSFabricOrganizationRequest,
    ) -> lto_20210707_models.ListBaaSFabricOrganizationResponse:
        """
        @param request: ListBaaSFabricOrganizationRequest
        @return: ListBaaSFabricOrganizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_baa_sfabric_organization_with_options(request, runtime)

    async def list_baa_sfabric_organization_async(
        self,
        request: lto_20210707_models.ListBaaSFabricOrganizationRequest,
    ) -> lto_20210707_models.ListBaaSFabricOrganizationResponse:
        """
        @param request: ListBaaSFabricOrganizationRequest
        @return: ListBaaSFabricOrganizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_baa_sfabric_organization_with_options_async(request, runtime)

    def list_biz_chain_with_options(
        self,
        request: lto_20210707_models.ListBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBizChainResponse:
        """
        @param request: ListBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBizChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_biz_chain_with_options_async(
        self,
        request: lto_20210707_models.ListBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBizChainResponse:
        """
        @param request: ListBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBizChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_biz_chain(
        self,
        request: lto_20210707_models.ListBizChainRequest,
    ) -> lto_20210707_models.ListBizChainResponse:
        """
        @param request: ListBizChainRequest
        @return: ListBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_biz_chain_with_options(request, runtime)

    async def list_biz_chain_async(
        self,
        request: lto_20210707_models.ListBizChainRequest,
    ) -> lto_20210707_models.ListBizChainResponse:
        """
        @param request: ListBizChainRequest
        @return: ListBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_biz_chain_with_options_async(request, runtime)

    def list_biz_chain_data_with_options(
        self,
        request: lto_20210707_models.ListBizChainDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBizChainDataResponse:
        """
        @param request: ListBizChainDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBizChainDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.io_tdata_did):
            query['IoTDataDID'] = request.io_tdata_did
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBizChainData',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBizChainDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_biz_chain_data_with_options_async(
        self,
        request: lto_20210707_models.ListBizChainDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListBizChainDataResponse:
        """
        @param request: ListBizChainDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBizChainDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.io_tdata_did):
            query['IoTDataDID'] = request.io_tdata_did
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBizChainData',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListBizChainDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_biz_chain_data(
        self,
        request: lto_20210707_models.ListBizChainDataRequest,
    ) -> lto_20210707_models.ListBizChainDataResponse:
        """
        @param request: ListBizChainDataRequest
        @return: ListBizChainDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_biz_chain_data_with_options(request, runtime)

    async def list_biz_chain_data_async(
        self,
        request: lto_20210707_models.ListBizChainDataRequest,
    ) -> lto_20210707_models.ListBizChainDataResponse:
        """
        @param request: ListBizChainDataRequest
        @return: ListBizChainDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_biz_chain_data_with_options_async(request, runtime)

    def list_device_with_options(
        self,
        request: lto_20210707_models.ListDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListDeviceResponse:
        """
        @param request: ListDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDevice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_with_options_async(
        self,
        request: lto_20210707_models.ListDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListDeviceResponse:
        """
        @param request: ListDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDevice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device(
        self,
        request: lto_20210707_models.ListDeviceRequest,
    ) -> lto_20210707_models.ListDeviceResponse:
        """
        @param request: ListDeviceRequest
        @return: ListDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_device_with_options(request, runtime)

    async def list_device_async(
        self,
        request: lto_20210707_models.ListDeviceRequest,
    ) -> lto_20210707_models.ListDeviceResponse:
        """
        @param request: ListDeviceRequest
        @return: ListDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_device_with_options_async(request, runtime)

    def list_device_group_with_options(
        self,
        request: lto_20210707_models.ListDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListDeviceGroupResponse:
        """
        @summary 查询设备组列表
        
        @param request: ListDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_name):
            query['MemberName'] = request.member_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceGroup',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_group_with_options_async(
        self,
        request: lto_20210707_models.ListDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListDeviceGroupResponse:
        """
        @summary 查询设备组列表
        
        @param request: ListDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_name):
            query['MemberName'] = request.member_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceGroup',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_group(
        self,
        request: lto_20210707_models.ListDeviceGroupRequest,
    ) -> lto_20210707_models.ListDeviceGroupResponse:
        """
        @summary 查询设备组列表
        
        @param request: ListDeviceGroupRequest
        @return: ListDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_device_group_with_options(request, runtime)

    async def list_device_group_async(
        self,
        request: lto_20210707_models.ListDeviceGroupRequest,
    ) -> lto_20210707_models.ListDeviceGroupResponse:
        """
        @summary 查询设备组列表
        
        @param request: ListDeviceGroupRequest
        @return: ListDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_device_group_with_options_async(request, runtime)

    def list_device_group_authorized_biz_chain_with_options(
        self,
        request: lto_20210707_models.ListDeviceGroupAuthorizedBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListDeviceGroupAuthorizedBizChainResponse:
        """
        @param request: ListDeviceGroupAuthorizedBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceGroupAuthorizedBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceGroupAuthorizedBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListDeviceGroupAuthorizedBizChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_group_authorized_biz_chain_with_options_async(
        self,
        request: lto_20210707_models.ListDeviceGroupAuthorizedBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListDeviceGroupAuthorizedBizChainResponse:
        """
        @param request: ListDeviceGroupAuthorizedBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeviceGroupAuthorizedBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceGroupAuthorizedBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListDeviceGroupAuthorizedBizChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_group_authorized_biz_chain(
        self,
        request: lto_20210707_models.ListDeviceGroupAuthorizedBizChainRequest,
    ) -> lto_20210707_models.ListDeviceGroupAuthorizedBizChainResponse:
        """
        @param request: ListDeviceGroupAuthorizedBizChainRequest
        @return: ListDeviceGroupAuthorizedBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_device_group_authorized_biz_chain_with_options(request, runtime)

    async def list_device_group_authorized_biz_chain_async(
        self,
        request: lto_20210707_models.ListDeviceGroupAuthorizedBizChainRequest,
    ) -> lto_20210707_models.ListDeviceGroupAuthorizedBizChainResponse:
        """
        @param request: ListDeviceGroupAuthorizedBizChainRequest
        @return: ListDeviceGroupAuthorizedBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_device_group_authorized_biz_chain_with_options_async(request, runtime)

    def list_edge_device_with_options(
        self,
        request: lto_20210707_models.ListEdgeDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListEdgeDeviceResponse:
        """
        @summary 查询边缘设备列表
        
        @param request: ListEdgeDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeDevice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListEdgeDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_edge_device_with_options_async(
        self,
        request: lto_20210707_models.ListEdgeDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListEdgeDeviceResponse:
        """
        @summary 查询边缘设备列表
        
        @param request: ListEdgeDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeDevice',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListEdgeDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_edge_device(
        self,
        request: lto_20210707_models.ListEdgeDeviceRequest,
    ) -> lto_20210707_models.ListEdgeDeviceResponse:
        """
        @summary 查询边缘设备列表
        
        @param request: ListEdgeDeviceRequest
        @return: ListEdgeDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_edge_device_with_options(request, runtime)

    async def list_edge_device_async(
        self,
        request: lto_20210707_models.ListEdgeDeviceRequest,
    ) -> lto_20210707_models.ListEdgeDeviceResponse:
        """
        @summary 查询边缘设备列表
        
        @param request: ListEdgeDeviceRequest
        @return: ListEdgeDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_edge_device_with_options_async(request, runtime)

    def list_edge_device_group_with_options(
        self,
        request: lto_20210707_models.ListEdgeDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListEdgeDeviceGroupResponse:
        """
        @summary 查询边缘设备组列表
        
        @param request: ListEdgeDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeDeviceGroup',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListEdgeDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_edge_device_group_with_options_async(
        self,
        request: lto_20210707_models.ListEdgeDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListEdgeDeviceGroupResponse:
        """
        @summary 查询边缘设备组列表
        
        @param request: ListEdgeDeviceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeDeviceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeDeviceGroup',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListEdgeDeviceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_edge_device_group(
        self,
        request: lto_20210707_models.ListEdgeDeviceGroupRequest,
    ) -> lto_20210707_models.ListEdgeDeviceGroupResponse:
        """
        @summary 查询边缘设备组列表
        
        @param request: ListEdgeDeviceGroupRequest
        @return: ListEdgeDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_edge_device_group_with_options(request, runtime)

    async def list_edge_device_group_async(
        self,
        request: lto_20210707_models.ListEdgeDeviceGroupRequest,
    ) -> lto_20210707_models.ListEdgeDeviceGroupResponse:
        """
        @summary 查询边缘设备组列表
        
        @param request: ListEdgeDeviceGroupRequest
        @return: ListEdgeDeviceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_edge_device_group_with_options_async(request, runtime)

    def list_member_with_options(
        self,
        request: lto_20210707_models.ListMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListMemberResponse:
        """
        @summary 查询成员列表
        
        @param request: ListMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contactor):
            query['Contactor'] = request.contactor
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_member_with_options_async(
        self,
        request: lto_20210707_models.ListMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListMemberResponse:
        """
        @summary 查询成员列表
        
        @param request: ListMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contactor):
            query['Contactor'] = request.contactor
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_member(
        self,
        request: lto_20210707_models.ListMemberRequest,
    ) -> lto_20210707_models.ListMemberResponse:
        """
        @summary 查询成员列表
        
        @param request: ListMemberRequest
        @return: ListMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_member_with_options(request, runtime)

    async def list_member_async(
        self,
        request: lto_20210707_models.ListMemberRequest,
    ) -> lto_20210707_models.ListMemberResponse:
        """
        @summary 查询成员列表
        
        @param request: ListMemberRequest
        @return: ListMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_member_with_options_async(request, runtime)

    def list_member_access_record_with_options(
        self,
        request: lto_20210707_models.ListMemberAccessRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListMemberAccessRecordResponse:
        """
        @summary 查询成员接入记录分页列表
        
        @param request: ListMemberAccessRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemberAccessRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_status):
            query['AccessStatus'] = request.access_status
        if not UtilClient.is_unset(request.contactor):
            query['Contactor'] = request.contactor
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemberAccessRecord',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListMemberAccessRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_member_access_record_with_options_async(
        self,
        request: lto_20210707_models.ListMemberAccessRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListMemberAccessRecordResponse:
        """
        @summary 查询成员接入记录分页列表
        
        @param request: ListMemberAccessRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemberAccessRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_status):
            query['AccessStatus'] = request.access_status
        if not UtilClient.is_unset(request.contactor):
            query['Contactor'] = request.contactor
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemberAccessRecord',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListMemberAccessRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_member_access_record(
        self,
        request: lto_20210707_models.ListMemberAccessRecordRequest,
    ) -> lto_20210707_models.ListMemberAccessRecordResponse:
        """
        @summary 查询成员接入记录分页列表
        
        @param request: ListMemberAccessRecordRequest
        @return: ListMemberAccessRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_member_access_record_with_options(request, runtime)

    async def list_member_access_record_async(
        self,
        request: lto_20210707_models.ListMemberAccessRecordRequest,
    ) -> lto_20210707_models.ListMemberAccessRecordResponse:
        """
        @summary 查询成员接入记录分页列表
        
        @param request: ListMemberAccessRecordRequest
        @return: ListMemberAccessRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_member_access_record_with_options_async(request, runtime)

    def list_member_authorized_biz_chain_with_options(
        self,
        request: lto_20210707_models.ListMemberAuthorizedBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListMemberAuthorizedBizChainResponse:
        """
        @param request: ListMemberAuthorizedBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemberAuthorizedBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemberAuthorizedBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListMemberAuthorizedBizChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_member_authorized_biz_chain_with_options_async(
        self,
        request: lto_20210707_models.ListMemberAuthorizedBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListMemberAuthorizedBizChainResponse:
        """
        @param request: ListMemberAuthorizedBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMemberAuthorizedBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMemberAuthorizedBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListMemberAuthorizedBizChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_member_authorized_biz_chain(
        self,
        request: lto_20210707_models.ListMemberAuthorizedBizChainRequest,
    ) -> lto_20210707_models.ListMemberAuthorizedBizChainResponse:
        """
        @param request: ListMemberAuthorizedBizChainRequest
        @return: ListMemberAuthorizedBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_member_authorized_biz_chain_with_options(request, runtime)

    async def list_member_authorized_biz_chain_async(
        self,
        request: lto_20210707_models.ListMemberAuthorizedBizChainRequest,
    ) -> lto_20210707_models.ListMemberAuthorizedBizChainResponse:
        """
        @param request: ListMemberAuthorizedBizChainRequest
        @return: ListMemberAuthorizedBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_member_authorized_biz_chain_with_options_async(request, runtime)

    def list_privacy_rule_with_options(
        self,
        request: lto_20210707_models.ListPrivacyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListPrivacyRuleResponse:
        """
        @param request: ListPrivacyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivacyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivacyRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListPrivacyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_privacy_rule_with_options_async(
        self,
        request: lto_20210707_models.ListPrivacyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListPrivacyRuleResponse:
        """
        @param request: ListPrivacyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivacyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivacyRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListPrivacyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_privacy_rule(
        self,
        request: lto_20210707_models.ListPrivacyRuleRequest,
    ) -> lto_20210707_models.ListPrivacyRuleResponse:
        """
        @param request: ListPrivacyRuleRequest
        @return: ListPrivacyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_privacy_rule_with_options(request, runtime)

    async def list_privacy_rule_async(
        self,
        request: lto_20210707_models.ListPrivacyRuleRequest,
    ) -> lto_20210707_models.ListPrivacyRuleResponse:
        """
        @param request: ListPrivacyRuleRequest
        @return: ListPrivacyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_privacy_rule_with_options_async(request, runtime)

    def list_privacy_rule_shared_member_with_options(
        self,
        request: lto_20210707_models.ListPrivacyRuleSharedMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListPrivacyRuleSharedMemberResponse:
        """
        @param request: ListPrivacyRuleSharedMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivacyRuleSharedMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.privacy_rule_id):
            query['PrivacyRuleId'] = request.privacy_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivacyRuleSharedMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListPrivacyRuleSharedMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_privacy_rule_shared_member_with_options_async(
        self,
        request: lto_20210707_models.ListPrivacyRuleSharedMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListPrivacyRuleSharedMemberResponse:
        """
        @param request: ListPrivacyRuleSharedMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivacyRuleSharedMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.privacy_rule_id):
            query['PrivacyRuleId'] = request.privacy_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivacyRuleSharedMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListPrivacyRuleSharedMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_privacy_rule_shared_member(
        self,
        request: lto_20210707_models.ListPrivacyRuleSharedMemberRequest,
    ) -> lto_20210707_models.ListPrivacyRuleSharedMemberResponse:
        """
        @param request: ListPrivacyRuleSharedMemberRequest
        @return: ListPrivacyRuleSharedMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_privacy_rule_shared_member_with_options(request, runtime)

    async def list_privacy_rule_shared_member_async(
        self,
        request: lto_20210707_models.ListPrivacyRuleSharedMemberRequest,
    ) -> lto_20210707_models.ListPrivacyRuleSharedMemberResponse:
        """
        @param request: ListPrivacyRuleSharedMemberRequest
        @return: ListPrivacyRuleSharedMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_privacy_rule_shared_member_with_options_async(request, runtime)

    def list_route_rule_with_options(
        self,
        request: lto_20210707_models.ListRouteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListRouteRuleResponse:
        """
        @param request: ListRouteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRouteRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_name):
            query['BizChainName'] = request.biz_chain_name
        if not UtilClient.is_unset(request.chain_up_mode):
            query['ChainUpMode'] = request.chain_up_mode
        if not UtilClient.is_unset(request.device_group_name):
            query['DeviceGroupName'] = request.device_group_name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRouteRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_route_rule_with_options_async(
        self,
        request: lto_20210707_models.ListRouteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.ListRouteRuleResponse:
        """
        @param request: ListRouteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRouteRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_name):
            query['BizChainName'] = request.biz_chain_name
        if not UtilClient.is_unset(request.chain_up_mode):
            query['ChainUpMode'] = request.chain_up_mode
        if not UtilClient.is_unset(request.device_group_name):
            query['DeviceGroupName'] = request.device_group_name
        if not UtilClient.is_unset(request.num):
            query['Num'] = request.num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRouteRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.ListRouteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_route_rule(
        self,
        request: lto_20210707_models.ListRouteRuleRequest,
    ) -> lto_20210707_models.ListRouteRuleResponse:
        """
        @param request: ListRouteRuleRequest
        @return: ListRouteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_route_rule_with_options(request, runtime)

    async def list_route_rule_async(
        self,
        request: lto_20210707_models.ListRouteRuleRequest,
    ) -> lto_20210707_models.ListRouteRuleResponse:
        """
        @param request: ListRouteRuleRequest
        @return: ListRouteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_route_rule_with_options_async(request, runtime)

    def query_blockchain_data_with_options(
        self,
        request: lto_20210707_models.QueryBlockchainDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.QueryBlockchainDataResponse:
        """
        @param request: QueryBlockchainDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryBlockchainDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.contract_name):
            query['ContractName'] = request.contract_name
        if not UtilClient.is_unset(request.invoke_type):
            query['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.iot_data_did):
            query['IotDataDID'] = request.iot_data_did
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBlockchainData',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.QueryBlockchainDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_blockchain_data_with_options_async(
        self,
        request: lto_20210707_models.QueryBlockchainDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.QueryBlockchainDataResponse:
        """
        @param request: QueryBlockchainDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryBlockchainDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.contract_name):
            query['ContractName'] = request.contract_name
        if not UtilClient.is_unset(request.invoke_type):
            query['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.iot_data_did):
            query['IotDataDID'] = request.iot_data_did
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBlockchainData',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.QueryBlockchainDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_blockchain_data(
        self,
        request: lto_20210707_models.QueryBlockchainDataRequest,
    ) -> lto_20210707_models.QueryBlockchainDataResponse:
        """
        @param request: QueryBlockchainDataRequest
        @return: QueryBlockchainDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_blockchain_data_with_options(request, runtime)

    async def query_blockchain_data_async(
        self,
        request: lto_20210707_models.QueryBlockchainDataRequest,
    ) -> lto_20210707_models.QueryBlockchainDataResponse:
        """
        @param request: QueryBlockchainDataRequest
        @return: QueryBlockchainDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_blockchain_data_with_options_async(request, runtime)

    def query_blockchain_metadata_with_options(
        self,
        request: lto_20210707_models.QueryBlockchainMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.QueryBlockchainMetadataResponse:
        """
        @param request: QueryBlockchainMetadataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryBlockchainMetadataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.contract_name):
            query['ContractName'] = request.contract_name
        if not UtilClient.is_unset(request.invoke_type):
            query['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.iot_data_did):
            query['IotDataDID'] = request.iot_data_did
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBlockchainMetadata',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.QueryBlockchainMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_blockchain_metadata_with_options_async(
        self,
        request: lto_20210707_models.QueryBlockchainMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.QueryBlockchainMetadataResponse:
        """
        @param request: QueryBlockchainMetadataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryBlockchainMetadataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.contract_name):
            query['ContractName'] = request.contract_name
        if not UtilClient.is_unset(request.invoke_type):
            query['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.iot_data_did):
            query['IotDataDID'] = request.iot_data_did
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBlockchainMetadata',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.QueryBlockchainMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_blockchain_metadata(
        self,
        request: lto_20210707_models.QueryBlockchainMetadataRequest,
    ) -> lto_20210707_models.QueryBlockchainMetadataResponse:
        """
        @param request: QueryBlockchainMetadataRequest
        @return: QueryBlockchainMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_blockchain_metadata_with_options(request, runtime)

    async def query_blockchain_metadata_async(
        self,
        request: lto_20210707_models.QueryBlockchainMetadataRequest,
    ) -> lto_20210707_models.QueryBlockchainMetadataResponse:
        """
        @param request: QueryBlockchainMetadataRequest
        @return: QueryBlockchainMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_blockchain_metadata_with_options_async(request, runtime)

    def share_privacy_rule_with_options(
        self,
        request: lto_20210707_models.SharePrivacyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.SharePrivacyRuleResponse:
        """
        @param request: SharePrivacyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SharePrivacyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_id_list):
            query['MemberIdList'] = request.member_id_list
        if not UtilClient.is_unset(request.privacy_rule_id):
            query['PrivacyRuleId'] = request.privacy_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SharePrivacyRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.SharePrivacyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def share_privacy_rule_with_options_async(
        self,
        request: lto_20210707_models.SharePrivacyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.SharePrivacyRuleResponse:
        """
        @param request: SharePrivacyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SharePrivacyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_id_list):
            query['MemberIdList'] = request.member_id_list
        if not UtilClient.is_unset(request.privacy_rule_id):
            query['PrivacyRuleId'] = request.privacy_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SharePrivacyRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.SharePrivacyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def share_privacy_rule(
        self,
        request: lto_20210707_models.SharePrivacyRuleRequest,
    ) -> lto_20210707_models.SharePrivacyRuleResponse:
        """
        @param request: SharePrivacyRuleRequest
        @return: SharePrivacyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.share_privacy_rule_with_options(request, runtime)

    async def share_privacy_rule_async(
        self,
        request: lto_20210707_models.SharePrivacyRuleRequest,
    ) -> lto_20210707_models.SharePrivacyRuleResponse:
        """
        @param request: SharePrivacyRuleRequest
        @return: SharePrivacyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.share_privacy_rule_with_options_async(request, runtime)

    def un_freeze_member_with_options(
        self,
        request: lto_20210707_models.UnFreezeMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.UnFreezeMemberResponse:
        """
        @param request: UnFreezeMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnFreezeMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnFreezeMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.UnFreezeMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_freeze_member_with_options_async(
        self,
        request: lto_20210707_models.UnFreezeMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.UnFreezeMemberResponse:
        """
        @param request: UnFreezeMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnFreezeMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnFreezeMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.UnFreezeMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_freeze_member(
        self,
        request: lto_20210707_models.UnFreezeMemberRequest,
    ) -> lto_20210707_models.UnFreezeMemberResponse:
        """
        @param request: UnFreezeMemberRequest
        @return: UnFreezeMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.un_freeze_member_with_options(request, runtime)

    async def un_freeze_member_async(
        self,
        request: lto_20210707_models.UnFreezeMemberRequest,
    ) -> lto_20210707_models.UnFreezeMemberResponse:
        """
        @param request: UnFreezeMemberRequest
        @return: UnFreezeMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_freeze_member_with_options_async(request, runtime)

    def update_biz_chain_with_options(
        self,
        request: lto_20210707_models.UpdateBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.UpdateBizChainResponse:
        """
        @param request: UpdateBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.UpdateBizChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_biz_chain_with_options_async(
        self,
        request: lto_20210707_models.UpdateBizChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.UpdateBizChainResponse:
        """
        @param request: UpdateBizChainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBizChainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBizChain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.UpdateBizChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_biz_chain(
        self,
        request: lto_20210707_models.UpdateBizChainRequest,
    ) -> lto_20210707_models.UpdateBizChainResponse:
        """
        @param request: UpdateBizChainRequest
        @return: UpdateBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_biz_chain_with_options(request, runtime)

    async def update_biz_chain_async(
        self,
        request: lto_20210707_models.UpdateBizChainRequest,
    ) -> lto_20210707_models.UpdateBizChainResponse:
        """
        @param request: UpdateBizChainRequest
        @return: UpdateBizChainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_biz_chain_with_options_async(request, runtime)

    def update_member_with_options(
        self,
        request: lto_20210707_models.UpdateMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.UpdateMemberResponse:
        """
        @summary 修改成员信息
        
        @param request: UpdateMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorized_count):
            query['AuthorizedCount'] = request.authorized_count
        if not UtilClient.is_unset(request.authorized_device_count):
            query['AuthorizedDeviceCount'] = request.authorized_device_count
        if not UtilClient.is_unset(request.contactor):
            query['Contactor'] = request.contactor
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.telephony):
            query['Telephony'] = request.telephony
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.UpdateMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_member_with_options_async(
        self,
        request: lto_20210707_models.UpdateMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.UpdateMemberResponse:
        """
        @summary 修改成员信息
        
        @param request: UpdateMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorized_count):
            query['AuthorizedCount'] = request.authorized_count
        if not UtilClient.is_unset(request.authorized_device_count):
            query['AuthorizedDeviceCount'] = request.authorized_device_count
        if not UtilClient.is_unset(request.contactor):
            query['Contactor'] = request.contactor
        if not UtilClient.is_unset(request.member_id):
            query['MemberId'] = request.member_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.telephony):
            query['Telephony'] = request.telephony
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMember',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.UpdateMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_member(
        self,
        request: lto_20210707_models.UpdateMemberRequest,
    ) -> lto_20210707_models.UpdateMemberResponse:
        """
        @summary 修改成员信息
        
        @param request: UpdateMemberRequest
        @return: UpdateMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_member_with_options(request, runtime)

    async def update_member_async(
        self,
        request: lto_20210707_models.UpdateMemberRequest,
    ) -> lto_20210707_models.UpdateMemberResponse:
        """
        @summary 修改成员信息
        
        @param request: UpdateMemberRequest
        @return: UpdateMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_member_with_options_async(request, runtime)

    def update_privacy_rule_with_options(
        self,
        request: lto_20210707_models.UpdatePrivacyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.UpdatePrivacyRuleResponse:
        """
        @param request: UpdatePrivacyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePrivacyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alg_impl):
            query['AlgImpl'] = request.alg_impl
        if not UtilClient.is_unset(request.alg_type):
            query['AlgType'] = request.alg_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.privacy_rule_id):
            query['PrivacyRuleId'] = request.privacy_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrivacyRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.UpdatePrivacyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_privacy_rule_with_options_async(
        self,
        request: lto_20210707_models.UpdatePrivacyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.UpdatePrivacyRuleResponse:
        """
        @param request: UpdatePrivacyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePrivacyRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alg_impl):
            query['AlgImpl'] = request.alg_impl
        if not UtilClient.is_unset(request.alg_type):
            query['AlgType'] = request.alg_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.privacy_rule_id):
            query['PrivacyRuleId'] = request.privacy_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrivacyRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.UpdatePrivacyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_privacy_rule(
        self,
        request: lto_20210707_models.UpdatePrivacyRuleRequest,
    ) -> lto_20210707_models.UpdatePrivacyRuleResponse:
        """
        @param request: UpdatePrivacyRuleRequest
        @return: UpdatePrivacyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_privacy_rule_with_options(request, runtime)

    async def update_privacy_rule_async(
        self,
        request: lto_20210707_models.UpdatePrivacyRuleRequest,
    ) -> lto_20210707_models.UpdatePrivacyRuleResponse:
        """
        @param request: UpdatePrivacyRuleRequest
        @return: UpdatePrivacyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_privacy_rule_with_options_async(request, runtime)

    def update_route_rule_with_options(
        self,
        request: lto_20210707_models.UpdateRouteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.UpdateRouteRuleResponse:
        """
        @param request: UpdateRouteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRouteRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.contract_name):
            query['ContractName'] = request.contract_name
        if not UtilClient.is_unset(request.contract_template_id):
            query['ContractTemplateId'] = request.contract_template_id
        if not UtilClient.is_unset(request.invoke_type):
            query['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.privacy_rule_id):
            query['PrivacyRuleId'] = request.privacy_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.route_rule_id):
            query['RouteRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRouteRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.UpdateRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_route_rule_with_options_async(
        self,
        request: lto_20210707_models.UpdateRouteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.UpdateRouteRuleResponse:
        """
        @param request: UpdateRouteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRouteRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_chain_id):
            query['BizChainId'] = request.biz_chain_id
        if not UtilClient.is_unset(request.contract_name):
            query['ContractName'] = request.contract_name
        if not UtilClient.is_unset(request.contract_template_id):
            query['ContractTemplateId'] = request.contract_template_id
        if not UtilClient.is_unset(request.invoke_type):
            query['InvokeType'] = request.invoke_type
        if not UtilClient.is_unset(request.privacy_rule_id):
            query['PrivacyRuleId'] = request.privacy_rule_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.route_rule_id):
            query['RouteRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRouteRule',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.UpdateRouteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_route_rule(
        self,
        request: lto_20210707_models.UpdateRouteRuleRequest,
    ) -> lto_20210707_models.UpdateRouteRuleResponse:
        """
        @param request: UpdateRouteRuleRequest
        @return: UpdateRouteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_route_rule_with_options(request, runtime)

    async def update_route_rule_async(
        self,
        request: lto_20210707_models.UpdateRouteRuleRequest,
    ) -> lto_20210707_models.UpdateRouteRuleResponse:
        """
        @param request: UpdateRouteRuleRequest
        @return: UpdateRouteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_route_rule_with_options_async(request, runtime)

    def upload_io_tdata_to_blockchain_with_options(
        self,
        request: lto_20210707_models.UploadIoTDataToBlockchainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.UploadIoTDataToBlockchainResponse:
        """
        @param request: UploadIoTDataToBlockchainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadIoTDataToBlockchainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_auth_type):
            query['IotAuthType'] = request.iot_auth_type
        if not UtilClient.is_unset(request.iot_data_did):
            query['IotDataDID'] = request.iot_data_did
        if not UtilClient.is_unset(request.iot_data_digest):
            query['IotDataDigest'] = request.iot_data_digest
        if not UtilClient.is_unset(request.iot_data_token):
            query['IotDataToken'] = request.iot_data_token
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_id_service_provider):
            query['IotIdServiceProvider'] = request.iot_id_service_provider
        if not UtilClient.is_unset(request.iot_id_source):
            query['IotIdSource'] = request.iot_id_source
        if not UtilClient.is_unset(request.plain_data):
            query['PlainData'] = request.plain_data
        if not UtilClient.is_unset(request.privacy_data):
            query['PrivacyData'] = request.privacy_data
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadIoTDataToBlockchain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.UploadIoTDataToBlockchainResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_io_tdata_to_blockchain_with_options_async(
        self,
        request: lto_20210707_models.UploadIoTDataToBlockchainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> lto_20210707_models.UploadIoTDataToBlockchainResponse:
        """
        @param request: UploadIoTDataToBlockchainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadIoTDataToBlockchainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_auth_type):
            query['IotAuthType'] = request.iot_auth_type
        if not UtilClient.is_unset(request.iot_data_did):
            query['IotDataDID'] = request.iot_data_did
        if not UtilClient.is_unset(request.iot_data_digest):
            query['IotDataDigest'] = request.iot_data_digest
        if not UtilClient.is_unset(request.iot_data_token):
            query['IotDataToken'] = request.iot_data_token
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_id_service_provider):
            query['IotIdServiceProvider'] = request.iot_id_service_provider
        if not UtilClient.is_unset(request.iot_id_source):
            query['IotIdSource'] = request.iot_id_source
        if not UtilClient.is_unset(request.plain_data):
            query['PlainData'] = request.plain_data
        if not UtilClient.is_unset(request.privacy_data):
            query['PrivacyData'] = request.privacy_data
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadIoTDataToBlockchain',
            version='2021-07-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            lto_20210707_models.UploadIoTDataToBlockchainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_io_tdata_to_blockchain(
        self,
        request: lto_20210707_models.UploadIoTDataToBlockchainRequest,
    ) -> lto_20210707_models.UploadIoTDataToBlockchainResponse:
        """
        @param request: UploadIoTDataToBlockchainRequest
        @return: UploadIoTDataToBlockchainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_io_tdata_to_blockchain_with_options(request, runtime)

    async def upload_io_tdata_to_blockchain_async(
        self,
        request: lto_20210707_models.UploadIoTDataToBlockchainRequest,
    ) -> lto_20210707_models.UploadIoTDataToBlockchainResponse:
        """
        @param request: UploadIoTDataToBlockchainRequest
        @return: UploadIoTDataToBlockchainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_io_tdata_to_blockchain_with_options_async(request, runtime)
