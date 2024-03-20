# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ebs20210730 import models as ebs_20210730_models
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
        self._endpoint = self.get_endpoint('ebs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.AddDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.AddDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   A replication pair and a replication pair-consistent group replicate in the same direction if they have the same primary region (production region), primary zone (production zone), secondary region (disaster recovery region), and secondary zone (disaster recovery zone). A replication pair can be added only to a replication pair-consistent group that replicates in the same direction as the replication pair.
        *   Before you can add a replication pair to a replication pair-consistent group, make sure that the pair and the group are in the **Created** (`created`) or **Stopped** (`stopped`) state.
        *   Up to 17 replication pairs can be added to a single replication pair-consistent group.
        *   After replication pairs are added to a replication pair-consistent group, the recovery point objective (RPO) of the group takes effect on the pairs in place of their original RPOs.
        
        @param request: AddDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.AddDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.AddDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.AddDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   A replication pair and a replication pair-consistent group replicate in the same direction if they have the same primary region (production region), primary zone (production zone), secondary region (disaster recovery region), and secondary zone (disaster recovery zone). A replication pair can be added only to a replication pair-consistent group that replicates in the same direction as the replication pair.
        *   Before you can add a replication pair to a replication pair-consistent group, make sure that the pair and the group are in the **Created** (`created`) or **Stopped** (`stopped`) state.
        *   Up to 17 replication pairs can be added to a single replication pair-consistent group.
        *   After replication pairs are added to a replication pair-consistent group, the recovery point objective (RPO) of the group takes effect on the pairs in place of their original RPOs.
        
        @param request: AddDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.AddDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_disk_replica_pair(
        self,
        request: ebs_20210730_models.AddDiskReplicaPairRequest,
    ) -> ebs_20210730_models.AddDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   A replication pair and a replication pair-consistent group replicate in the same direction if they have the same primary region (production region), primary zone (production zone), secondary region (disaster recovery region), and secondary zone (disaster recovery zone). A replication pair can be added only to a replication pair-consistent group that replicates in the same direction as the replication pair.
        *   Before you can add a replication pair to a replication pair-consistent group, make sure that the pair and the group are in the **Created** (`created`) or **Stopped** (`stopped`) state.
        *   Up to 17 replication pairs can be added to a single replication pair-consistent group.
        *   After replication pairs are added to a replication pair-consistent group, the recovery point objective (RPO) of the group takes effect on the pairs in place of their original RPOs.
        
        @param request: AddDiskReplicaPairRequest
        @return: AddDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_disk_replica_pair_with_options(request, runtime)

    async def add_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.AddDiskReplicaPairRequest,
    ) -> ebs_20210730_models.AddDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   A replication pair and a replication pair-consistent group replicate in the same direction if they have the same primary region (production region), primary zone (production zone), secondary region (disaster recovery region), and secondary zone (disaster recovery zone). A replication pair can be added only to a replication pair-consistent group that replicates in the same direction as the replication pair.
        *   Before you can add a replication pair to a replication pair-consistent group, make sure that the pair and the group are in the **Created** (`created`) or **Stopped** (`stopped`) state.
        *   Up to 17 replication pairs can be added to a single replication pair-consistent group.
        *   After replication pairs are added to a replication pair-consistent group, the recovery point objective (RPO) of the group takes effect on the pairs in place of their original RPOs.
        
        @param request: AddDiskReplicaPairRequest
        @return: AddDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_disk_replica_pair_with_options_async(request, runtime)

    def apply_lens_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ApplyLensServiceResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: ApplyLensServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyLensServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ApplyLensService',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ApplyLensServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_lens_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ApplyLensServiceResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: ApplyLensServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyLensServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ApplyLensService',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ApplyLensServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_lens_service(self) -> ebs_20210730_models.ApplyLensServiceResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @return: ApplyLensServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_lens_service_with_options(runtime)

    async def apply_lens_service_async(self) -> ebs_20210730_models.ApplyLensServiceResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @return: ApplyLensServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_lens_service_with_options_async(runtime)

    def bind_enterprise_snapshot_policy_with_options(
        self,
        request: ebs_20210730_models.BindEnterpriseSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.BindEnterpriseSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_targets):
            query['DiskTargets'] = request.disk_targets
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindEnterpriseSnapshotPolicy',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.BindEnterpriseSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_enterprise_snapshot_policy_with_options_async(
        self,
        request: ebs_20210730_models.BindEnterpriseSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.BindEnterpriseSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_targets):
            query['DiskTargets'] = request.disk_targets
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindEnterpriseSnapshotPolicy',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.BindEnterpriseSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_enterprise_snapshot_policy(
        self,
        request: ebs_20210730_models.BindEnterpriseSnapshotPolicyRequest,
    ) -> ebs_20210730_models.BindEnterpriseSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_enterprise_snapshot_policy_with_options(request, runtime)

    async def bind_enterprise_snapshot_policy_async(
        self,
        request: ebs_20210730_models.BindEnterpriseSnapshotPolicyRequest,
    ) -> ebs_20210730_models.BindEnterpriseSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_enterprise_snapshot_policy_with_options_async(request, runtime)

    def cancel_lens_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CancelLensServiceResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: CancelLensServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelLensServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CancelLensService',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CancelLensServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_lens_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CancelLensServiceResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: CancelLensServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelLensServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CancelLensService',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CancelLensServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_lens_service(self) -> ebs_20210730_models.CancelLensServiceResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @return: CancelLensServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_lens_service_with_options(runtime)

    async def cancel_lens_service_async(self) -> ebs_20210730_models.CancelLensServiceResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @return: CancelLensServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_lens_service_with_options_async(runtime)

    def change_resource_group_with_options(
        self,
        request: ebs_20210730_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: ebs_20210730_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: ebs_20210730_models.ChangeResourceGroupRequest,
    ) -> ebs_20210730_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: ebs_20210730_models.ChangeResourceGroupRequest,
    ) -> ebs_20210730_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def clear_pair_drill_with_options(
        self,
        request: ebs_20210730_models.ClearPairDrillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ClearPairDrillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drill_id):
            query['DrillId'] = request.drill_id
        if not UtilClient.is_unset(request.pair_id):
            query['PairId'] = request.pair_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearPairDrill',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ClearPairDrillResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_pair_drill_with_options_async(
        self,
        request: ebs_20210730_models.ClearPairDrillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ClearPairDrillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drill_id):
            query['DrillId'] = request.drill_id
        if not UtilClient.is_unset(request.pair_id):
            query['PairId'] = request.pair_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearPairDrill',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ClearPairDrillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_pair_drill(
        self,
        request: ebs_20210730_models.ClearPairDrillRequest,
    ) -> ebs_20210730_models.ClearPairDrillResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_pair_drill_with_options(request, runtime)

    async def clear_pair_drill_async(
        self,
        request: ebs_20210730_models.ClearPairDrillRequest,
    ) -> ebs_20210730_models.ClearPairDrillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_pair_drill_with_options_async(request, runtime)

    def clear_replica_group_drill_with_options(
        self,
        request: ebs_20210730_models.ClearReplicaGroupDrillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ClearReplicaGroupDrillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drill_id):
            query['DrillId'] = request.drill_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearReplicaGroupDrill',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ClearReplicaGroupDrillResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_replica_group_drill_with_options_async(
        self,
        request: ebs_20210730_models.ClearReplicaGroupDrillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ClearReplicaGroupDrillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drill_id):
            query['DrillId'] = request.drill_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearReplicaGroupDrill',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ClearReplicaGroupDrillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_replica_group_drill(
        self,
        request: ebs_20210730_models.ClearReplicaGroupDrillRequest,
    ) -> ebs_20210730_models.ClearReplicaGroupDrillResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_replica_group_drill_with_options(request, runtime)

    async def clear_replica_group_drill_async(
        self,
        request: ebs_20210730_models.ClearReplicaGroupDrillRequest,
    ) -> ebs_20210730_models.ClearReplicaGroupDrillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_replica_group_drill_with_options_async(request, runtime)

    def create_dedicated_block_storage_cluster_with_options(
        self,
        request: ebs_20210730_models.CreateDedicatedBlockStorageClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDedicatedBlockStorageClusterResponse:
        """
        Dedicated block storage clusters are physically isolated from public block storage clusters. The owner of each dedicated block storage cluster has exclusive access to all resources in the cluster.
        Disks created in a dedicated block storage cluster can be attached only to Elastic Compute Service (ECS) instances that reside in the same zone as the cluster. Before you create a dedicated block storage cluster, decide the regions and zones in which to deploy your cloud resources.
        Dedicated block storage clusters are classified into basic and performance types. When you create a dedicated block storage cluster, select a cluster type based on your business requirements.
        You are charged for creating dedicated block storage clusters.
        
        @param request: CreateDedicatedBlockStorageClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDedicatedBlockStorageClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.azone):
            query['Azone'] = request.azone
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.dbsc_name):
            query['DbscName'] = request.dbsc_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
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
            action='CreateDedicatedBlockStorageCluster',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDedicatedBlockStorageClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_block_storage_cluster_with_options_async(
        self,
        request: ebs_20210730_models.CreateDedicatedBlockStorageClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDedicatedBlockStorageClusterResponse:
        """
        Dedicated block storage clusters are physically isolated from public block storage clusters. The owner of each dedicated block storage cluster has exclusive access to all resources in the cluster.
        Disks created in a dedicated block storage cluster can be attached only to Elastic Compute Service (ECS) instances that reside in the same zone as the cluster. Before you create a dedicated block storage cluster, decide the regions and zones in which to deploy your cloud resources.
        Dedicated block storage clusters are classified into basic and performance types. When you create a dedicated block storage cluster, select a cluster type based on your business requirements.
        You are charged for creating dedicated block storage clusters.
        
        @param request: CreateDedicatedBlockStorageClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDedicatedBlockStorageClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.azone):
            query['Azone'] = request.azone
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.dbsc_name):
            query['DbscName'] = request.dbsc_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
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
            action='CreateDedicatedBlockStorageCluster',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDedicatedBlockStorageClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_block_storage_cluster(
        self,
        request: ebs_20210730_models.CreateDedicatedBlockStorageClusterRequest,
    ) -> ebs_20210730_models.CreateDedicatedBlockStorageClusterResponse:
        """
        Dedicated block storage clusters are physically isolated from public block storage clusters. The owner of each dedicated block storage cluster has exclusive access to all resources in the cluster.
        Disks created in a dedicated block storage cluster can be attached only to Elastic Compute Service (ECS) instances that reside in the same zone as the cluster. Before you create a dedicated block storage cluster, decide the regions and zones in which to deploy your cloud resources.
        Dedicated block storage clusters are classified into basic and performance types. When you create a dedicated block storage cluster, select a cluster type based on your business requirements.
        You are charged for creating dedicated block storage clusters.
        
        @param request: CreateDedicatedBlockStorageClusterRequest
        @return: CreateDedicatedBlockStorageClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_block_storage_cluster_with_options(request, runtime)

    async def create_dedicated_block_storage_cluster_async(
        self,
        request: ebs_20210730_models.CreateDedicatedBlockStorageClusterRequest,
    ) -> ebs_20210730_models.CreateDedicatedBlockStorageClusterResponse:
        """
        Dedicated block storage clusters are physically isolated from public block storage clusters. The owner of each dedicated block storage cluster has exclusive access to all resources in the cluster.
        Disks created in a dedicated block storage cluster can be attached only to Elastic Compute Service (ECS) instances that reside in the same zone as the cluster. Before you create a dedicated block storage cluster, decide the regions and zones in which to deploy your cloud resources.
        Dedicated block storage clusters are classified into basic and performance types. When you create a dedicated block storage cluster, select a cluster type based on your business requirements.
        You are charged for creating dedicated block storage clusters.
        
        @param request: CreateDedicatedBlockStorageClusterRequest
        @return: CreateDedicatedBlockStorageClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_block_storage_cluster_with_options_async(request, runtime)

    def create_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.CreateDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        The replication pair-consistent group feature allows you to batch manage multiple disks in disaster recovery scenarios. You can restore the data of all disks in the same replication pair-consistent group to the same point in time to allow for disaster recovery of instances.
        Take note of the following items:
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   Replication pair-consistent groups can be used to implement disaster recovery across zones within the same region and disaster recovery across regions.
        *   A replication pair and a replication pair-consistent group can replicate in the same direction if they have the same primary region (production region), primary zone (production zone), secondary region (disaster recovery region), and secondary zone (disaster recovery zone). A replication pair can be added to only a replication pair-consistent group that replicates in the same direction as the replication pair.
        *   After replication pairs are added to a replication pair-consistent group, the recovery point objective (RPO) of the group takes effect on the pairs instead of their original RPOs.
        
        @param request: CreateDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.CreateDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        The replication pair-consistent group feature allows you to batch manage multiple disks in disaster recovery scenarios. You can restore the data of all disks in the same replication pair-consistent group to the same point in time to allow for disaster recovery of instances.
        Take note of the following items:
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   Replication pair-consistent groups can be used to implement disaster recovery across zones within the same region and disaster recovery across regions.
        *   A replication pair and a replication pair-consistent group can replicate in the same direction if they have the same primary region (production region), primary zone (production zone), secondary region (disaster recovery region), and secondary zone (disaster recovery zone). A replication pair can be added to only a replication pair-consistent group that replicates in the same direction as the replication pair.
        *   After replication pairs are added to a replication pair-consistent group, the recovery point objective (RPO) of the group takes effect on the pairs instead of their original RPOs.
        
        @param request: CreateDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_disk_replica_group(
        self,
        request: ebs_20210730_models.CreateDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.CreateDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        The replication pair-consistent group feature allows you to batch manage multiple disks in disaster recovery scenarios. You can restore the data of all disks in the same replication pair-consistent group to the same point in time to allow for disaster recovery of instances.
        Take note of the following items:
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   Replication pair-consistent groups can be used to implement disaster recovery across zones within the same region and disaster recovery across regions.
        *   A replication pair and a replication pair-consistent group can replicate in the same direction if they have the same primary region (production region), primary zone (production zone), secondary region (disaster recovery region), and secondary zone (disaster recovery zone). A replication pair can be added to only a replication pair-consistent group that replicates in the same direction as the replication pair.
        *   After replication pairs are added to a replication pair-consistent group, the recovery point objective (RPO) of the group takes effect on the pairs instead of their original RPOs.
        
        @param request: CreateDiskReplicaGroupRequest
        @return: CreateDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_disk_replica_group_with_options(request, runtime)

    async def create_disk_replica_group_async(
        self,
        request: ebs_20210730_models.CreateDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.CreateDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        The replication pair-consistent group feature allows you to batch manage multiple disks in disaster recovery scenarios. You can restore the data of all disks in the same replication pair-consistent group to the same point in time to allow for disaster recovery of instances.
        Take note of the following items:
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   Replication pair-consistent groups can be used to implement disaster recovery across zones within the same region and disaster recovery across regions.
        *   A replication pair and a replication pair-consistent group can replicate in the same direction if they have the same primary region (production region), primary zone (production zone), secondary region (disaster recovery region), and secondary zone (disaster recovery zone). A replication pair can be added to only a replication pair-consistent group that replicates in the same direction as the replication pair.
        *   After replication pairs are added to a replication pair-consistent group, the recovery point objective (RPO) of the group takes effect on the pairs instead of their original RPOs.
        
        @param request: CreateDiskReplicaGroupRequest
        @return: CreateDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_disk_replica_group_with_options_async(request, runtime)

    def create_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.CreateDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDiskReplicaPairResponse:
        """
        Async replication is a feature that protects data across regions by using the data replication capability of Elastic Block Storage (EBS). This feature can be used to asynchronously replicate data from a disk in one region to a disk in another region for disaster recovery purposes. You can use this feature to implement disaster recovery for critical business to protect data in your databases and improve business continuity.
        Currently, the async replication feature can asynchronously replicate data only between enhanced SSDs (ESSDs). The functionality of disks in replication pairs is limited. You are charged on a subscription basis for the bandwidth that is used by the async replication feature.
        Before you call this operation, take note of the following items:
        *   Make sure that the source disk (primary disk) from which to replicate data and the destination disk (secondary disk) to which to replicate data are created. You can call the [CreateDisk](~~25513~~) operation to create disks.
        *   The secondary disk cannot reside the same region as the primary disk. The async replication feature is supported in the China (Hangzhou), China (Shanghai), China (Beijing), China (Shenzhen), China (Heyuan), China (Chengdu), China (Hong Kong), Singapore, US (Silicon Valley), and US (Virginia) regions.
        *   After you call this operation to create a replication pair, you must call the [StartDiskReplicaPair](~~354205~~) operation to enable async replication to periodically replicate data from the primary disk to the secondary disk across regions.
        
        @param request: CreateDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_disk_id):
            query['DestinationDiskId'] = request.destination_disk_id
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.pair_name):
            query['PairName'] = request.pair_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.CreateDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateDiskReplicaPairResponse:
        """
        Async replication is a feature that protects data across regions by using the data replication capability of Elastic Block Storage (EBS). This feature can be used to asynchronously replicate data from a disk in one region to a disk in another region for disaster recovery purposes. You can use this feature to implement disaster recovery for critical business to protect data in your databases and improve business continuity.
        Currently, the async replication feature can asynchronously replicate data only between enhanced SSDs (ESSDs). The functionality of disks in replication pairs is limited. You are charged on a subscription basis for the bandwidth that is used by the async replication feature.
        Before you call this operation, take note of the following items:
        *   Make sure that the source disk (primary disk) from which to replicate data and the destination disk (secondary disk) to which to replicate data are created. You can call the [CreateDisk](~~25513~~) operation to create disks.
        *   The secondary disk cannot reside the same region as the primary disk. The async replication feature is supported in the China (Hangzhou), China (Shanghai), China (Beijing), China (Shenzhen), China (Heyuan), China (Chengdu), China (Hong Kong), Singapore, US (Silicon Valley), and US (Virginia) regions.
        *   After you call this operation to create a replication pair, you must call the [StartDiskReplicaPair](~~354205~~) operation to enable async replication to periodically replicate data from the primary disk to the secondary disk across regions.
        
        @param request: CreateDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_disk_id):
            query['DestinationDiskId'] = request.destination_disk_id
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.destination_zone_id):
            query['DestinationZoneId'] = request.destination_zone_id
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.pair_name):
            query['PairName'] = request.pair_name
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_zone_id):
            query['SourceZoneId'] = request.source_zone_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_disk_replica_pair(
        self,
        request: ebs_20210730_models.CreateDiskReplicaPairRequest,
    ) -> ebs_20210730_models.CreateDiskReplicaPairResponse:
        """
        Async replication is a feature that protects data across regions by using the data replication capability of Elastic Block Storage (EBS). This feature can be used to asynchronously replicate data from a disk in one region to a disk in another region for disaster recovery purposes. You can use this feature to implement disaster recovery for critical business to protect data in your databases and improve business continuity.
        Currently, the async replication feature can asynchronously replicate data only between enhanced SSDs (ESSDs). The functionality of disks in replication pairs is limited. You are charged on a subscription basis for the bandwidth that is used by the async replication feature.
        Before you call this operation, take note of the following items:
        *   Make sure that the source disk (primary disk) from which to replicate data and the destination disk (secondary disk) to which to replicate data are created. You can call the [CreateDisk](~~25513~~) operation to create disks.
        *   The secondary disk cannot reside the same region as the primary disk. The async replication feature is supported in the China (Hangzhou), China (Shanghai), China (Beijing), China (Shenzhen), China (Heyuan), China (Chengdu), China (Hong Kong), Singapore, US (Silicon Valley), and US (Virginia) regions.
        *   After you call this operation to create a replication pair, you must call the [StartDiskReplicaPair](~~354205~~) operation to enable async replication to periodically replicate data from the primary disk to the secondary disk across regions.
        
        @param request: CreateDiskReplicaPairRequest
        @return: CreateDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_disk_replica_pair_with_options(request, runtime)

    async def create_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.CreateDiskReplicaPairRequest,
    ) -> ebs_20210730_models.CreateDiskReplicaPairResponse:
        """
        Async replication is a feature that protects data across regions by using the data replication capability of Elastic Block Storage (EBS). This feature can be used to asynchronously replicate data from a disk in one region to a disk in another region for disaster recovery purposes. You can use this feature to implement disaster recovery for critical business to protect data in your databases and improve business continuity.
        Currently, the async replication feature can asynchronously replicate data only between enhanced SSDs (ESSDs). The functionality of disks in replication pairs is limited. You are charged on a subscription basis for the bandwidth that is used by the async replication feature.
        Before you call this operation, take note of the following items:
        *   Make sure that the source disk (primary disk) from which to replicate data and the destination disk (secondary disk) to which to replicate data are created. You can call the [CreateDisk](~~25513~~) operation to create disks.
        *   The secondary disk cannot reside the same region as the primary disk. The async replication feature is supported in the China (Hangzhou), China (Shanghai), China (Beijing), China (Shenzhen), China (Heyuan), China (Chengdu), China (Hong Kong), Singapore, US (Silicon Valley), and US (Virginia) regions.
        *   After you call this operation to create a replication pair, you must call the [StartDiskReplicaPair](~~354205~~) operation to enable async replication to periodically replicate data from the primary disk to the secondary disk across regions.
        
        @param request: CreateDiskReplicaPairRequest
        @return: CreateDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_disk_replica_pair_with_options_async(request, runtime)

    def create_enterprise_snapshot_policy_with_options(
        self,
        tmp_req: ebs_20210730_models.CreateEnterpriseSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateEnterpriseSnapshotPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = ebs_20210730_models.CreateEnterpriseSnapshotPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cross_region_copy_info):
            request.cross_region_copy_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cross_region_copy_info, 'CrossRegionCopyInfo', 'json')
        if not UtilClient.is_unset(tmp_req.retain_rule):
            request.retain_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retain_rule, 'RetainRule', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        if not UtilClient.is_unset(tmp_req.special_retain_rules):
            request.special_retain_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.special_retain_rules, 'SpecialRetainRules', 'json')
        if not UtilClient.is_unset(tmp_req.storage_rule):
            request.storage_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.storage_rule, 'StorageRule', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_region_copy_info_shrink):
            query['CrossRegionCopyInfo'] = request.cross_region_copy_info_shrink
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.retain_rule_shrink):
            query['RetainRule'] = request.retain_rule_shrink
        if not UtilClient.is_unset(request.schedule_shrink):
            query['Schedule'] = request.schedule_shrink
        if not UtilClient.is_unset(request.special_retain_rules_shrink):
            query['SpecialRetainRules'] = request.special_retain_rules_shrink
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.storage_rule_shrink):
            query['StorageRule'] = request.storage_rule_shrink
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEnterpriseSnapshotPolicy',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateEnterpriseSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_enterprise_snapshot_policy_with_options_async(
        self,
        tmp_req: ebs_20210730_models.CreateEnterpriseSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.CreateEnterpriseSnapshotPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = ebs_20210730_models.CreateEnterpriseSnapshotPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cross_region_copy_info):
            request.cross_region_copy_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cross_region_copy_info, 'CrossRegionCopyInfo', 'json')
        if not UtilClient.is_unset(tmp_req.retain_rule):
            request.retain_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retain_rule, 'RetainRule', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        if not UtilClient.is_unset(tmp_req.special_retain_rules):
            request.special_retain_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.special_retain_rules, 'SpecialRetainRules', 'json')
        if not UtilClient.is_unset(tmp_req.storage_rule):
            request.storage_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.storage_rule, 'StorageRule', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_region_copy_info_shrink):
            query['CrossRegionCopyInfo'] = request.cross_region_copy_info_shrink
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.retain_rule_shrink):
            query['RetainRule'] = request.retain_rule_shrink
        if not UtilClient.is_unset(request.schedule_shrink):
            query['Schedule'] = request.schedule_shrink
        if not UtilClient.is_unset(request.special_retain_rules_shrink):
            query['SpecialRetainRules'] = request.special_retain_rules_shrink
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.storage_rule_shrink):
            query['StorageRule'] = request.storage_rule_shrink
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEnterpriseSnapshotPolicy',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.CreateEnterpriseSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_enterprise_snapshot_policy(
        self,
        request: ebs_20210730_models.CreateEnterpriseSnapshotPolicyRequest,
    ) -> ebs_20210730_models.CreateEnterpriseSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_enterprise_snapshot_policy_with_options(request, runtime)

    async def create_enterprise_snapshot_policy_async(
        self,
        request: ebs_20210730_models.CreateEnterpriseSnapshotPolicyRequest,
    ) -> ebs_20210730_models.CreateEnterpriseSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_enterprise_snapshot_policy_with_options_async(request, runtime)

    def delete_disk_with_options(
        self,
        request: ebs_20210730_models.DeleteDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteDiskResponse:
        """
        Currently, this API is only available for use with ACS resource hosting and is not yet open for direct invocation.
        
        @param request: DeleteDiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDisk',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_disk_with_options_async(
        self,
        request: ebs_20210730_models.DeleteDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteDiskResponse:
        """
        Currently, this API is only available for use with ACS resource hosting and is not yet open for direct invocation.
        
        @param request: DeleteDiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDisk',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_disk(
        self,
        request: ebs_20210730_models.DeleteDiskRequest,
    ) -> ebs_20210730_models.DeleteDiskResponse:
        """
        Currently, this API is only available for use with ACS resource hosting and is not yet open for direct invocation.
        
        @param request: DeleteDiskRequest
        @return: DeleteDiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_disk_with_options(request, runtime)

    async def delete_disk_async(
        self,
        request: ebs_20210730_models.DeleteDiskRequest,
    ) -> ebs_20210730_models.DeleteDiskResponse:
        """
        Currently, this API is only available for use with ACS resource hosting and is not yet open for direct invocation.
        
        @param request: DeleteDiskRequest
        @return: DeleteDiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_disk_with_options_async(request, runtime)

    def delete_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   Before you can delete a replication pair-consistent group, make sure that no replication pairs exist in the group.
        *   The replication pair-consistent group that you want to delete must be in the **Created** (`created`), **Creation Failed** (`create_failed`), **Stopped** (`stopped`), **Failovered** (`failovered`), **Deleting** (`deleting`), **Deletion Failed** (`delete_failed`), or **Invalid** (`invalid`) state.
        
        @param request: DeleteDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   Before you can delete a replication pair-consistent group, make sure that no replication pairs exist in the group.
        *   The replication pair-consistent group that you want to delete must be in the **Created** (`created`), **Creation Failed** (`create_failed`), **Stopped** (`stopped`), **Failovered** (`failovered`), **Deleting** (`deleting`), **Deletion Failed** (`delete_failed`), or **Invalid** (`invalid`) state.
        
        @param request: DeleteDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_disk_replica_group(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.DeleteDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   Before you can delete a replication pair-consistent group, make sure that no replication pairs exist in the group.
        *   The replication pair-consistent group that you want to delete must be in the **Created** (`created`), **Creation Failed** (`create_failed`), **Stopped** (`stopped`), **Failovered** (`failovered`), **Deleting** (`deleting`), **Deletion Failed** (`delete_failed`), or **Invalid** (`invalid`) state.
        
        @param request: DeleteDiskReplicaGroupRequest
        @return: DeleteDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_disk_replica_group_with_options(request, runtime)

    async def delete_disk_replica_group_async(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.DeleteDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   Before you can delete a replication pair-consistent group, make sure that no replication pairs exist in the group.
        *   The replication pair-consistent group that you want to delete must be in the **Created** (`created`), **Creation Failed** (`create_failed`), **Stopped** (`stopped`), **Failovered** (`failovered`), **Deleting** (`deleting`), **Deletion Failed** (`delete_failed`), or **Invalid** (`invalid`) state.
        
        @param request: DeleteDiskReplicaGroupRequest
        @return: DeleteDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_disk_replica_group_with_options_async(request, runtime)

    def delete_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Stopped** (`stopped`), **Invalid** (`invalid`), or **Failovered** (`failovered`) state can be deleted. This operation deletes only replication pairs. The primary and secondary disks in the deleted replication pairs are retained.
        *   To delete a replication pair, you must call this operation in the region where the primary disk is located. After the replication pair is deleted, the functionality limits are lifted from the primary and secondary disks. For example, you can attach the secondary disk, resize the disk, or read data from or write data to the disk.
        
        @param request: DeleteDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Stopped** (`stopped`), **Invalid** (`invalid`), or **Failovered** (`failovered`) state can be deleted. This operation deletes only replication pairs. The primary and secondary disks in the deleted replication pairs are retained.
        *   To delete a replication pair, you must call this operation in the region where the primary disk is located. After the replication pair is deleted, the functionality limits are lifted from the primary and secondary disks. For example, you can attach the secondary disk, resize the disk, or read data from or write data to the disk.
        
        @param request: DeleteDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_disk_replica_pair(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaPairRequest,
    ) -> ebs_20210730_models.DeleteDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Stopped** (`stopped`), **Invalid** (`invalid`), or **Failovered** (`failovered`) state can be deleted. This operation deletes only replication pairs. The primary and secondary disks in the deleted replication pairs are retained.
        *   To delete a replication pair, you must call this operation in the region where the primary disk is located. After the replication pair is deleted, the functionality limits are lifted from the primary and secondary disks. For example, you can attach the secondary disk, resize the disk, or read data from or write data to the disk.
        
        @param request: DeleteDiskReplicaPairRequest
        @return: DeleteDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_disk_replica_pair_with_options(request, runtime)

    async def delete_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.DeleteDiskReplicaPairRequest,
    ) -> ebs_20210730_models.DeleteDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Stopped** (`stopped`), **Invalid** (`invalid`), or **Failovered** (`failovered`) state can be deleted. This operation deletes only replication pairs. The primary and secondary disks in the deleted replication pairs are retained.
        *   To delete a replication pair, you must call this operation in the region where the primary disk is located. After the replication pair is deleted, the functionality limits are lifted from the primary and secondary disks. For example, you can attach the secondary disk, resize the disk, or read data from or write data to the disk.
        
        @param request: DeleteDiskReplicaPairRequest
        @return: DeleteDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_disk_replica_pair_with_options_async(request, runtime)

    def delete_enterprise_snapshot_policy_with_options(
        self,
        request: ebs_20210730_models.DeleteEnterpriseSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteEnterpriseSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnterpriseSnapshotPolicy',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteEnterpriseSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_enterprise_snapshot_policy_with_options_async(
        self,
        request: ebs_20210730_models.DeleteEnterpriseSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DeleteEnterpriseSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnterpriseSnapshotPolicy',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DeleteEnterpriseSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_enterprise_snapshot_policy(
        self,
        request: ebs_20210730_models.DeleteEnterpriseSnapshotPolicyRequest,
    ) -> ebs_20210730_models.DeleteEnterpriseSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_enterprise_snapshot_policy_with_options(request, runtime)

    async def delete_enterprise_snapshot_policy_async(
        self,
        request: ebs_20210730_models.DeleteEnterpriseSnapshotPolicyRequest,
    ) -> ebs_20210730_models.DeleteEnterpriseSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_enterprise_snapshot_policy_with_options_async(request, runtime)

    def describe_dedicated_block_storage_cluster_disks_with_options(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksResponse:
        """
        You can use one of the following methods to check the responses:
        *   Method 1: Use `NextToken` to configure the query token. Set the value to the `NextToken` value that is returned in the last call to the DescribeDisks operation. Then, use `MaxResults` to specify the maximum number of entries to return on each page.
        *   Method 2: Use `PageSize` to specify the number of entries to return on each page and then use `PageNumber` to specify the number of the page to return.
        You can use only one of the preceding methods. If a large number of entries are to be returned, we recommend that you use method 1. When `NextToken` is specified, `PageSize` and `PageNumber` do not take effect and `TotalCount` in the response is invalid.
        *   A disk that has the multi-attach feature enabled can be attached to multiple instances. You can query the attachment information of the disk based on the `Attachment` values in the response.
        When you call an API operation by using Alibaba Cloud CLI, you must specify request parameter values of different data types in the required formats. For more information, see [Parameter format overview](~~110340~~).
        
        @param request: DescribeDedicatedBlockStorageClusterDisksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedBlockStorageClusterDisksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedBlockStorageClusterDisks',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_block_storage_cluster_disks_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksResponse:
        """
        You can use one of the following methods to check the responses:
        *   Method 1: Use `NextToken` to configure the query token. Set the value to the `NextToken` value that is returned in the last call to the DescribeDisks operation. Then, use `MaxResults` to specify the maximum number of entries to return on each page.
        *   Method 2: Use `PageSize` to specify the number of entries to return on each page and then use `PageNumber` to specify the number of the page to return.
        You can use only one of the preceding methods. If a large number of entries are to be returned, we recommend that you use method 1. When `NextToken` is specified, `PageSize` and `PageNumber` do not take effect and `TotalCount` in the response is invalid.
        *   A disk that has the multi-attach feature enabled can be attached to multiple instances. You can query the attachment information of the disk based on the `Attachment` values in the response.
        When you call an API operation by using Alibaba Cloud CLI, you must specify request parameter values of different data types in the required formats. For more information, see [Parameter format overview](~~110340~~).
        
        @param request: DescribeDedicatedBlockStorageClusterDisksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedBlockStorageClusterDisksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedBlockStorageClusterDisks',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_block_storage_cluster_disks(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksRequest,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksResponse:
        """
        You can use one of the following methods to check the responses:
        *   Method 1: Use `NextToken` to configure the query token. Set the value to the `NextToken` value that is returned in the last call to the DescribeDisks operation. Then, use `MaxResults` to specify the maximum number of entries to return on each page.
        *   Method 2: Use `PageSize` to specify the number of entries to return on each page and then use `PageNumber` to specify the number of the page to return.
        You can use only one of the preceding methods. If a large number of entries are to be returned, we recommend that you use method 1. When `NextToken` is specified, `PageSize` and `PageNumber` do not take effect and `TotalCount` in the response is invalid.
        *   A disk that has the multi-attach feature enabled can be attached to multiple instances. You can query the attachment information of the disk based on the `Attachment` values in the response.
        When you call an API operation by using Alibaba Cloud CLI, you must specify request parameter values of different data types in the required formats. For more information, see [Parameter format overview](~~110340~~).
        
        @param request: DescribeDedicatedBlockStorageClusterDisksRequest
        @return: DescribeDedicatedBlockStorageClusterDisksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_block_storage_cluster_disks_with_options(request, runtime)

    async def describe_dedicated_block_storage_cluster_disks_async(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksRequest,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClusterDisksResponse:
        """
        You can use one of the following methods to check the responses:
        *   Method 1: Use `NextToken` to configure the query token. Set the value to the `NextToken` value that is returned in the last call to the DescribeDisks operation. Then, use `MaxResults` to specify the maximum number of entries to return on each page.
        *   Method 2: Use `PageSize` to specify the number of entries to return on each page and then use `PageNumber` to specify the number of the page to return.
        You can use only one of the preceding methods. If a large number of entries are to be returned, we recommend that you use method 1. When `NextToken` is specified, `PageSize` and `PageNumber` do not take effect and `TotalCount` in the response is invalid.
        *   A disk that has the multi-attach feature enabled can be attached to multiple instances. You can query the attachment information of the disk based on the `Attachment` values in the response.
        When you call an API operation by using Alibaba Cloud CLI, you must specify request parameter values of different data types in the required formats. For more information, see [Parameter format overview](~~110340~~).
        
        @param request: DescribeDedicatedBlockStorageClusterDisksRequest
        @return: DescribeDedicatedBlockStorageClusterDisksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_block_storage_cluster_disks_with_options_async(request, runtime)

    def describe_dedicated_block_storage_clusters_with_options(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClustersResponse:
        """
        ## [](#)Usage notes
        >  The Dedicated Block Storage Cluster feature is available only in the China (Heyuan), Indonesia (Jakarta), and China (Shenzhen) regions.
        *   You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are included in the filter conditions.
        *   We recommend that you use NextToken and MaxResults to perform paged queries. We recommend that you use MaxResults to specify the maximum number of entries to return in each request. The return value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. When you call the DescribeDedicatedBlockStorageClusters operation to retrieve a new page of results, set NextToken to the NextToken value that is returned in the previous call and specify MaxResults to limit the number of entries returned.
        
        @param request: DescribeDedicatedBlockStorageClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedBlockStorageClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_block_storage_cluster_id):
            query['DedicatedBlockStorageClusterId'] = request.dedicated_block_storage_cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.azone_id):
            body['AzoneId'] = request.azone_id
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedBlockStorageClusters',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDedicatedBlockStorageClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dedicated_block_storage_clusters_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClustersResponse:
        """
        ## [](#)Usage notes
        >  The Dedicated Block Storage Cluster feature is available only in the China (Heyuan), Indonesia (Jakarta), and China (Shenzhen) regions.
        *   You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are included in the filter conditions.
        *   We recommend that you use NextToken and MaxResults to perform paged queries. We recommend that you use MaxResults to specify the maximum number of entries to return in each request. The return value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. When you call the DescribeDedicatedBlockStorageClusters operation to retrieve a new page of results, set NextToken to the NextToken value that is returned in the previous call and specify MaxResults to limit the number of entries returned.
        
        @param request: DescribeDedicatedBlockStorageClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDedicatedBlockStorageClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dedicated_block_storage_cluster_id):
            query['DedicatedBlockStorageClusterId'] = request.dedicated_block_storage_cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.azone_id):
            body['AzoneId'] = request.azone_id
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDedicatedBlockStorageClusters',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDedicatedBlockStorageClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dedicated_block_storage_clusters(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClustersRequest,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClustersResponse:
        """
        ## [](#)Usage notes
        >  The Dedicated Block Storage Cluster feature is available only in the China (Heyuan), Indonesia (Jakarta), and China (Shenzhen) regions.
        *   You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are included in the filter conditions.
        *   We recommend that you use NextToken and MaxResults to perform paged queries. We recommend that you use MaxResults to specify the maximum number of entries to return in each request. The return value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. When you call the DescribeDedicatedBlockStorageClusters operation to retrieve a new page of results, set NextToken to the NextToken value that is returned in the previous call and specify MaxResults to limit the number of entries returned.
        
        @param request: DescribeDedicatedBlockStorageClustersRequest
        @return: DescribeDedicatedBlockStorageClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_block_storage_clusters_with_options(request, runtime)

    async def describe_dedicated_block_storage_clusters_async(
        self,
        request: ebs_20210730_models.DescribeDedicatedBlockStorageClustersRequest,
    ) -> ebs_20210730_models.DescribeDedicatedBlockStorageClustersResponse:
        """
        ## [](#)Usage notes
        >  The Dedicated Block Storage Cluster feature is available only in the China (Heyuan), Indonesia (Jakarta), and China (Shenzhen) regions.
        *   You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are included in the filter conditions.
        *   We recommend that you use NextToken and MaxResults to perform paged queries. We recommend that you use MaxResults to specify the maximum number of entries to return in each request. The return value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. When you call the DescribeDedicatedBlockStorageClusters operation to retrieve a new page of results, set NextToken to the NextToken value that is returned in the previous call and specify MaxResults to limit the number of entries returned.
        
        @param request: DescribeDedicatedBlockStorageClustersRequest
        @return: DescribeDedicatedBlockStorageClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_block_storage_clusters_with_options_async(request, runtime)

    def describe_disk_events_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskEventsResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: DescribeDiskEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiskEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskEvents',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_events_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDiskEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskEventsResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: DescribeDiskEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiskEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskEvents',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_events(
        self,
        request: ebs_20210730_models.DescribeDiskEventsRequest,
    ) -> ebs_20210730_models.DescribeDiskEventsResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: DescribeDiskEventsRequest
        @return: DescribeDiskEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_events_with_options(request, runtime)

    async def describe_disk_events_async(
        self,
        request: ebs_20210730_models.DescribeDiskEventsRequest,
    ) -> ebs_20210730_models.DescribeDiskEventsResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: DescribeDiskEventsRequest
        @return: DescribeDiskEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_events_with_options_async(request, runtime)

    def describe_disk_monitor_data_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataResponse:
        """
        ## Usage notes
        *   CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        *   Up to 400 monitoring data entries can be returned at a time. An error is returned if the value calculated based on the following formula is greater than 400: `(EndTime - StartTime)/Period`.
        *   You can query the monitoring data collected in the last three days. An error is returned if the time specified by `StartTime` is more than three days prior to the current time.
        
        @param request: DescribeDiskMonitorDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiskMonitorDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskMonitorData',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_monitor_data_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataResponse:
        """
        ## Usage notes
        *   CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        *   Up to 400 monitoring data entries can be returned at a time. An error is returned if the value calculated based on the following formula is greater than 400: `(EndTime - StartTime)/Period`.
        *   You can query the monitoring data collected in the last three days. An error is returned if the time specified by `StartTime` is more than three days prior to the current time.
        
        @param request: DescribeDiskMonitorDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiskMonitorDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskMonitorData',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_monitor_data(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataRequest,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataResponse:
        """
        ## Usage notes
        *   CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        *   Up to 400 monitoring data entries can be returned at a time. An error is returned if the value calculated based on the following formula is greater than 400: `(EndTime - StartTime)/Period`.
        *   You can query the monitoring data collected in the last three days. An error is returned if the time specified by `StartTime` is more than three days prior to the current time.
        
        @param request: DescribeDiskMonitorDataRequest
        @return: DescribeDiskMonitorDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_monitor_data_with_options(request, runtime)

    async def describe_disk_monitor_data_async(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataRequest,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataResponse:
        """
        ## Usage notes
        *   CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        *   Up to 400 monitoring data entries can be returned at a time. An error is returned if the value calculated based on the following formula is greater than 400: `(EndTime - StartTime)/Period`.
        *   You can query the monitoring data collected in the last three days. An error is returned if the time specified by `StartTime` is more than three days prior to the current time.
        
        @param request: DescribeDiskMonitorDataRequest
        @return: DescribeDiskMonitorDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_monitor_data_with_options_async(request, runtime)

    def describe_disk_monitor_data_list_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataListResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: DescribeDiskMonitorDataListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiskMonitorDataListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskMonitorDataList',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskMonitorDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_monitor_data_list_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataListResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: DescribeDiskMonitorDataListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiskMonitorDataListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskMonitorDataList',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskMonitorDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_monitor_data_list(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataListRequest,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataListResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: DescribeDiskMonitorDataListRequest
        @return: DescribeDiskMonitorDataListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_monitor_data_list_with_options(request, runtime)

    async def describe_disk_monitor_data_list_async(
        self,
        request: ebs_20210730_models.DescribeDiskMonitorDataListRequest,
    ) -> ebs_20210730_models.DescribeDiskMonitorDataListResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: DescribeDiskMonitorDataListRequest
        @return: DescribeDiskMonitorDataListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_monitor_data_list_with_options_async(request, runtime)

    def describe_disk_replica_groups_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaGroupsResponse:
        """
        To perform a paged query, set the MaxResults and NextToken parameters.
        During a paged query, when you call the DescribeDiskReplicaGroups operation to retrieve the first page of results, set `MaxResults` to specify the maximum number of entries to return in the call. The return value of `NextToken` is a pagination token, which can be used in the next call to retrieve a new page of results. When you call the DescribeDiskReplicaGroups operation to retrieve a new page of results, set `NextToken` to the `NextToken` value returned in the previous call and set MaxResults to specify the maximum number of entries to return in this call.
        
        @param request: DescribeDiskReplicaGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiskReplicaGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.site):
            query['Site'] = request.site
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaGroups',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_replica_groups_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaGroupsResponse:
        """
        To perform a paged query, set the MaxResults and NextToken parameters.
        During a paged query, when you call the DescribeDiskReplicaGroups operation to retrieve the first page of results, set `MaxResults` to specify the maximum number of entries to return in the call. The return value of `NextToken` is a pagination token, which can be used in the next call to retrieve a new page of results. When you call the DescribeDiskReplicaGroups operation to retrieve a new page of results, set `NextToken` to the `NextToken` value returned in the previous call and set MaxResults to specify the maximum number of entries to return in this call.
        
        @param request: DescribeDiskReplicaGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiskReplicaGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.site):
            query['Site'] = request.site
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaGroups',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_replica_groups(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaGroupsRequest,
    ) -> ebs_20210730_models.DescribeDiskReplicaGroupsResponse:
        """
        To perform a paged query, set the MaxResults and NextToken parameters.
        During a paged query, when you call the DescribeDiskReplicaGroups operation to retrieve the first page of results, set `MaxResults` to specify the maximum number of entries to return in the call. The return value of `NextToken` is a pagination token, which can be used in the next call to retrieve a new page of results. When you call the DescribeDiskReplicaGroups operation to retrieve a new page of results, set `NextToken` to the `NextToken` value returned in the previous call and set MaxResults to specify the maximum number of entries to return in this call.
        
        @param request: DescribeDiskReplicaGroupsRequest
        @return: DescribeDiskReplicaGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_replica_groups_with_options(request, runtime)

    async def describe_disk_replica_groups_async(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaGroupsRequest,
    ) -> ebs_20210730_models.DescribeDiskReplicaGroupsResponse:
        """
        To perform a paged query, set the MaxResults and NextToken parameters.
        During a paged query, when you call the DescribeDiskReplicaGroups operation to retrieve the first page of results, set `MaxResults` to specify the maximum number of entries to return in the call. The return value of `NextToken` is a pagination token, which can be used in the next call to retrieve a new page of results. When you call the DescribeDiskReplicaGroups operation to retrieve a new page of results, set `NextToken` to the `NextToken` value returned in the previous call and set MaxResults to specify the maximum number of entries to return in this call.
        
        @param request: DescribeDiskReplicaGroupsRequest
        @return: DescribeDiskReplicaGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_replica_groups_with_options_async(request, runtime)

    def describe_disk_replica_pair_progress_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaPairProgress',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaPairProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_replica_pair_progress_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaPairProgress',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaPairProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_replica_pair_progress(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairProgressRequest,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_replica_pair_progress_with_options(request, runtime)

    async def describe_disk_replica_pair_progress_async(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairProgressRequest,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_replica_pair_progress_with_options_async(request, runtime)

    def describe_disk_replica_pairs_with_options(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairsResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   When you call this operation for a specific region, if the primary disk (source disk) or secondary disk (destination disk) of a replication pair resides in the region, information about the replication pair is displayed in the response.
        *   If you want to perform a paged query, configure the `NextToken` and `MaxResults` parameters. During a paged query, when you call the DescribeDiskReplicaPairs operation to retrieve the first page of results, set `MaxResults` to limit the maximum number of entries to return in the call. The return value of NextToken is a pagination token, which can be used in the next call to retrieve a new page of results. When you call the DescribeDiskReplicaPairs operation to retrieve a new page of results, set NextToken to the NextToken value returned in the previous call and set MaxResults to specify the maximum number of entries to return in this call.
        
        @param request: DescribeDiskReplicaPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiskReplicaPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pair_ids):
            query['PairIds'] = request.pair_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.site):
            query['Site'] = request.site
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaPairs',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_replica_pairs_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairsResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   When you call this operation for a specific region, if the primary disk (source disk) or secondary disk (destination disk) of a replication pair resides in the region, information about the replication pair is displayed in the response.
        *   If you want to perform a paged query, configure the `NextToken` and `MaxResults` parameters. During a paged query, when you call the DescribeDiskReplicaPairs operation to retrieve the first page of results, set `MaxResults` to limit the maximum number of entries to return in the call. The return value of NextToken is a pagination token, which can be used in the next call to retrieve a new page of results. When you call the DescribeDiskReplicaPairs operation to retrieve a new page of results, set NextToken to the NextToken value returned in the previous call and set MaxResults to specify the maximum number of entries to return in this call.
        
        @param request: DescribeDiskReplicaPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiskReplicaPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pair_ids):
            query['PairIds'] = request.pair_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.site):
            query['Site'] = request.site
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiskReplicaPairs',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDiskReplicaPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_replica_pairs(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairsRequest,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairsResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   When you call this operation for a specific region, if the primary disk (source disk) or secondary disk (destination disk) of a replication pair resides in the region, information about the replication pair is displayed in the response.
        *   If you want to perform a paged query, configure the `NextToken` and `MaxResults` parameters. During a paged query, when you call the DescribeDiskReplicaPairs operation to retrieve the first page of results, set `MaxResults` to limit the maximum number of entries to return in the call. The return value of NextToken is a pagination token, which can be used in the next call to retrieve a new page of results. When you call the DescribeDiskReplicaPairs operation to retrieve a new page of results, set NextToken to the NextToken value returned in the previous call and set MaxResults to specify the maximum number of entries to return in this call.
        
        @param request: DescribeDiskReplicaPairsRequest
        @return: DescribeDiskReplicaPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_replica_pairs_with_options(request, runtime)

    async def describe_disk_replica_pairs_async(
        self,
        request: ebs_20210730_models.DescribeDiskReplicaPairsRequest,
    ) -> ebs_20210730_models.DescribeDiskReplicaPairsResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   When you call this operation for a specific region, if the primary disk (source disk) or secondary disk (destination disk) of a replication pair resides in the region, information about the replication pair is displayed in the response.
        *   If you want to perform a paged query, configure the `NextToken` and `MaxResults` parameters. During a paged query, when you call the DescribeDiskReplicaPairs operation to retrieve the first page of results, set `MaxResults` to limit the maximum number of entries to return in the call. The return value of NextToken is a pagination token, which can be used in the next call to retrieve a new page of results. When you call the DescribeDiskReplicaPairs operation to retrieve a new page of results, set NextToken to the NextToken value returned in the previous call and set MaxResults to specify the maximum number of entries to return in this call.
        
        @param request: DescribeDiskReplicaPairsRequest
        @return: DescribeDiskReplicaPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_replica_pairs_with_options_async(request, runtime)

    def describe_disks_with_options(
        self,
        request: ebs_20210730_models.DescribeDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDisksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.disk_name):
            query['DiskName'] = request.disk_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDisks',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disks_with_options_async(
        self,
        request: ebs_20210730_models.DescribeDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeDisksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.disk_name):
            query['DiskName'] = request.disk_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDisks',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeDisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disks(
        self,
        request: ebs_20210730_models.DescribeDisksRequest,
    ) -> ebs_20210730_models.DescribeDisksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disks_with_options(request, runtime)

    async def describe_disks_async(
        self,
        request: ebs_20210730_models.DescribeDisksRequest,
    ) -> ebs_20210730_models.DescribeDisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disks_with_options_async(request, runtime)

    def describe_enterprise_snapshot_policy_with_options(
        self,
        request: ebs_20210730_models.DescribeEnterpriseSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeEnterpriseSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_ids):
            query['PolicyIds'] = request.policy_ids
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
            action='DescribeEnterpriseSnapshotPolicy',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeEnterpriseSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_enterprise_snapshot_policy_with_options_async(
        self,
        request: ebs_20210730_models.DescribeEnterpriseSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeEnterpriseSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_ids):
            query['PolicyIds'] = request.policy_ids
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
            action='DescribeEnterpriseSnapshotPolicy',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeEnterpriseSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_enterprise_snapshot_policy(
        self,
        request: ebs_20210730_models.DescribeEnterpriseSnapshotPolicyRequest,
    ) -> ebs_20210730_models.DescribeEnterpriseSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_enterprise_snapshot_policy_with_options(request, runtime)

    async def describe_enterprise_snapshot_policy_async(
        self,
        request: ebs_20210730_models.DescribeEnterpriseSnapshotPolicyRequest,
    ) -> ebs_20210730_models.DescribeEnterpriseSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_enterprise_snapshot_policy_with_options_async(request, runtime)

    def describe_lens_service_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeLensServiceStatusResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: DescribeLensServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLensServiceStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeLensServiceStatus',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeLensServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lens_service_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeLensServiceStatusResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @param request: DescribeLensServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLensServiceStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeLensServiceStatus',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeLensServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lens_service_status(self) -> ebs_20210730_models.DescribeLensServiceStatusResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @return: DescribeLensServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_lens_service_status_with_options(runtime)

    async def describe_lens_service_status_async(self) -> ebs_20210730_models.DescribeLensServiceStatusResponse:
        """
        ## Usage notes
        CloudLens for EBS is in invitational preview in the China (Hangzhou), China (Shanghai), China (Zhangjiakou), China (Shenzhen), and China (Hong Kong) regions. To use the feature, [submit a ticket](https://workorder-intl.console.aliyun.com/#/ticket/createIndex).
        
        @return: DescribeLensServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_lens_service_status_with_options_async(runtime)

    def describe_metric_data_with_options(
        self,
        request: ebs_20210730_models.DescribeMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
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
            action='DescribeMetricData',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_data_with_options_async(
        self,
        request: ebs_20210730_models.DescribeMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
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
            action='DescribeMetricData',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_data(
        self,
        request: ebs_20210730_models.DescribeMetricDataRequest,
    ) -> ebs_20210730_models.DescribeMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_data_with_options(request, runtime)

    async def describe_metric_data_async(
        self,
        request: ebs_20210730_models.DescribeMetricDataRequest,
    ) -> ebs_20210730_models.DescribeMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_data_with_options_async(request, runtime)

    def describe_pair_drills_with_options(
        self,
        request: ebs_20210730_models.DescribePairDrillsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribePairDrillsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drill_id):
            query['DrillId'] = request.drill_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pair_id):
            query['PairId'] = request.pair_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePairDrills',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribePairDrillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pair_drills_with_options_async(
        self,
        request: ebs_20210730_models.DescribePairDrillsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribePairDrillsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drill_id):
            query['DrillId'] = request.drill_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pair_id):
            query['PairId'] = request.pair_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePairDrills',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribePairDrillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pair_drills(
        self,
        request: ebs_20210730_models.DescribePairDrillsRequest,
    ) -> ebs_20210730_models.DescribePairDrillsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pair_drills_with_options(request, runtime)

    async def describe_pair_drills_async(
        self,
        request: ebs_20210730_models.DescribePairDrillsRequest,
    ) -> ebs_20210730_models.DescribePairDrillsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pair_drills_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ebs_20210730_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ebs_20210730_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: ebs_20210730_models.DescribeRegionsRequest,
    ) -> ebs_20210730_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ebs_20210730_models.DescribeRegionsRequest,
    ) -> ebs_20210730_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_replica_group_drills_with_options(
        self,
        request: ebs_20210730_models.DescribeReplicaGroupDrillsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeReplicaGroupDrillsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drill_id):
            query['DrillId'] = request.drill_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            action='DescribeReplicaGroupDrills',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeReplicaGroupDrillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_replica_group_drills_with_options_async(
        self,
        request: ebs_20210730_models.DescribeReplicaGroupDrillsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeReplicaGroupDrillsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drill_id):
            query['DrillId'] = request.drill_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            action='DescribeReplicaGroupDrills',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeReplicaGroupDrillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_replica_group_drills(
        self,
        request: ebs_20210730_models.DescribeReplicaGroupDrillsRequest,
    ) -> ebs_20210730_models.DescribeReplicaGroupDrillsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_replica_group_drills_with_options(request, runtime)

    async def describe_replica_group_drills_async(
        self,
        request: ebs_20210730_models.DescribeReplicaGroupDrillsRequest,
    ) -> ebs_20210730_models.DescribeReplicaGroupDrillsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_replica_group_drills_with_options_async(request, runtime)

    def describe_solution_instance_configuration_with_options(
        self,
        request: ebs_20210730_models.DescribeSolutionInstanceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeSolutionInstanceConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.solution_id):
            query['SolutionId'] = request.solution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSolutionInstanceConfiguration',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeSolutionInstanceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_solution_instance_configuration_with_options_async(
        self,
        request: ebs_20210730_models.DescribeSolutionInstanceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.DescribeSolutionInstanceConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.solution_id):
            query['SolutionId'] = request.solution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSolutionInstanceConfiguration',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.DescribeSolutionInstanceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_solution_instance_configuration(
        self,
        request: ebs_20210730_models.DescribeSolutionInstanceConfigurationRequest,
    ) -> ebs_20210730_models.DescribeSolutionInstanceConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_solution_instance_configuration_with_options(request, runtime)

    async def describe_solution_instance_configuration_async(
        self,
        request: ebs_20210730_models.DescribeSolutionInstanceConfigurationRequest,
    ) -> ebs_20210730_models.DescribeSolutionInstanceConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_solution_instance_configuration_with_options_async(request, runtime)

    def failover_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.FailoverDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group must be in the **One-time Syncing** (`manual_syncing`), **Syncing** (`syncing`), **Normal** (`normal`), **Stopping** (`stopping`), **Stop Failed** (`stop_failed`), **Stopped** (`stopped`), **In Failover** (`failovering`), **Failover Failed** (`failover_failed`), or **Failovered** (`failovered`) state.
        *   After a failover is performed, the replication pair-consistent group enters the **Failovered** (`failovered`) state.
        *   Before you perform a failover, make sure that the first full data synchronization is completed between the primary site and secondary site.
        
        @param request: FailoverDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FailoverDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailoverDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.FailoverDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def failover_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.FailoverDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group must be in the **One-time Syncing** (`manual_syncing`), **Syncing** (`syncing`), **Normal** (`normal`), **Stopping** (`stopping`), **Stop Failed** (`stop_failed`), **Stopped** (`stopped`), **In Failover** (`failovering`), **Failover Failed** (`failover_failed`), or **Failovered** (`failovered`) state.
        *   After a failover is performed, the replication pair-consistent group enters the **Failovered** (`failovered`) state.
        *   Before you perform a failover, make sure that the first full data synchronization is completed between the primary site and secondary site.
        
        @param request: FailoverDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FailoverDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailoverDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.FailoverDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def failover_disk_replica_group(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.FailoverDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group must be in the **One-time Syncing** (`manual_syncing`), **Syncing** (`syncing`), **Normal** (`normal`), **Stopping** (`stopping`), **Stop Failed** (`stop_failed`), **Stopped** (`stopped`), **In Failover** (`failovering`), **Failover Failed** (`failover_failed`), or **Failovered** (`failovered`) state.
        *   After a failover is performed, the replication pair-consistent group enters the **Failovered** (`failovered`) state.
        *   Before you perform a failover, make sure that the first full data synchronization is completed between the primary site and secondary site.
        
        @param request: FailoverDiskReplicaGroupRequest
        @return: FailoverDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.failover_disk_replica_group_with_options(request, runtime)

    async def failover_disk_replica_group_async(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.FailoverDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group must be in the **One-time Syncing** (`manual_syncing`), **Syncing** (`syncing`), **Normal** (`normal`), **Stopping** (`stopping`), **Stop Failed** (`stop_failed`), **Stopped** (`stopped`), **In Failover** (`failovering`), **Failover Failed** (`failover_failed`), or **Failovered** (`failovered`) state.
        *   After a failover is performed, the replication pair-consistent group enters the **Failovered** (`failovered`) state.
        *   Before you perform a failover, make sure that the first full data synchronization is completed between the primary site and secondary site.
        
        @param request: FailoverDiskReplicaGroupRequest
        @return: FailoverDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.failover_disk_replica_group_with_options_async(request, runtime)

    def failover_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.FailoverDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   The replication pair for which you want to enable failover cannot be in the **Invalid** (`invalid`) or **Deleted** (`deleted`) state.
        *   After a failover is performed, the replication pair enters the **Failovered** (`failovered`) state.
        
        @param request: FailoverDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FailoverDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailoverDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.FailoverDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def failover_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.FailoverDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   The replication pair for which you want to enable failover cannot be in the **Invalid** (`invalid`) or **Deleted** (`deleted`) state.
        *   After a failover is performed, the replication pair enters the **Failovered** (`failovered`) state.
        
        @param request: FailoverDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FailoverDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FailoverDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.FailoverDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def failover_disk_replica_pair(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaPairRequest,
    ) -> ebs_20210730_models.FailoverDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   The replication pair for which you want to enable failover cannot be in the **Invalid** (`invalid`) or **Deleted** (`deleted`) state.
        *   After a failover is performed, the replication pair enters the **Failovered** (`failovered`) state.
        
        @param request: FailoverDiskReplicaPairRequest
        @return: FailoverDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.failover_disk_replica_pair_with_options(request, runtime)

    async def failover_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.FailoverDiskReplicaPairRequest,
    ) -> ebs_20210730_models.FailoverDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   The replication pair for which you want to enable failover cannot be in the **Invalid** (`invalid`) or **Deleted** (`deleted`) state.
        *   After a failover is performed, the replication pair enters the **Failovered** (`failovered`) state.
        
        @param request: FailoverDiskReplicaPairRequest
        @return: FailoverDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.failover_disk_replica_pair_with_options_async(request, runtime)

    def get_disk_with_options(
        self,
        request: ebs_20210730_models.GetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.GetDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDisk',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.GetDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_disk_with_options_async(
        self,
        request: ebs_20210730_models.GetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.GetDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDisk',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.GetDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_disk(
        self,
        request: ebs_20210730_models.GetDiskRequest,
    ) -> ebs_20210730_models.GetDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_disk_with_options(request, runtime)

    async def get_disk_async(
        self,
        request: ebs_20210730_models.GetDiskRequest,
    ) -> ebs_20210730_models.GetDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_disk_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ebs_20210730_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ListTagResourcesResponse:
        """
        Specify at least one of the following parameters or parameter pairs in a request to determine a query object:
        *   `ResourceId.N`
        *   `Tag.N` parameter pair (`Tag.N.Key` and `Tag.N.Value`)
        If you set `Tag.N` and `ResourceId.N` at the same time, the EBS resources that match both the parameters are returned.
        
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
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ebs_20210730_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ListTagResourcesResponse:
        """
        Specify at least one of the following parameters or parameter pairs in a request to determine a query object:
        *   `ResourceId.N`
        *   `Tag.N` parameter pair (`Tag.N.Key` and `Tag.N.Value`)
        If you set `Tag.N` and `ResourceId.N` at the same time, the EBS resources that match both the parameters are returned.
        
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
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: ebs_20210730_models.ListTagResourcesRequest,
    ) -> ebs_20210730_models.ListTagResourcesResponse:
        """
        Specify at least one of the following parameters or parameter pairs in a request to determine a query object:
        *   `ResourceId.N`
        *   `Tag.N` parameter pair (`Tag.N.Key` and `Tag.N.Value`)
        If you set `Tag.N` and `ResourceId.N` at the same time, the EBS resources that match both the parameters are returned.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ebs_20210730_models.ListTagResourcesRequest,
    ) -> ebs_20210730_models.ListTagResourcesResponse:
        """
        Specify at least one of the following parameters or parameter pairs in a request to determine a query object:
        *   `ResourceId.N`
        *   `Tag.N` parameter pair (`Tag.N.Key` and `Tag.N.Value`)
        If you set `Tag.N` and `ResourceId.N` at the same time, the EBS resources that match both the parameters are returned.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_dedicated_block_storage_cluster_attribute_with_options(
        self,
        request: ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeResponse:
        """
        You can call this operation to modify the information of a dedicated block storage cluster. The information includes the name and description of the cluster.
        
        @param request: ModifyDedicatedBlockStorageClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedBlockStorageClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.dbsc_name):
            query['DbscName'] = request.dbsc_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedBlockStorageClusterAttribute',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dedicated_block_storage_cluster_attribute_with_options_async(
        self,
        request: ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeResponse:
        """
        You can call this operation to modify the information of a dedicated block storage cluster. The information includes the name and description of the cluster.
        
        @param request: ModifyDedicatedBlockStorageClusterAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDedicatedBlockStorageClusterAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbsc_id):
            query['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.dbsc_name):
            query['DbscName'] = request.dbsc_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDedicatedBlockStorageClusterAttribute',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dedicated_block_storage_cluster_attribute(
        self,
        request: ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeRequest,
    ) -> ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeResponse:
        """
        You can call this operation to modify the information of a dedicated block storage cluster. The information includes the name and description of the cluster.
        
        @param request: ModifyDedicatedBlockStorageClusterAttributeRequest
        @return: ModifyDedicatedBlockStorageClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_block_storage_cluster_attribute_with_options(request, runtime)

    async def modify_dedicated_block_storage_cluster_attribute_async(
        self,
        request: ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeRequest,
    ) -> ebs_20210730_models.ModifyDedicatedBlockStorageClusterAttributeResponse:
        """
        You can call this operation to modify the information of a dedicated block storage cluster. The information includes the name and description of the cluster.
        
        @param request: ModifyDedicatedBlockStorageClusterAttributeRequest
        @return: ModifyDedicatedBlockStorageClusterAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_block_storage_cluster_attribute_with_options_async(request, runtime)

    def modify_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group must be in the **Created** (`created`) or **Stopped** (`stopped`) state.
        
        @param request: ModifyDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group must be in the **Created** (`created`) or **Stopped** (`stopped`) state.
        
        @param request: ModifyDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_replica_group(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.ModifyDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group must be in the **Created** (`created`) or **Stopped** (`stopped`) state.
        
        @param request: ModifyDiskReplicaGroupRequest
        @return: ModifyDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_replica_group_with_options(request, runtime)

    async def modify_disk_replica_group_async(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.ModifyDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group must be in the **Created** (`created`) or **Stopped** (`stopped`) state.
        
        @param request: ModifyDiskReplicaGroupRequest
        @return: ModifyDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_replica_group_with_options_async(request, runtime)

    def modify_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Created** (`created`) or **Stopped** (`stopped`) state can have their names or descriptions modified.
        
        @param request: ModifyDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.pair_name):
            query['PairName'] = request.pair_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ModifyDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Created** (`created`) or **Stopped** (`stopped`) state can have their names or descriptions modified.
        
        @param request: ModifyDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.pair_name):
            query['PairName'] = request.pair_name
        if not UtilClient.is_unset(request.rpo):
            query['RPO'] = request.rpo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ModifyDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_replica_pair(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaPairRequest,
    ) -> ebs_20210730_models.ModifyDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Created** (`created`) or **Stopped** (`stopped`) state can have their names or descriptions modified.
        
        @param request: ModifyDiskReplicaPairRequest
        @return: ModifyDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_replica_pair_with_options(request, runtime)

    async def modify_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.ModifyDiskReplicaPairRequest,
    ) -> ebs_20210730_models.ModifyDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Created** (`created`) or **Stopped** (`stopped`) state can have their names or descriptions modified.
        
        @param request: ModifyDiskReplicaPairRequest
        @return: ModifyDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_replica_pair_with_options_async(request, runtime)

    def query_dedicated_block_storage_cluster_disk_throughput_status_with_options(
        self,
        request: ebs_20210730_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.qos_request_id):
            body['QosRequestId'] = request.qos_request_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDedicatedBlockStorageClusterDiskThroughputStatus',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dedicated_block_storage_cluster_disk_throughput_status_with_options_async(
        self,
        request: ebs_20210730_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.qos_request_id):
            body['QosRequestId'] = request.qos_request_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDedicatedBlockStorageClusterDiskThroughputStatus',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dedicated_block_storage_cluster_disk_throughput_status(
        self,
        request: ebs_20210730_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusRequest,
    ) -> ebs_20210730_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dedicated_block_storage_cluster_disk_throughput_status_with_options(request, runtime)

    async def query_dedicated_block_storage_cluster_disk_throughput_status_async(
        self,
        request: ebs_20210730_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusRequest,
    ) -> ebs_20210730_models.QueryDedicatedBlockStorageClusterDiskThroughputStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dedicated_block_storage_cluster_disk_throughput_status_with_options_async(request, runtime)

    def query_dedicated_block_storage_cluster_inventory_data_with_options(
        self,
        request: ebs_20210730_models.QueryDedicatedBlockStorageClusterInventoryDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.QueryDedicatedBlockStorageClusterInventoryDataResponse:
        """
        Period is the time interval between data retrieval points. When set to 60 (minute interval), a maximum of 1440 data points can be returned; when set to 3600 (hour interval), a maximum of 744 data points can be returned; and when set to 86400 (day interval), a maximum of 366 data points can be returned.
        
        @param request: QueryDedicatedBlockStorageClusterInventoryDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDedicatedBlockStorageClusterInventoryDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.dbsc_id):
            body['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDedicatedBlockStorageClusterInventoryData',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.QueryDedicatedBlockStorageClusterInventoryDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dedicated_block_storage_cluster_inventory_data_with_options_async(
        self,
        request: ebs_20210730_models.QueryDedicatedBlockStorageClusterInventoryDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.QueryDedicatedBlockStorageClusterInventoryDataResponse:
        """
        Period is the time interval between data retrieval points. When set to 60 (minute interval), a maximum of 1440 data points can be returned; when set to 3600 (hour interval), a maximum of 744 data points can be returned; and when set to 86400 (day interval), a maximum of 366 data points can be returned.
        
        @param request: QueryDedicatedBlockStorageClusterInventoryDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDedicatedBlockStorageClusterInventoryDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.dbsc_id):
            body['DbscId'] = request.dbsc_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDedicatedBlockStorageClusterInventoryData',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.QueryDedicatedBlockStorageClusterInventoryDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dedicated_block_storage_cluster_inventory_data(
        self,
        request: ebs_20210730_models.QueryDedicatedBlockStorageClusterInventoryDataRequest,
    ) -> ebs_20210730_models.QueryDedicatedBlockStorageClusterInventoryDataResponse:
        """
        Period is the time interval between data retrieval points. When set to 60 (minute interval), a maximum of 1440 data points can be returned; when set to 3600 (hour interval), a maximum of 744 data points can be returned; and when set to 86400 (day interval), a maximum of 366 data points can be returned.
        
        @param request: QueryDedicatedBlockStorageClusterInventoryDataRequest
        @return: QueryDedicatedBlockStorageClusterInventoryDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_dedicated_block_storage_cluster_inventory_data_with_options(request, runtime)

    async def query_dedicated_block_storage_cluster_inventory_data_async(
        self,
        request: ebs_20210730_models.QueryDedicatedBlockStorageClusterInventoryDataRequest,
    ) -> ebs_20210730_models.QueryDedicatedBlockStorageClusterInventoryDataResponse:
        """
        Period is the time interval between data retrieval points. When set to 60 (minute interval), a maximum of 1440 data points can be returned; when set to 3600 (hour interval), a maximum of 744 data points can be returned; and when set to 86400 (day interval), a maximum of 366 data points can be returned.
        
        @param request: QueryDedicatedBlockStorageClusterInventoryDataRequest
        @return: QueryDedicatedBlockStorageClusterInventoryDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_dedicated_block_storage_cluster_inventory_data_with_options_async(request, runtime)

    def remove_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.RemoveDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.RemoveDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group from which you want to remove a replication pair must be in the **Created** (`created`), **Stopped** (`stopped`), or **Invalid** (`invalid`) state.
        
        @param request: RemoveDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.RemoveDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.RemoveDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.RemoveDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group from which you want to remove a replication pair must be in the **Created** (`created`), **Stopped** (`stopped`), or **Invalid** (`invalid`) state.
        
        @param request: RemoveDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.RemoveDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_disk_replica_pair(
        self,
        request: ebs_20210730_models.RemoveDiskReplicaPairRequest,
    ) -> ebs_20210730_models.RemoveDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group from which you want to remove a replication pair must be in the **Created** (`created`), **Stopped** (`stopped`), or **Invalid** (`invalid`) state.
        
        @param request: RemoveDiskReplicaPairRequest
        @return: RemoveDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_disk_replica_pair_with_options(request, runtime)

    async def remove_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.RemoveDiskReplicaPairRequest,
    ) -> ebs_20210730_models.RemoveDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group from which you want to remove a replication pair must be in the **Created** (`created`), **Stopped** (`stopped`), or **Invalid** (`invalid`) state.
        
        @param request: RemoveDiskReplicaPairRequest
        @return: RemoveDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_disk_replica_pair_with_options_async(request, runtime)

    def reprotect_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ReprotectDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group for which you want to enable reverse replication must be in the **Failovered** (`failovered`) state. You can call the `FailoverDiskReplicaPair` operation to enable failover.
        *   Before a reverse replication is performed, the primary disks must be detached from its associated Elastic Compute Service (ECS) instance and must be in the Unattached state. You can call the [DetachDisk](~~25516~~) operation to detach the disks.
        *   After you enable reverse replication, you must call the `StartDiskReplicaPair` operation again to enable the async replication feature before data can be replicated from the original secondary disks to the original primary disks.
        *   You can set the ReverseReplicate parameter to false to cancel the **Failovered** (`failovered`) state and restore the original replication direction.
        
        @param request: ReprotectDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReprotectDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.reverse_replicate):
            query['ReverseReplicate'] = request.reverse_replicate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReprotectDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ReprotectDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def reprotect_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ReprotectDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group for which you want to enable reverse replication must be in the **Failovered** (`failovered`) state. You can call the `FailoverDiskReplicaPair` operation to enable failover.
        *   Before a reverse replication is performed, the primary disks must be detached from its associated Elastic Compute Service (ECS) instance and must be in the Unattached state. You can call the [DetachDisk](~~25516~~) operation to detach the disks.
        *   After you enable reverse replication, you must call the `StartDiskReplicaPair` operation again to enable the async replication feature before data can be replicated from the original secondary disks to the original primary disks.
        *   You can set the ReverseReplicate parameter to false to cancel the **Failovered** (`failovered`) state and restore the original replication direction.
        
        @param request: ReprotectDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReprotectDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        if not UtilClient.is_unset(request.reverse_replicate):
            query['ReverseReplicate'] = request.reverse_replicate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReprotectDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ReprotectDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reprotect_disk_replica_group(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.ReprotectDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group for which you want to enable reverse replication must be in the **Failovered** (`failovered`) state. You can call the `FailoverDiskReplicaPair` operation to enable failover.
        *   Before a reverse replication is performed, the primary disks must be detached from its associated Elastic Compute Service (ECS) instance and must be in the Unattached state. You can call the [DetachDisk](~~25516~~) operation to detach the disks.
        *   After you enable reverse replication, you must call the `StartDiskReplicaPair` operation again to enable the async replication feature before data can be replicated from the original secondary disks to the original primary disks.
        *   You can set the ReverseReplicate parameter to false to cancel the **Failovered** (`failovered`) state and restore the original replication direction.
        
        @param request: ReprotectDiskReplicaGroupRequest
        @return: ReprotectDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reprotect_disk_replica_group_with_options(request, runtime)

    async def reprotect_disk_replica_group_async(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.ReprotectDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group for which you want to enable reverse replication must be in the **Failovered** (`failovered`) state. You can call the `FailoverDiskReplicaPair` operation to enable failover.
        *   Before a reverse replication is performed, the primary disks must be detached from its associated Elastic Compute Service (ECS) instance and must be in the Unattached state. You can call the [DetachDisk](~~25516~~) operation to detach the disks.
        *   After you enable reverse replication, you must call the `StartDiskReplicaPair` operation again to enable the async replication feature before data can be replicated from the original secondary disks to the original primary disks.
        *   You can set the ReverseReplicate parameter to false to cancel the **Failovered** (`failovered`) state and restore the original replication direction.
        
        @param request: ReprotectDiskReplicaGroupRequest
        @return: ReprotectDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reprotect_disk_replica_group_with_options_async(request, runtime)

    def reprotect_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ReprotectDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   The replication pair for which you want to enable reverse replication must be in the **Failovered** (`failovered`) state. You can call the [FailoverDiskReplicaPair](~~354358~~) operation to enable failover.
        *   The primary disk must be detached from its associated Elastic Compute Service (ECS) instance and is in the Unattached state. You can call the [DetachDisk](~~25516~~) operation to detach the disk.
        *   After you enable reverse replication, you must call the [StartDiskReplicaPair](~~354205~~) operation again to activate the replication pair before data can be replicated from the original secondary disk to the original primary disk.
        *   You can set the ReverseReplicate parameter to false to cancel the **Failovered** (`failovered`) state and restore the original replication direction.
        
        @param request: ReprotectDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReprotectDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        if not UtilClient.is_unset(request.reverse_replicate):
            query['ReverseReplicate'] = request.reverse_replicate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReprotectDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ReprotectDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def reprotect_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.ReprotectDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   The replication pair for which you want to enable reverse replication must be in the **Failovered** (`failovered`) state. You can call the [FailoverDiskReplicaPair](~~354358~~) operation to enable failover.
        *   The primary disk must be detached from its associated Elastic Compute Service (ECS) instance and is in the Unattached state. You can call the [DetachDisk](~~25516~~) operation to detach the disk.
        *   After you enable reverse replication, you must call the [StartDiskReplicaPair](~~354205~~) operation again to activate the replication pair before data can be replicated from the original secondary disk to the original primary disk.
        *   You can set the ReverseReplicate parameter to false to cancel the **Failovered** (`failovered`) state and restore the original replication direction.
        
        @param request: ReprotectDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReprotectDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        if not UtilClient.is_unset(request.reverse_replicate):
            query['ReverseReplicate'] = request.reverse_replicate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReprotectDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.ReprotectDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reprotect_disk_replica_pair(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaPairRequest,
    ) -> ebs_20210730_models.ReprotectDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   The replication pair for which you want to enable reverse replication must be in the **Failovered** (`failovered`) state. You can call the [FailoverDiskReplicaPair](~~354358~~) operation to enable failover.
        *   The primary disk must be detached from its associated Elastic Compute Service (ECS) instance and is in the Unattached state. You can call the [DetachDisk](~~25516~~) operation to detach the disk.
        *   After you enable reverse replication, you must call the [StartDiskReplicaPair](~~354205~~) operation again to activate the replication pair before data can be replicated from the original secondary disk to the original primary disk.
        *   You can set the ReverseReplicate parameter to false to cancel the **Failovered** (`failovered`) state and restore the original replication direction.
        
        @param request: ReprotectDiskReplicaPairRequest
        @return: ReprotectDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reprotect_disk_replica_pair_with_options(request, runtime)

    async def reprotect_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.ReprotectDiskReplicaPairRequest,
    ) -> ebs_20210730_models.ReprotectDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   The replication pair for which you want to enable reverse replication must be in the **Failovered** (`failovered`) state. You can call the [FailoverDiskReplicaPair](~~354358~~) operation to enable failover.
        *   The primary disk must be detached from its associated Elastic Compute Service (ECS) instance and is in the Unattached state. You can call the [DetachDisk](~~25516~~) operation to detach the disk.
        *   After you enable reverse replication, you must call the [StartDiskReplicaPair](~~354205~~) operation again to activate the replication pair before data can be replicated from the original secondary disk to the original primary disk.
        *   You can set the ReverseReplicate parameter to false to cancel the **Failovered** (`failovered`) state and restore the original replication direction.
        
        @param request: ReprotectDiskReplicaPairRequest
        @return: ReprotectDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reprotect_disk_replica_pair_with_options_async(request, runtime)

    def set_dedicated_block_storage_cluster_disk_throughput_with_options(
        self,
        request: ebs_20210730_models.SetDedicatedBlockStorageClusterDiskThroughputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.SetDedicatedBlockStorageClusterDiskThroughputResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.bps):
            body['Bps'] = request.bps
        if not UtilClient.is_unset(request.disk_id):
            body['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDedicatedBlockStorageClusterDiskThroughput',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.SetDedicatedBlockStorageClusterDiskThroughputResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dedicated_block_storage_cluster_disk_throughput_with_options_async(
        self,
        request: ebs_20210730_models.SetDedicatedBlockStorageClusterDiskThroughputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.SetDedicatedBlockStorageClusterDiskThroughputResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.bps):
            body['Bps'] = request.bps
        if not UtilClient.is_unset(request.disk_id):
            body['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDedicatedBlockStorageClusterDiskThroughput',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.SetDedicatedBlockStorageClusterDiskThroughputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dedicated_block_storage_cluster_disk_throughput(
        self,
        request: ebs_20210730_models.SetDedicatedBlockStorageClusterDiskThroughputRequest,
    ) -> ebs_20210730_models.SetDedicatedBlockStorageClusterDiskThroughputResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_dedicated_block_storage_cluster_disk_throughput_with_options(request, runtime)

    async def set_dedicated_block_storage_cluster_disk_throughput_async(
        self,
        request: ebs_20210730_models.SetDedicatedBlockStorageClusterDiskThroughputRequest,
    ) -> ebs_20210730_models.SetDedicatedBlockStorageClusterDiskThroughputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dedicated_block_storage_cluster_disk_throughput_with_options_async(request, runtime)

    def start_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.StartDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   If you set the `OneShot` to `false`, the replication pair-consistent group must be in the **Created** (`created` ), **Synchronizing** (`syncing` ), **Normal** (`normal` ), or **Stopped** (`stopped`) state.
        *   If you set `OneShot` to `true`, the replication pair-consistent group must be in the **Created** (`created` ), **One-time Syncing** (`manual_syncing` ), or **Stopped** (`stopped`) state. The time interval between two consecutive one-time synchronizations must be longer than one half of the recovery point objective (RPO).
        *   After a replication pair-consistent group is activated, the group enters the **Initial Syncing** (`initial_syncing`) state and the system performs the first async replication to replicate all data from the primary disks to secondary disks.
        
        @param request: StartDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.one_shot):
            query['OneShot'] = request.one_shot
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.StartDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   If you set the `OneShot` to `false`, the replication pair-consistent group must be in the **Created** (`created` ), **Synchronizing** (`syncing` ), **Normal** (`normal` ), or **Stopped** (`stopped`) state.
        *   If you set `OneShot` to `true`, the replication pair-consistent group must be in the **Created** (`created` ), **One-time Syncing** (`manual_syncing` ), or **Stopped** (`stopped`) state. The time interval between two consecutive one-time synchronizations must be longer than one half of the recovery point objective (RPO).
        *   After a replication pair-consistent group is activated, the group enters the **Initial Syncing** (`initial_syncing`) state and the system performs the first async replication to replicate all data from the primary disks to secondary disks.
        
        @param request: StartDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.one_shot):
            query['OneShot'] = request.one_shot
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_disk_replica_group(
        self,
        request: ebs_20210730_models.StartDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.StartDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   If you set the `OneShot` to `false`, the replication pair-consistent group must be in the **Created** (`created` ), **Synchronizing** (`syncing` ), **Normal** (`normal` ), or **Stopped** (`stopped`) state.
        *   If you set `OneShot` to `true`, the replication pair-consistent group must be in the **Created** (`created` ), **One-time Syncing** (`manual_syncing` ), or **Stopped** (`stopped`) state. The time interval between two consecutive one-time synchronizations must be longer than one half of the recovery point objective (RPO).
        *   After a replication pair-consistent group is activated, the group enters the **Initial Syncing** (`initial_syncing`) state and the system performs the first async replication to replicate all data from the primary disks to secondary disks.
        
        @param request: StartDiskReplicaGroupRequest
        @return: StartDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_disk_replica_group_with_options(request, runtime)

    async def start_disk_replica_group_async(
        self,
        request: ebs_20210730_models.StartDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.StartDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   If you set the `OneShot` to `false`, the replication pair-consistent group must be in the **Created** (`created` ), **Synchronizing** (`syncing` ), **Normal** (`normal` ), or **Stopped** (`stopped`) state.
        *   If you set `OneShot` to `true`, the replication pair-consistent group must be in the **Created** (`created` ), **One-time Syncing** (`manual_syncing` ), or **Stopped** (`stopped`) state. The time interval between two consecutive one-time synchronizations must be longer than one half of the recovery point objective (RPO).
        *   After a replication pair-consistent group is activated, the group enters the **Initial Syncing** (`initial_syncing`) state and the system performs the first async replication to replicate all data from the primary disks to secondary disks.
        
        @param request: StartDiskReplicaGroupRequest
        @return: StartDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_disk_replica_group_with_options_async(request, runtime)

    def start_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.StartDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Created** (`created`) or **Stopped** (`stopped`) state can be activated.
        *   After a replication pair is activated, it enters the **Initial Syncing** (`initial_syncing`) state and the system performs the first asynchronous replication to replicate all data from the primary disk to the secondary disk.
        
        @param request: StartDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.one_shot):
            query['OneShot'] = request.one_shot
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.StartDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Created** (`created`) or **Stopped** (`stopped`) state can be activated.
        *   After a replication pair is activated, it enters the **Initial Syncing** (`initial_syncing`) state and the system performs the first asynchronous replication to replicate all data from the primary disk to the secondary disk.
        
        @param request: StartDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.one_shot):
            query['OneShot'] = request.one_shot
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_disk_replica_pair(
        self,
        request: ebs_20210730_models.StartDiskReplicaPairRequest,
    ) -> ebs_20210730_models.StartDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Created** (`created`) or **Stopped** (`stopped`) state can be activated.
        *   After a replication pair is activated, it enters the **Initial Syncing** (`initial_syncing`) state and the system performs the first asynchronous replication to replicate all data from the primary disk to the secondary disk.
        
        @param request: StartDiskReplicaPairRequest
        @return: StartDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_disk_replica_pair_with_options(request, runtime)

    async def start_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.StartDiskReplicaPairRequest,
    ) -> ebs_20210730_models.StartDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Created** (`created`) or **Stopped** (`stopped`) state can be activated.
        *   After a replication pair is activated, it enters the **Initial Syncing** (`initial_syncing`) state and the system performs the first asynchronous replication to replicate all data from the primary disk to the secondary disk.
        
        @param request: StartDiskReplicaPairRequest
        @return: StartDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_disk_replica_pair_with_options_async(request, runtime)

    def start_pair_drill_with_options(
        self,
        request: ebs_20210730_models.StartPairDrillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartPairDrillResponse:
        """
        After the disaster recovery drill is complete on the secondary disk, a pay-as-you-go drill disk that has the same capacity and category as the secondary disk is created in the zone where the secondary disk resides. The drill disk contains last-recovery-point data that can be used to test the completeness and correctness of applications.
        
        @param request: StartPairDrillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartPairDrillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.pair_id):
            query['PairId'] = request.pair_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPairDrill',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartPairDrillResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_pair_drill_with_options_async(
        self,
        request: ebs_20210730_models.StartPairDrillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartPairDrillResponse:
        """
        After the disaster recovery drill is complete on the secondary disk, a pay-as-you-go drill disk that has the same capacity and category as the secondary disk is created in the zone where the secondary disk resides. The drill disk contains last-recovery-point data that can be used to test the completeness and correctness of applications.
        
        @param request: StartPairDrillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartPairDrillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.pair_id):
            query['PairId'] = request.pair_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPairDrill',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartPairDrillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_pair_drill(
        self,
        request: ebs_20210730_models.StartPairDrillRequest,
    ) -> ebs_20210730_models.StartPairDrillResponse:
        """
        After the disaster recovery drill is complete on the secondary disk, a pay-as-you-go drill disk that has the same capacity and category as the secondary disk is created in the zone where the secondary disk resides. The drill disk contains last-recovery-point data that can be used to test the completeness and correctness of applications.
        
        @param request: StartPairDrillRequest
        @return: StartPairDrillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_pair_drill_with_options(request, runtime)

    async def start_pair_drill_async(
        self,
        request: ebs_20210730_models.StartPairDrillRequest,
    ) -> ebs_20210730_models.StartPairDrillResponse:
        """
        After the disaster recovery drill is complete on the secondary disk, a pay-as-you-go drill disk that has the same capacity and category as the secondary disk is created in the zone where the secondary disk resides. The drill disk contains last-recovery-point data that can be used to test the completeness and correctness of applications.
        
        @param request: StartPairDrillRequest
        @return: StartPairDrillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_pair_drill_with_options_async(request, runtime)

    def start_replica_group_drill_with_options(
        self,
        request: ebs_20210730_models.StartReplicaGroupDrillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartReplicaGroupDrillResponse:
        """
        After the disaster recovery drill is complete on secondary disks, a pay-as-you-go drill disk is created in the zone where the secondary disk of each replication pair resides. The latest-recovery-point data is restored to the drill disks to test the completeness and correctness of applications.
        
        @param request: StartReplicaGroupDrillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartReplicaGroupDrillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartReplicaGroupDrill',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartReplicaGroupDrillResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_replica_group_drill_with_options_async(
        self,
        request: ebs_20210730_models.StartReplicaGroupDrillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StartReplicaGroupDrillResponse:
        """
        After the disaster recovery drill is complete on secondary disks, a pay-as-you-go drill disk is created in the zone where the secondary disk of each replication pair resides. The latest-recovery-point data is restored to the drill disks to test the completeness and correctness of applications.
        
        @param request: StartReplicaGroupDrillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartReplicaGroupDrillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartReplicaGroupDrill',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StartReplicaGroupDrillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_replica_group_drill(
        self,
        request: ebs_20210730_models.StartReplicaGroupDrillRequest,
    ) -> ebs_20210730_models.StartReplicaGroupDrillResponse:
        """
        After the disaster recovery drill is complete on secondary disks, a pay-as-you-go drill disk is created in the zone where the secondary disk of each replication pair resides. The latest-recovery-point data is restored to the drill disks to test the completeness and correctness of applications.
        
        @param request: StartReplicaGroupDrillRequest
        @return: StartReplicaGroupDrillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_replica_group_drill_with_options(request, runtime)

    async def start_replica_group_drill_async(
        self,
        request: ebs_20210730_models.StartReplicaGroupDrillRequest,
    ) -> ebs_20210730_models.StartReplicaGroupDrillResponse:
        """
        After the disaster recovery drill is complete on secondary disks, a pay-as-you-go drill disk is created in the zone where the secondary disk of each replication pair resides. The latest-recovery-point data is restored to the drill disks to test the completeness and correctness of applications.
        
        @param request: StartReplicaGroupDrillRequest
        @return: StartReplicaGroupDrillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_replica_group_drill_with_options_async(request, runtime)

    def stop_disk_replica_group_with_options(
        self,
        request: ebs_20210730_models.StopDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StopDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group that you want to stop must be in the **One-time Syncing** (`manual_syncing`), **Syncing** (`syncing`), **Normal** (`normal`), **Stopping** (`stopping`), **Stop Failed** (`stop_failed`), or **Stopped** (`stopped`) state.
        *   When a replication pair-consistent group is stopped, it enters the **Stopped** (`stopped`) state. If a replication pair-consistent group cannot be stopped, the state of the group remains unchanged or changes to **Stop Failed** (`stop_failed`). In this case, try again later.
        
        @param request: StopDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StopDiskReplicaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_disk_replica_group_with_options_async(
        self,
        request: ebs_20210730_models.StopDiskReplicaGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StopDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group that you want to stop must be in the **One-time Syncing** (`manual_syncing`), **Syncing** (`syncing`), **Normal** (`normal`), **Stopping** (`stopping`), **Stop Failed** (`stop_failed`), or **Stopped** (`stopped`) state.
        *   When a replication pair-consistent group is stopped, it enters the **Stopped** (`stopped`) state. If a replication pair-consistent group cannot be stopped, the state of the group remains unchanged or changes to **Stop Failed** (`stop_failed`). In this case, try again later.
        
        @param request: StopDiskReplicaGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDiskReplicaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_group_id):
            query['ReplicaGroupId'] = request.replica_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDiskReplicaGroup',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StopDiskReplicaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_disk_replica_group(
        self,
        request: ebs_20210730_models.StopDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.StopDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group that you want to stop must be in the **One-time Syncing** (`manual_syncing`), **Syncing** (`syncing`), **Normal** (`normal`), **Stopping** (`stopping`), **Stop Failed** (`stop_failed`), or **Stopped** (`stopped`) state.
        *   When a replication pair-consistent group is stopped, it enters the **Stopped** (`stopped`) state. If a replication pair-consistent group cannot be stopped, the state of the group remains unchanged or changes to **Stop Failed** (`stop_failed`). In this case, try again later.
        
        @param request: StopDiskReplicaGroupRequest
        @return: StopDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_disk_replica_group_with_options(request, runtime)

    async def stop_disk_replica_group_async(
        self,
        request: ebs_20210730_models.StopDiskReplicaGroupRequest,
    ) -> ebs_20210730_models.StopDiskReplicaGroupResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which the replication pair-consistent group feature is available, see [Overview](~~314563~~).
        *   The replication pair-consistent group that you want to stop must be in the **One-time Syncing** (`manual_syncing`), **Syncing** (`syncing`), **Normal** (`normal`), **Stopping** (`stopping`), **Stop Failed** (`stop_failed`), or **Stopped** (`stopped`) state.
        *   When a replication pair-consistent group is stopped, it enters the **Stopped** (`stopped`) state. If a replication pair-consistent group cannot be stopped, the state of the group remains unchanged or changes to **Stop Failed** (`stop_failed`). In this case, try again later.
        
        @param request: StopDiskReplicaGroupRequest
        @return: StopDiskReplicaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_disk_replica_group_with_options_async(request, runtime)

    def stop_disk_replica_pair_with_options(
        self,
        request: ebs_20210730_models.StopDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StopDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Initial Syncing** (`initial_syncing`), **Syncing** (`syncing`), **One-time Syncing** (`manual_syncing`), or **Normal** (`normal`) state can be stopped. When a replication pair is stopped, it enters the Stopped (`stopped`) state. The secondary disk rolls back to the point in time when the last async replication was complete and drops all the data that is being replicated from the primary disk.
        
        @param request: StopDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StopDiskReplicaPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_disk_replica_pair_with_options_async(
        self,
        request: ebs_20210730_models.StopDiskReplicaPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.StopDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Initial Syncing** (`initial_syncing`), **Syncing** (`syncing`), **One-time Syncing** (`manual_syncing`), or **Normal** (`normal`) state can be stopped. When a replication pair is stopped, it enters the Stopped (`stopped`) state. The secondary disk rolls back to the point in time when the last async replication was complete and drops all the data that is being replicated from the primary disk.
        
        @param request: StopDiskReplicaPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDiskReplicaPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replica_pair_id):
            query['ReplicaPairId'] = request.replica_pair_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDiskReplicaPair',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.StopDiskReplicaPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_disk_replica_pair(
        self,
        request: ebs_20210730_models.StopDiskReplicaPairRequest,
    ) -> ebs_20210730_models.StopDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Initial Syncing** (`initial_syncing`), **Syncing** (`syncing`), **One-time Syncing** (`manual_syncing`), or **Normal** (`normal`) state can be stopped. When a replication pair is stopped, it enters the Stopped (`stopped`) state. The secondary disk rolls back to the point in time when the last async replication was complete and drops all the data that is being replicated from the primary disk.
        
        @param request: StopDiskReplicaPairRequest
        @return: StopDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_disk_replica_pair_with_options(request, runtime)

    async def stop_disk_replica_pair_async(
        self,
        request: ebs_20210730_models.StopDiskReplicaPairRequest,
    ) -> ebs_20210730_models.StopDiskReplicaPairResponse:
        """
        ## [](#)Usage notes
        *   For information about the regions in which async replication is available, see [Overview](~~314563~~).
        *   Only replication pairs that are in the **Initial Syncing** (`initial_syncing`), **Syncing** (`syncing`), **One-time Syncing** (`manual_syncing`), or **Normal** (`normal`) state can be stopped. When a replication pair is stopped, it enters the Stopped (`stopped`) state. The secondary disk rolls back to the point in time when the last async replication was complete and drops all the data that is being replicated from the primary disk.
        
        @param request: StopDiskReplicaPairRequest
        @return: StopDiskReplicaPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_disk_replica_pair_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ebs_20210730_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.TagResourcesResponse:
        """
        Before you add tags to a resource, Alibaba Cloud checks the number of existing tags of the resource. If the maximum number of tags is reached, an error message is returned. For more information, see the "Tag limits" section in [Limits](~~25412~~).
        
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
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ebs_20210730_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.TagResourcesResponse:
        """
        Before you add tags to a resource, Alibaba Cloud checks the number of existing tags of the resource. If the maximum number of tags is reached, an error message is returned. For more information, see the "Tag limits" section in [Limits](~~25412~~).
        
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
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: ebs_20210730_models.TagResourcesRequest,
    ) -> ebs_20210730_models.TagResourcesResponse:
        """
        Before you add tags to a resource, Alibaba Cloud checks the number of existing tags of the resource. If the maximum number of tags is reached, an error message is returned. For more information, see the "Tag limits" section in [Limits](~~25412~~).
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ebs_20210730_models.TagResourcesRequest,
    ) -> ebs_20210730_models.TagResourcesResponse:
        """
        Before you add tags to a resource, Alibaba Cloud checks the number of existing tags of the resource. If the maximum number of tags is reached, an error message is returned. For more information, see the "Tag limits" section in [Limits](~~25412~~).
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unbind_enterprise_snapshot_policy_with_options(
        self,
        request: ebs_20210730_models.UnbindEnterpriseSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.UnbindEnterpriseSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_targets):
            query['DiskTargets'] = request.disk_targets
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindEnterpriseSnapshotPolicy',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.UnbindEnterpriseSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_enterprise_snapshot_policy_with_options_async(
        self,
        request: ebs_20210730_models.UnbindEnterpriseSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.UnbindEnterpriseSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disk_targets):
            query['DiskTargets'] = request.disk_targets
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindEnterpriseSnapshotPolicy',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.UnbindEnterpriseSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_enterprise_snapshot_policy(
        self,
        request: ebs_20210730_models.UnbindEnterpriseSnapshotPolicyRequest,
    ) -> ebs_20210730_models.UnbindEnterpriseSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_enterprise_snapshot_policy_with_options(request, runtime)

    async def unbind_enterprise_snapshot_policy_async(
        self,
        request: ebs_20210730_models.UnbindEnterpriseSnapshotPolicyRequest,
    ) -> ebs_20210730_models.UnbindEnterpriseSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_enterprise_snapshot_policy_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ebs_20210730_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.UntagResourcesResponse:
        """
        You can remove up to 20 tags at a time.
        *   After a tag is removed from an EBS resource, the tag is automatically deleted if the tag is not added to any instance.
        
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
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ebs_20210730_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.UntagResourcesResponse:
        """
        You can remove up to 20 tags at a time.
        *   After a tag is removed from an EBS resource, the tag is automatically deleted if the tag is not added to any instance.
        
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
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: ebs_20210730_models.UntagResourcesRequest,
    ) -> ebs_20210730_models.UntagResourcesResponse:
        """
        You can remove up to 20 tags at a time.
        *   After a tag is removed from an EBS resource, the tag is automatically deleted if the tag is not added to any instance.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ebs_20210730_models.UntagResourcesRequest,
    ) -> ebs_20210730_models.UntagResourcesResponse:
        """
        You can remove up to 20 tags at a time.
        *   After a tag is removed from an EBS resource, the tag is automatically deleted if the tag is not added to any instance.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_enterprise_snapshot_policy_with_options(
        self,
        tmp_req: ebs_20210730_models.UpdateEnterpriseSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.UpdateEnterpriseSnapshotPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = ebs_20210730_models.UpdateEnterpriseSnapshotPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cross_region_copy_info):
            request.cross_region_copy_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cross_region_copy_info, 'CrossRegionCopyInfo', 'json')
        if not UtilClient.is_unset(tmp_req.retain_rule):
            request.retain_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retain_rule, 'RetainRule', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        if not UtilClient.is_unset(tmp_req.special_retain_rules):
            request.special_retain_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.special_retain_rules, 'SpecialRetainRules', 'json')
        if not UtilClient.is_unset(tmp_req.storage_rule):
            request.storage_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.storage_rule, 'StorageRule', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_region_copy_info_shrink):
            query['CrossRegionCopyInfo'] = request.cross_region_copy_info_shrink
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retain_rule_shrink):
            query['RetainRule'] = request.retain_rule_shrink
        if not UtilClient.is_unset(request.schedule_shrink):
            query['Schedule'] = request.schedule_shrink
        if not UtilClient.is_unset(request.special_retain_rules_shrink):
            query['SpecialRetainRules'] = request.special_retain_rules_shrink
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.storage_rule_shrink):
            query['StorageRule'] = request.storage_rule_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseSnapshotPolicy',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.UpdateEnterpriseSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_enterprise_snapshot_policy_with_options_async(
        self,
        tmp_req: ebs_20210730_models.UpdateEnterpriseSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.UpdateEnterpriseSnapshotPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = ebs_20210730_models.UpdateEnterpriseSnapshotPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cross_region_copy_info):
            request.cross_region_copy_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cross_region_copy_info, 'CrossRegionCopyInfo', 'json')
        if not UtilClient.is_unset(tmp_req.retain_rule):
            request.retain_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retain_rule, 'RetainRule', 'json')
        if not UtilClient.is_unset(tmp_req.schedule):
            request.schedule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule, 'Schedule', 'json')
        if not UtilClient.is_unset(tmp_req.special_retain_rules):
            request.special_retain_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.special_retain_rules, 'SpecialRetainRules', 'json')
        if not UtilClient.is_unset(tmp_req.storage_rule):
            request.storage_rule_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.storage_rule, 'StorageRule', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_region_copy_info_shrink):
            query['CrossRegionCopyInfo'] = request.cross_region_copy_info_shrink
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retain_rule_shrink):
            query['RetainRule'] = request.retain_rule_shrink
        if not UtilClient.is_unset(request.schedule_shrink):
            query['Schedule'] = request.schedule_shrink
        if not UtilClient.is_unset(request.special_retain_rules_shrink):
            query['SpecialRetainRules'] = request.special_retain_rules_shrink
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.storage_rule_shrink):
            query['StorageRule'] = request.storage_rule_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnterpriseSnapshotPolicy',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.UpdateEnterpriseSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_enterprise_snapshot_policy(
        self,
        request: ebs_20210730_models.UpdateEnterpriseSnapshotPolicyRequest,
    ) -> ebs_20210730_models.UpdateEnterpriseSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_enterprise_snapshot_policy_with_options(request, runtime)

    async def update_enterprise_snapshot_policy_async(
        self,
        request: ebs_20210730_models.UpdateEnterpriseSnapshotPolicyRequest,
    ) -> ebs_20210730_models.UpdateEnterpriseSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_enterprise_snapshot_policy_with_options_async(request, runtime)

    def update_solution_instance_attribute_with_options(
        self,
        request: ebs_20210730_models.UpdateSolutionInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.UpdateSolutionInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.solution_instance_id):
            query['SolutionInstanceId'] = request.solution_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSolutionInstanceAttribute',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.UpdateSolutionInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_solution_instance_attribute_with_options_async(
        self,
        request: ebs_20210730_models.UpdateSolutionInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ebs_20210730_models.UpdateSolutionInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.solution_instance_id):
            query['SolutionInstanceId'] = request.solution_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSolutionInstanceAttribute',
            version='2021-07-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ebs_20210730_models.UpdateSolutionInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_solution_instance_attribute(
        self,
        request: ebs_20210730_models.UpdateSolutionInstanceAttributeRequest,
    ) -> ebs_20210730_models.UpdateSolutionInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_solution_instance_attribute_with_options(request, runtime)

    async def update_solution_instance_attribute_async(
        self,
        request: ebs_20210730_models.UpdateSolutionInstanceAttributeRequest,
    ) -> ebs_20210730_models.UpdateSolutionInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_solution_instance_attribute_with_options_async(request, runtime)
