# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ReplaceAppGroupCommodityCodeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ReplaceAppGroupCommodityCodeResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.ReplaceAppGroupCommodityCodeResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class ReplaceAppGroupCommodityCodeResponseBodyResult(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        charging_way: int = None,
        commodity_code: str = None,
        created: int = None,
        current_version: str = None,
        description: str = None,
        expire_on: str = None,
        first_rank_algo_deployment_id: int = None,
        has_pending_quota_review_task: int = None,
        id: str = None,
        instance_id: str = None,
        lock_mode: str = None,
        locked_by_expiration: int = None,
        name: str = None,
        pending_second_rank_algo_deployment_id: int = None,
        processing_order_id: str = None,
        produced: int = None,
        project_id: str = None,
        quota: main_models.ReplaceAppGroupCommodityCodeResponseBodyResultQuota = None,
        second_rank_algo_deployment_id: int = None,
        status: str = None,
        switched_time: int = None,
        type: str = None,
        updated: int = None,
        versions: List[str] = None,
    ):
        # The billing method. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go.
        # *   PREPAY: subscription.
        self.charge_type = charge_type
        # The billing type. Valid values:
        # 
        # *   1: computing resources.
        # *   2: queries per second (QPS).
        self.charging_way = charging_way
        # The code of the commodity.
        self.commodity_code = commodity_code
        # The timestamp when the application was created.
        self.created = created
        # The ID of the current online version.
        self.current_version = current_version
        # The description of the application.
        self.description = description
        # The expiration time.
        self.expire_on = expire_on
        # The ID of the rough sort expression.
        self.first_rank_algo_deployment_id = first_rank_algo_deployment_id
        # The approval state of the quotas. Valid values:
        # 
        # *   0: The approval status is normal.
        # *   1: The quotas are being approved.
        self.has_pending_quota_review_task = has_pending_quota_review_task
        # The application ID.
        self.id = id
        # The instance ID.
        self.instance_id = instance_id
        # The lock state. Valid values:
        # 
        # *   Unlock: The instance is unlocked.
        # *   LockByExpiration: The instance is automatically locked after it expires.
        # *   ManualLock: The instance is manually locked.
        self.lock_mode = lock_mode
        # Indicates whether the instance is automatically locked after it expires. Valid values:
        # 
        # *   0: The instance is not automatically locked after it expires.
        # *   1: The instance is automatically locked after it expires.
        self.locked_by_expiration = locked_by_expiration
        # The name of the order.
        self.name = name
        # The ID of the fine sort expression that is being created.
        self.pending_second_rank_algo_deployment_id = pending_second_rank_algo_deployment_id
        # The ID of the order that is in progress.
        self.processing_order_id = processing_order_id
        # Indicates whether the order is produced.
        self.produced = produced
        # The name of the A/B test group.
        self.project_id = project_id
        # The configuration information.
        self.quota = quota
        # The ID of the fine sort expression.
        self.second_rank_algo_deployment_id = second_rank_algo_deployment_id
        # The status of the application.
        self.status = status
        # The timestamp when the current online version was published.
        self.switched_time = switched_time
        # The type of the application.
        self.type = type
        # The timestamp when the application was updated.
        self.updated = updated
        # The versions.
        self.versions = versions

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.charging_way is not None:
            result['chargingWay'] = self.charging_way

        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        if self.created is not None:
            result['created'] = self.created

        if self.current_version is not None:
            result['currentVersion'] = self.current_version

        if self.description is not None:
            result['description'] = self.description

        if self.expire_on is not None:
            result['expireOn'] = self.expire_on

        if self.first_rank_algo_deployment_id is not None:
            result['firstRankAlgoDeploymentId'] = self.first_rank_algo_deployment_id

        if self.has_pending_quota_review_task is not None:
            result['hasPendingQuotaReviewTask'] = self.has_pending_quota_review_task

        if self.id is not None:
            result['id'] = self.id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode

        if self.locked_by_expiration is not None:
            result['lockedByExpiration'] = self.locked_by_expiration

        if self.name is not None:
            result['name'] = self.name

        if self.pending_second_rank_algo_deployment_id is not None:
            result['pendingSecondRankAlgoDeploymentId'] = self.pending_second_rank_algo_deployment_id

        if self.processing_order_id is not None:
            result['processingOrderId'] = self.processing_order_id

        if self.produced is not None:
            result['produced'] = self.produced

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

        if self.second_rank_algo_deployment_id is not None:
            result['secondRankAlgoDeploymentId'] = self.second_rank_algo_deployment_id

        if self.status is not None:
            result['status'] = self.status

        if self.switched_time is not None:
            result['switchedTime'] = self.switched_time

        if self.type is not None:
            result['type'] = self.type

        if self.updated is not None:
            result['updated'] = self.updated

        if self.versions is not None:
            result['versions'] = self.versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('chargingWay') is not None:
            self.charging_way = m.get('chargingWay')

        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('expireOn') is not None:
            self.expire_on = m.get('expireOn')

        if m.get('firstRankAlgoDeploymentId') is not None:
            self.first_rank_algo_deployment_id = m.get('firstRankAlgoDeploymentId')

        if m.get('hasPendingQuotaReviewTask') is not None:
            self.has_pending_quota_review_task = m.get('hasPendingQuotaReviewTask')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')

        if m.get('lockedByExpiration') is not None:
            self.locked_by_expiration = m.get('lockedByExpiration')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pendingSecondRankAlgoDeploymentId') is not None:
            self.pending_second_rank_algo_deployment_id = m.get('pendingSecondRankAlgoDeploymentId')

        if m.get('processingOrderId') is not None:
            self.processing_order_id = m.get('processingOrderId')

        if m.get('produced') is not None:
            self.produced = m.get('produced')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('quota') is not None:
            temp_model = main_models.ReplaceAppGroupCommodityCodeResponseBodyResultQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        if m.get('secondRankAlgoDeploymentId') is not None:
            self.second_rank_algo_deployment_id = m.get('secondRankAlgoDeploymentId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('switchedTime') is not None:
            self.switched_time = m.get('switchedTime')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        if m.get('versions') is not None:
            self.versions = m.get('versions')

        return self

class ReplaceAppGroupCommodityCodeResponseBodyResultQuota(DaraModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        spec: str = None,
    ):
        # The number of computing resources configured.
        self.compute_resource = compute_resource
        # The storage capacity.
        self.doc_size = doc_size
        # The specifications configured.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource

        if self.doc_size is not None:
            result['docSize'] = self.doc_size

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')

        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

